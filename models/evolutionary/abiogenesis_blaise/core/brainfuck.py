"""
Modified Brainfuck interpreter for BFF abiogenesis experiment.

This implements the BFF variant where:
1. Code and data share the same tape (self-modifying code)
2. Three pointers: instruction pointer, data pointer, console pointer
3. Only 7 instructions: < > + - , [ ]
4. All other bytes are no-ops
"""

import random
from dataclasses import dataclass
from typing import Optional
from .tape import Tape


# Brainfuck instruction characters
INST_LEFT = ord('<')         # 60: move data pointer left
INST_RIGHT = ord('>')        # 62: move data pointer right
INST_INCREMENT = ord('+')    # 43: increment byte at data pointer
INST_DECREMENT = ord('-')    # 45: decrement byte at data pointer
INST_COPY = ord(',')         # 44: copy from console pointer to data pointer
INST_LOOP_START = ord('[')   # 91: begin loop
INST_LOOP_END = ord(']')     # 93: end loop


@dataclass
class ExecutionResult:
    """
    Result of executing a Brainfuck program.

    Attributes:
        operations: Number of operations executed
        terminated: Whether program completed normally
        crashed: Whether program crashed (e.g., unmatched bracket)
        timed_out: Whether execution stopped due to probabilistic timeout
        final_instruction_pointer: Final position of instruction pointer
        final_data_pointer: Final position of data pointer
        final_console_pointer: Final position of console pointer
    """
    operations: int
    terminated: bool
    crashed: bool = False
    timed_out: bool = False
    final_instruction_pointer: int = 0
    final_data_pointer: int = 0
    final_console_pointer: int = 0


