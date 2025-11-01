"""
Tests for the modified Brainfuck interpreter.

This implements the BFF variant where code and data share the same tape,
with three pointers: instruction pointer, data pointer, and console pointer.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from core.tape import Tape
from core.brainfuck import BrainfuckInterpreter, ExecutionResult


class TestBasicInstructions:
    """Test individual Brainfuck instructions."""

    def test_move_data_pointer_right(self):
        """Test > instruction: move data pointer right."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        assert interp.data_pointer == 0
        interp.execute_instruction('>')
        assert interp.data_pointer == 1

    def test_move_data_pointer_left(self):
        """Test < instruction: move data pointer left."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)
        interp.data_pointer = 5

        interp.execute_instruction('<')
        assert interp.data_pointer == 4

    def test_increment_byte(self):
        """Test + instruction: increment byte at data pointer."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        assert tape.get_byte(0) == 0
        interp.execute_instruction('+')
        assert tape.get_byte(0) == 1

    def test_decrement_byte(self):
        """Test - instruction: decrement byte at data pointer."""
        tape = Tape(length=64, data=[100] + [0] * 63)
        interp = BrainfuckInterpreter(tape)

        interp.execute_instruction('-')
        assert tape.get_byte(0) == 99

    def test_copy_instruction(self):
        """Test , instruction: copy from console pointer to data pointer."""
        tape = Tape(length=64, data=[42] + [0] * 63)
        interp = BrainfuckInterpreter(tape)
        interp.console_pointer = 0
        interp.data_pointer = 1

        interp.execute_instruction(',')
        assert tape.get_byte(1) == 42  # Copied from position 0

    def test_no_op_ignored(self):
        """Test that invalid bytes (no-ops) are ignored."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        # Byte value 99 is not a valid instruction
        interp.execute_instruction(chr(99))
        # Should not crash, just do nothing


class TestPointerWrapping:
    """Test pointer wrapping behavior."""

    def test_data_pointer_wraps_forward(self):
        """Data pointer should wrap to 0 at end of tape."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)
        interp.data_pointer = 63

        interp.execute_instruction('>')
        assert interp.data_pointer == 0

    def test_data_pointer_wraps_backward(self):
        """Data pointer should wrap to end at beginning of tape."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)
        interp.data_pointer = 0

        interp.execute_instruction('<')
        assert interp.data_pointer == 63

    def test_console_pointer_wraps(self):
        """Console pointer should wrap like data pointer."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)
        interp.console_pointer = 63

        interp.move_console_right()
        assert interp.console_pointer == 0


class TestLoops:
    """Test loop execution with [ and ]."""

    def test_simple_loop_executes(self):
        """Test that a simple loop executes correctly."""
        # Program: set byte 0 to 5, then loop decrementing until 0
        # +++++[-]  -> should result in byte 0 = 0
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        # Manually set up: [5, 0, 0, ...]
        tape.set_byte(0, 5)

        # Execute loop that decrements: [-]
        # [ at position 0, - at position 1, ] at position 2
        program = '[-]'
        result = interp.run(program)

        assert tape.get_byte(0) == 0
        assert result.terminated

    def test_loop_skipped_if_zero(self):
        """Test that loop is skipped when byte is 0."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        # Byte is 0, so [+] should be skipped
        program = '[+]'
        result = interp.run(program)

        assert tape.get_byte(0) == 0  # Should still be 0
        assert result.operations < 5  # Should not loop

    def test_nested_loops_not_crash(self):
        """Test that nested loops don't crash."""
        tape = Tape(length=64, data=[2, 3] + [0] * 62)
        interp = BrainfuckInterpreter(tape)

        # Nested loop structure
        program = '[>[-]<-]'
        result = interp.run(program, max_ops=1000)

        # Should eventually terminate
        assert result.terminated or result.operations >= 1000


class TestProgramExecution:
    """Test full program execution."""

    def test_empty_program(self):
        """Empty program should do nothing."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        result = interp.run('')
        assert result.operations == 0
        assert result.terminated

    def test_simple_program(self):
        """Test a simple program that increments and moves."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        # Increment first byte, move right, increment second byte
        program = '+>+'
        result = interp.run(program)

        assert tape.get_byte(0) == 1
        assert tape.get_byte(1) == 1
        assert result.operations == 3  # +, >, +

    def test_max_operations_limit(self):
        """Test that execution stops at max operations."""
        tape = Tape(length=64, data=[1] + [0] * 63)
        interp = BrainfuckInterpreter(tape)

        # Infinite loop: [+]
        program = '[+]'
        result = interp.run(program, max_ops=100)

        assert result.operations >= 100
        assert not result.terminated

    def test_operation_counting(self):
        """Test that operations are counted correctly."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        # 5 real instructions
        program = '++>--'
        result = interp.run(program)

        assert result.operations == 5


class TestSelfModification:
    """Test self-modifying code capabilities."""

    def test_code_can_modify_itself(self):
        """Test that code can modify its own tape."""
        # This is the key feature for BFF abiogenesis
        tape = Tape(length=64, data=[43] + [0] * 63)  # 43 = '+'
        interp = BrainfuckInterpreter(tape)

        # Execute the + instruction at position 0
        # This should increment byte at data pointer (also position 0)
        # Changing 43 to 44 ('+' to ',')
        result = interp.run('+', start_position=0)

        assert tape.get_byte(0) == 44  # Modified from 43


class TestExecutionResult:
    """Test the ExecutionResult dataclass."""

    def test_result_contains_metadata(self):
        """Test that result contains execution metadata."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        result = interp.run('++>--')

        assert hasattr(result, 'operations')
        assert hasattr(result, 'terminated')
        assert hasattr(result, 'final_instruction_pointer')
        assert hasattr(result, 'final_data_pointer')

    def test_result_tracks_final_state(self):
        """Test that result tracks interpreter final state."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        result = interp.run('>>++')

        assert result.final_data_pointer == 2
        assert result.final_instruction_pointer > 0


class TestPairwiseExecution:
    """Test execution of two concatenated tapes (core BFF mechanism)."""

    def test_two_tapes_concatenated(self):
        """Test running two 64-byte tapes end-to-end."""
        tape1 = Tape(length=64, data=[43] * 64)  # All '+' instructions
        tape2 = Tape(length=64, data=[45] * 64)  # All '-' instructions

        # Concatenate
        combined_data = tape1.data + tape2.data
        combined_tape = Tape(length=128, data=combined_data)

        interp = BrainfuckInterpreter(combined_tape)
        result = interp.run_from_tape()

        # Should execute many operations
        assert result.operations > 0


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_unmatched_close_bracket_crashes(self):
        """Test that unmatched ] causes controlled termination."""
        tape = Tape(length=64, data=[0] * 64)
        interp = BrainfuckInterpreter(tape)

        # Unmatched ]
        result = interp.run(']')

        # Should crash gracefully
        assert result.crashed

    def test_timeout_mechanism(self):
        """Test probabilistic timeout during execution."""
        tape = Tape(length=64, data=[1] + [0] * 63)
        interp = BrainfuckInterpreter(tape)

        # Infinite loop with certain timeout
        program = '[+]'
        result = interp.run(program, max_ops=10000, timeout_prob=1.0)

        # Should stop due to timeout
        assert result.operations < 10000 or result.timed_out

    def test_very_long_program(self):
        """Test that very long programs can execute."""
        tape = Tape(length=128, data=[43] * 128)  # 128 '+' instructions
        interp = BrainfuckInterpreter(tape)

        result = interp.run_from_tape(max_ops=200)

        assert result.operations > 100
