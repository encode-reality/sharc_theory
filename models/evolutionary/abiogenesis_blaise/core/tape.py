"""
Tape data structure for BFF (Brainfuck) abiogenesis experiment.

A Tape represents a sequence of bytes that can contain both code and data.
In the BFF experiment, tapes are 64 bytes long and interact in pairs.
"""

import random
import hashlib
from typing import List, Dict, Optional


# Brainfuck instruction set (ASCII values)
VALID_INSTRUCTIONS = {
    60,   # <  move data pointer left
    62,   # >  move data pointer right
    43,   # +  increment byte at data pointer
    45,   # -  decrement byte at data pointer
    44,   # ,  copy/input
    91,   # [  begin loop
    93,   # ]  end loop
}


class Tape:
    """
    Represents a single tape in the BFF soup.

    A tape is a fixed-length sequence of bytes (0-255) that can contain
    both Brainfuck instructions and data. Tapes interact in pairs and
    can modify themselves and each other.

    Attributes:
        length: Number of bytes in the tape
        data: List of bytes (integers 0-255)
    """

    def __init__(
        self,
        length: int,
        data: Optional[List[int]] = None,
        seed: Optional[int] = None
    ):
        """
        Initialize a tape.

        Args:
            length: Number of bytes in the tape
            data: Optional explicit byte data. If None, initializes randomly.
            seed: Optional random seed for reproducibility
        """
        self.length = length

        if data is not None:
            # Copy data to avoid mutation of external list
            self.data = data.copy()
            if len(self.data) != length:
                raise ValueError(f"Data length {len(data)} != tape length {length}")
        else:
            # Initialize with random bytes
            if seed is not None:
                rng = random.Random(seed)
                self.data = [rng.randint(0, 255) for _ in range(length)]
            else:
                self.data = [random.randint(0, 255) for _ in range(length)]

    def get_byte(self, position: int) -> int:
        """
        Get byte value at position.

        Args:
            position: Index in tape (0 to length-1)

        Returns:
            Byte value (0-255)
        """
        return self.data[position]

    def set_byte(self, position: int, value: int) -> None:
        """
        Set byte value at position.

        Args:
            position: Index in tape (0 to length-1)
            value: Byte value (0-255), will be clamped
        """
        self.data[position] = max(0, min(255, value))

    def increment_byte(self, position: int) -> None:
        """
        Increment byte at position with wrapping.

        Incrementing 255 wraps to 0.

        Args:
            position: Index in tape (0 to length-1)
        """
        self.data[position] = (self.data[position] + 1) % 256

    def decrement_byte(self, position: int) -> None:
        """
        Decrement byte at position with wrapping.

        Decrementing 0 wraps to 255.

        Args:
            position: Index in tape (0 to length-1)
        """
        self.data[position] = (self.data[position] - 1) % 256

    def hash(self) -> str:
        """
        Compute hash of tape data for replication detection.

        Returns:
            Hex string hash of tape data
        """
        # Use SHA-256 for consistent hashing
        data_bytes = bytes(self.data)
        return hashlib.sha256(data_bytes).hexdigest()

    def clone(self) -> 'Tape':
        """
        Create independent copy of this tape.

        Returns:
            New Tape with same data
        """
        return Tape(length=self.length, data=self.data.copy())

    def to_dict(self) -> Dict:
        """
        Serialize tape to dictionary.

        Returns:
            Dictionary with 'length' and 'data' keys
        """
        return {
            'length': self.length,
            'data': self.data.copy()
        }

    @classmethod
    def from_dict(cls, tape_dict: Dict) -> 'Tape':
        """
        Deserialize tape from dictionary.

        Args:
            tape_dict: Dictionary with 'length' and 'data' keys

        Returns:
            Reconstructed Tape
        """
        return cls(
            length=tape_dict['length'],
            data=tape_dict['data']
        )

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another tape.

        Args:
            other: Another object to compare

        Returns:
            True if other is a Tape with same length and data
        """
        if not isinstance(other, Tape):
            return False
        return self.length == other.length and self.data == other.data

    def __ne__(self, other: object) -> bool:
        """Check inequality."""
        return not self.__eq__(other)

    def count_instructions(self) -> int:
        """
        Count number of valid Brainfuck instructions in tape.

        Valid instructions are: < > + - , [ ]
        All other bytes are no-ops.

        Returns:
            Number of valid instruction bytes
        """
        return sum(1 for byte in self.data if byte in VALID_INSTRUCTIONS)

    def __repr__(self) -> str:
        """String representation for debugging."""
        preview = self.data[:8] if len(self.data) > 8 else self.data
        preview_str = ', '.join(str(b) for b in preview)
        suffix = '...' if len(self.data) > 8 else ''
        return f"Tape(length={self.length}, data=[{preview_str}{suffix}])"
