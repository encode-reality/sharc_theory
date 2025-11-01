"""
Soup population dynamics engine for BFF abiogenesis experiment.

The Soup manages a population of tapes and orchestrates their pairwise interactions.
This is where the magic of spontaneous replication emergence happens.
"""

import random
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional
from .tape import Tape
from .brainfuck import BrainfuckInterpreter


@dataclass
class InteractionResult:
    """
    Result of a single pairwise interaction.

    Attributes:
        operations: Number of operations executed during interaction
        idx1: Index of first tape
        idx2: Index of second tape
        terminated: Whether execution completed normally
        crashed: Whether execution crashed
        timed_out: Whether execution timed out
    """
    operations: int
    idx1: int
    idx2: int
    terminated: bool
    crashed: bool = False
    timed_out: bool = False


class Soup:
    """
    Population of interacting tapes (the primordial soup).

    The Soup maintains a population of tapes and orchestrates their
    pairwise interactions. This is the core engine for the BFF
    abiogenesis experiment.

    Key features:
    - Random pairwise selection
    - Tape concatenation and execution
    - Optional mutation
    - State tracking and checkpointing
    """

    def __init__(
        self,
        size: int,
        tape_length: int = 64,
        mutation_rate: float = 0.0,
        seed: Optional[int] = None
    ):
        """
        Initialize a soup of random tapes.

        Args:
            size: Number of tapes in the soup
            tape_length: Length of each tape in bytes
            mutation_rate: Probability of mutation per byte per interaction
            seed: Random seed for reproducibility
        """
        self.size = size
        self.tape_length = tape_length
        self.mutation_rate = mutation_rate
        self.interaction_count = 0

        # Set random seed if provided
        if seed is not None:
            random.seed(seed)
            self._rng = random.Random(seed)
        else:
            self._rng = random.Random()

        # Initialize population with random tapes
        self.tapes: List[Tape] = []
        for i in range(size):
            if seed is not None:
                tape_seed = seed + i  # Different seed for each tape
                self.tapes.append(Tape(length=tape_length, seed=tape_seed))
            else:
                self.tapes.append(Tape(length=tape_length))

    def select_pair(self) -> Tuple[Tape, Tape, int, int]:
        """
        Select two random tapes for interaction.

        Returns:
            Tuple of (tape1, tape2, index1, index2)
        """
        idx1 = self._rng.randint(0, self.size - 1)
        idx2 = self._rng.randint(0, self.size - 1)

        # Ensure different tapes
        while idx2 == idx1:
            idx2 = self._rng.randint(0, self.size - 1)

        return self.tapes[idx1], self.tapes[idx2], idx1, idx2

    def interact_pair(
        self,
        idx1: int,
        idx2: int,
        max_ops: int = 10000,
        timeout_prob: float = 0.0
    ) -> InteractionResult:
        """
        Execute interaction between two specific tapes.

        The tapes are concatenated end-to-end and executed as a single program.
        After execution, they are separated and put back in the soup.

        Args:
            idx1: Index of first tape
            idx2: Index of second tape
            max_ops: Maximum operations per interaction
            timeout_prob: Probability of random timeout per operation

        Returns:
            InteractionResult with execution metadata
        """
        tape1 = self.tapes[idx1]
        tape2 = self.tapes[idx2]

        # Concatenate tapes
        combined_data = tape1.data + tape2.data
        combined_tape = Tape(length=len(combined_data), data=combined_data)

        # Execute
        interpreter = BrainfuckInterpreter(combined_tape)
        exec_result = interpreter.run_from_tape(
            start_position=0,
            max_ops=max_ops,
            timeout_prob=timeout_prob
        )

        # Separate and update tapes
        # Note: The combined tape may have been modified during execution
        tape1.data = combined_tape.data[:self.tape_length]
        tape2.data = combined_tape.data[self.tape_length:]

        return InteractionResult(
            operations=exec_result.operations,
            idx1=idx1,
            idx2=idx2,
            terminated=exec_result.terminated,
            crashed=exec_result.crashed,
            timed_out=exec_result.timed_out
        )

    def interact_once(
        self,
        max_ops: int = 10000,
        timeout_prob: float = 0.0
    ) -> InteractionResult:
        """
        Perform one random pairwise interaction.

        Args:
            max_ops: Maximum operations per interaction
            timeout_prob: Probability of random timeout

        Returns:
            InteractionResult
        """
        _, _, idx1, idx2 = self.select_pair()
        result = self.interact_pair(idx1, idx2, max_ops, timeout_prob)

        self.interaction_count += 1

        # Apply mutations if enabled
        if self.mutation_rate > 0:
            self.apply_mutations()

        return result

    def run(
        self,
        num_interactions: int,
        max_ops: int = 10000,
        timeout_prob: float = 0.0
    ) -> List[InteractionResult]:
        """
        Run multiple interactions.

        Args:
            num_interactions: Number of interactions to perform
            max_ops: Maximum operations per interaction
            timeout_prob: Probability of random timeout

        Returns:
            List of InteractionResult objects
        """
        results = []

        for _ in range(num_interactions):
            result = self.interact_once(max_ops, timeout_prob)
            results.append(result)

        return results

    def apply_mutations(self) -> None:
        """
        Apply random mutations to the soup.

        Each byte has a probability of mutation_rate of being randomized.
        """
        if self.mutation_rate <= 0:
            return

        for tape in self.tapes:
            for i in range(tape.length):
                if self._rng.random() < self.mutation_rate:
                    tape.data[i] = self._rng.randint(0, 255)

    def get_tape_hashes(self) -> List[str]:
        """
        Get hash of each tape in soup.

        Returns:
            List of hash strings
        """
        return [tape.hash() for tape in self.tapes]

    def count_unique_tapes(self) -> int:
        """
        Count number of unique tapes in soup.

        Returns:
            Number of distinct tapes (by hash)
        """
        hashes = self.get_tape_hashes()
        return len(set(hashes))

    def get_diversity(self) -> float:
        """
        Calculate diversity metric (ratio of unique to total tapes).

        Returns:
            Diversity in range [0, 1], where 1 = all unique
        """
        return self.count_unique_tapes() / self.size

    def get_state(self) -> Dict:
        """
        Get complete soup state for checkpointing.

        Returns:
            Dictionary with all soup state
        """
        return {
            'size': self.size,
            'tape_length': self.tape_length,
            'mutation_rate': self.mutation_rate,
            'interaction_count': self.interaction_count,
            'tapes': [tape.to_dict() for tape in self.tapes]
        }

    @classmethod
    def from_state(cls, state: Dict) -> 'Soup':
        """
        Restore soup from saved state.

        Args:
            state: Dictionary from get_state()

        Returns:
            Reconstructed Soup
        """
        # Create soup without initializing random tapes
        soup = cls.__new__(cls)
        soup.size = state['size']
        soup.tape_length = state['tape_length']
        soup.mutation_rate = state['mutation_rate']
        soup.interaction_count = state['interaction_count']
        soup._rng = random.Random()

        # Restore tapes
        soup.tapes = [Tape.from_dict(tape_dict) for tape_dict in state['tapes']]

        return soup

    def __repr__(self) -> str:
        """String representation."""
        unique = self.count_unique_tapes()
        return (
            f"Soup(size={self.size}, tape_length={self.tape_length}, "
            f"interactions={self.interaction_count}, unique_tapes={unique})"
        )