class BrainfuckInterpreter:
    """
    Modified Brainfuck interpreter for BFF experiment.

    In BFF:
    - The tape contains both code and data
    - Three pointers operate on the same tape
    - Programs can modify themselves during execution
    - Most bytes are no-ops (only 7 valid instructions)
    """

    def __init__(self, tape: Tape):
        """
        Initialize interpreter with a tape.

        Args:
            tape: Tape containing both code and data
        """
        self.tape = tape
        self.instruction_pointer = 0  # Where we're reading instructions from
        self.data_pointer = 0         # Where data operations happen
        self.console_pointer = 0      # Where copy operations read from

    def execute_instruction(self, instruction: str) -> bool:
        """
        Execute a single Brainfuck instruction.

        Args:
            instruction: Single character instruction

        Returns:
            True if instruction was valid, False if no-op
        """
        inst_byte = ord(instruction) if len(instruction) == 1 else -1

        if inst_byte == INST_RIGHT:
            self.move_data_right()
            return True

        elif inst_byte == INST_LEFT:
            self.move_data_left()
            return True

        elif inst_byte == INST_INCREMENT:
            self.tape.increment_byte(self.data_pointer)
            return True

        elif inst_byte == INST_DECREMENT:
            self.tape.decrement_byte(self.data_pointer)
            return True

        elif inst_byte == INST_COPY:
            # Copy from console pointer to data pointer
            value = self.tape.get_byte(self.console_pointer)
            self.tape.set_byte(self.data_pointer, value)
            self.move_console_right()
            return True

        # Loops are handled separately in run() method
        # Other bytes are no-ops
        return False

    def move_data_right(self):
        """Move data pointer right with wrapping."""
        self.data_pointer = (self.data_pointer + 1) % self.tape.length

    def move_data_left(self):
        """Move data pointer left with wrapping."""
        self.data_pointer = (self.data_pointer - 1) % self.tape.length

    def move_console_right(self):
        """Move console pointer right with wrapping."""
        self.console_pointer = (self.console_pointer + 1) % self.tape.length

    def run(
        self,
        program: str = '',
        start_position: int = 0,
        max_ops: int = 10000,
        timeout_prob: float = 0.0
    ) -> ExecutionResult:
        """
        Run a Brainfuck program.

        Args:
            program: Program string to execute. If empty, reads from tape.
            start_position: Starting instruction pointer position
            max_ops: Maximum operations before forced termination
            timeout_prob: Probability per operation of random timeout (0.0 to 1.0)

        Returns:
            ExecutionResult with execution metadata
        """
        if program:
            # Run explicit program string
            return self._run_string(program, max_ops, timeout_prob)
        else:
            # Run from tape itself (self-modifying code)
            return self.run_from_tape(start_position, max_ops, timeout_prob)

    def _run_string(
        self,
        program: str,
        max_ops: int,
        timeout_prob: float
    ) -> ExecutionResult:
        """Run program from explicit string."""
        operations = 0
        ip = 0  # Instruction pointer in program string

        # Build bracket matching map
        bracket_map = self._build_bracket_map(program)
        if bracket_map is None:
            # Unmatched brackets
            return ExecutionResult(
                operations=0,
                terminated=False,
                crashed=True,
                final_instruction_pointer=0,
                final_data_pointer=self.data_pointer,
                final_console_pointer=self.console_pointer
            )

        while ip < len(program) and operations < max_ops:
            # Probabilistic timeout (for BFF simulation)
            if timeout_prob > 0 and random.random() < timeout_prob:
                return ExecutionResult(
                    operations=operations,
                    terminated=False,
                    timed_out=True,
                    final_instruction_pointer=ip,
                    final_data_pointer=self.data_pointer,
                    final_console_pointer=self.console_pointer
                )

            instruction = program[ip]
            inst_byte = ord(instruction)

            # Handle loops specially
            if inst_byte == INST_LOOP_START:
                if self.tape.get_byte(self.data_pointer) == 0:
                    # Skip to matching ]
                    ip = bracket_map[ip]
                operations += 1

            elif inst_byte == INST_LOOP_END:
                if self.tape.get_byte(self.data_pointer) != 0:
                    # Jump back to matching [
                    ip = bracket_map[ip]
                operations += 1

            else:
                # Regular instruction
                if self.execute_instruction(instruction):
                    operations += 1

            ip += 1

        return ExecutionResult(
            operations=operations,
            terminated=(ip >= len(program)),
            crashed=False,
            timed_out=False,
            final_instruction_pointer=ip,
            final_data_pointer=self.data_pointer,
            final_console_pointer=self.console_pointer
        )

    def run_from_tape(
        self,
        start_position: int = 0,
        max_ops: int = 10000,
        timeout_prob: float = 0.0
    ) -> ExecutionResult:
        """
        Run program from the tape itself (self-modifying code).

        This is the core mechanism for BFF: the tape contains both
        the program and the data it operates on.

        Args:
            start_position: Starting instruction pointer
            max_ops: Maximum operations before forced termination
            timeout_prob: Probability per operation of random timeout

        Returns:
            ExecutionResult with execution metadata
        """
        operations = 0
        self.instruction_pointer = start_position

        # Pre-compute bracket matching (gets stale if code modifies itself,
        # but that's okay - we'll just crash or behave weirdly, like life!)
        bracket_map = self._build_bracket_map_from_tape()

        while operations < max_ops:
            # Probabilistic timeout
            if timeout_prob > 0 and random.random() < timeout_prob:
                return ExecutionResult(
                    operations=operations,
                    terminated=False,
                    timed_out=True,
                    final_instruction_pointer=self.instruction_pointer,
                    final_data_pointer=self.data_pointer,
                    final_console_pointer=self.console_pointer
                )

            # Check if we've run off the end of the tape
            if self.instruction_pointer >= self.tape.length:
                return ExecutionResult(
                    operations=operations,
                    terminated=True,
                    final_instruction_pointer=self.instruction_pointer,
                    final_data_pointer=self.data_pointer,
                    final_console_pointer=self.console_pointer
                )

            # Fetch instruction from tape
            inst_byte = self.tape.get_byte(self.instruction_pointer)

            # Handle loops
            if inst_byte == INST_LOOP_START:
                if self.tape.get_byte(self.data_pointer) == 0:
                    # Skip to matching ] (or end of tape if not found)
                    if self.instruction_pointer in bracket_map:
                        self.instruction_pointer = bracket_map[self.instruction_pointer]
                    else:
                        # Unmatched bracket - crash
                        return ExecutionResult(
                            operations=operations,
                            terminated=False,
                            crashed=True,
                            final_instruction_pointer=self.instruction_pointer,
                            final_data_pointer=self.data_pointer,
                            final_console_pointer=self.console_pointer
                        )
                operations += 1

            elif inst_byte == INST_LOOP_END:
                if self.tape.get_byte(self.data_pointer) != 0:
                    # Jump back to matching [
                    if self.instruction_pointer in bracket_map:
                        self.instruction_pointer = bracket_map[self.instruction_pointer]
                    else:
                        # Unmatched bracket - crash
                        return ExecutionResult(
                            operations=operations,
                            terminated=False,
                            crashed=True,
                            final_instruction_pointer=self.instruction_pointer,
                            final_data_pointer=self.data_pointer,
                            final_console_pointer=self.console_pointer
                        )
                operations += 1

            else:
                # Regular instruction
                instruction = chr(inst_byte)
                if self.execute_instruction(instruction):
                    operations += 1

            self.instruction_pointer += 1

        # Reached max operations
        return ExecutionResult(
            operations=operations,
            terminated=False,
            final_instruction_pointer=self.instruction_pointer,
            final_data_pointer=self.data_pointer,
            final_console_pointer=self.console_pointer
        )

    def _build_bracket_map(self, program: str) -> Optional[dict]:
        """
        Build mapping of bracket positions for jumps.

        Args:
            program: Program string

        Returns:
            Dictionary mapping [ positions to ] positions and vice versa,
            or None if brackets are unmatched
        """
        bracket_map = {}
        stack = []

        for i, char in enumerate(program):
            if char == '[':
                stack.append(i)
            elif char == ']':
                if not stack:
                    return None  # Unmatched ]
                start = stack.pop()
                bracket_map[start] = i
                bracket_map[i] = start

        if stack:
            return None  # Unmatched [

        return bracket_map

    def _build_bracket_map_from_tape(self) -> dict:
        """
        Build bracket mapping from tape data.

        Returns:
            Dictionary mapping bracket positions (best effort, may be incomplete)
        """
        bracket_map = {}
        stack = []

        for i in range(self.tape.length):
            byte = self.tape.get_byte(i)
            if byte == INST_LOOP_START:
                stack.append(i)
            elif byte == INST_LOOP_END:
                if stack:
                    start = stack.pop()
                    bracket_map[start] = i
                    bracket_map[i] = start

        return bracket_map
