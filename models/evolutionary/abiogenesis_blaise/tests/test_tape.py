"""
Tests for the Tape data structure.

Following TDD: these tests are written FIRST, then core/tape.py will be implemented
to pass these tests.
"""

import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from core.tape import Tape


class TestTapeInitialization:
    """Test tape creation and initialization."""

    def test_default_random_initialization(self):
        """Tape should initialize with random bytes if no data provided."""
        tape = Tape(length=64)
        assert len(tape.data) == 64
        assert all(0 <= byte <= 255 for byte in tape.data)
        assert isinstance(tape.data, list)

    def test_explicit_data_initialization(self):
        """Tape should accept explicit byte data."""
        data = [1, 2, 3, 4, 5] + [0] * 59
        tape = Tape(length=64, data=data)
        assert len(tape.data) == 64
        assert tape.data[:5] == [1, 2, 3, 4, 5]
        assert tape.data[5:] == [0] * 59

    def test_length_property(self):
        """Tape should expose its length."""
        tape = Tape(length=128)
        assert tape.length == 128
        assert len(tape.data) == 128

    def test_data_immutability_on_init(self):
        """Tape should copy input data, not reference it."""
        original_data = [1, 2, 3] + [0] * 61
        tape = Tape(length=64, data=original_data)
        original_data[0] = 99
        assert tape.data[0] == 1  # Tape data unchanged


class TestTapeByteOperations:
    """Test individual byte manipulation."""

    def test_get_byte(self):
        """Should retrieve byte at given position."""
        tape = Tape(length=64, data=[0] * 64)
        tape.data[10] = 42
        assert tape.get_byte(10) == 42

    def test_set_byte(self):
        """Should set byte at given position."""
        tape = Tape(length=64, data=[0] * 64)
        tape.set_byte(10, 42)
        assert tape.data[10] == 42

    def test_increment_byte(self):
        """Should increment byte with wrapping at 256."""
        tape = Tape(length=64, data=[0] * 64)
        tape.set_byte(0, 100)
        tape.increment_byte(0)
        assert tape.get_byte(0) == 101

    def test_increment_byte_wrapping(self):
        """Incrementing 255 should wrap to 0."""
        tape = Tape(length=64, data=[0] * 64)
        tape.set_byte(0, 255)
        tape.increment_byte(0)
        assert tape.get_byte(0) == 0

    def test_decrement_byte(self):
        """Should decrement byte with wrapping at 0."""
        tape = Tape(length=64, data=[0] * 64)
        tape.set_byte(0, 100)
        tape.decrement_byte(0)
        assert tape.get_byte(0) == 99

    def test_decrement_byte_wrapping(self):
        """Decrementing 0 should wrap to 255."""
        tape = Tape(length=64, data=[0] * 64)
        tape.set_byte(0, 0)
        tape.decrement_byte(0)
        assert tape.get_byte(0) == 255


class TestTapeHashing:
    """Test hashing for replication detection."""

    def test_hash_consistency(self):
        """Same tape should produce same hash."""
        data = [1, 2, 3] + [0] * 61
        tape1 = Tape(length=64, data=data)
        tape2 = Tape(length=64, data=data)
        assert tape1.hash() == tape2.hash()

    def test_hash_difference(self):
        """Different tapes should produce different hashes (with high probability)."""
        tape1 = Tape(length=64, data=[1] * 64)
        tape2 = Tape(length=64, data=[2] * 64)
        assert tape1.hash() != tape2.hash()

    def test_hash_after_modification(self):
        """Hash should change after tape modification."""
        tape = Tape(length=64, data=[0] * 64)
        hash1 = tape.hash()
        tape.set_byte(0, 42)
        hash2 = tape.hash()
        assert hash1 != hash2


class TestTapeCopyAndClone:
    """Test tape copying operations."""

    def test_clone(self):
        """Should create independent copy of tape."""
        original = Tape(length=64, data=[1, 2, 3] + [0] * 61)
        clone = original.clone()

        assert clone.data == original.data
        assert clone.data is not original.data  # Different object

        # Modify clone
        clone.set_byte(0, 99)
        assert original.get_byte(0) == 1  # Original unchanged
        assert clone.get_byte(0) == 99


class TestTapeSerialization:
    """Test serialization for saving/loading."""

    def test_to_dict(self):
        """Should serialize to dictionary."""
        tape = Tape(length=64, data=[1, 2, 3] + [0] * 61)
        tape_dict = tape.to_dict()

        assert tape_dict['length'] == 64
        assert tape_dict['data'] == [1, 2, 3] + [0] * 61

    def test_from_dict(self):
        """Should deserialize from dictionary."""
        tape_dict = {
            'length': 64,
            'data': [1, 2, 3] + [0] * 61
        }
        tape = Tape.from_dict(tape_dict)

        assert tape.length == 64
        assert tape.data == [1, 2, 3] + [0] * 61

    def test_round_trip_serialization(self):
        """Serialize then deserialize should preserve tape."""
        original = Tape(length=64, data=[1, 2, 3] + [0] * 61)
        tape_dict = original.to_dict()
        restored = Tape.from_dict(tape_dict)

        assert restored.data == original.data
        assert restored.length == original.length


class TestTapeEquality:
    """Test equality comparisons."""

    def test_equality_same_data(self):
        """Tapes with same data should be equal."""
        data = [1, 2, 3] + [0] * 61
        tape1 = Tape(length=64, data=data)
        tape2 = Tape(length=64, data=data)
        assert tape1 == tape2

    def test_inequality_different_data(self):
        """Tapes with different data should not be equal."""
        tape1 = Tape(length=64, data=[1] * 64)
        tape2 = Tape(length=64, data=[2] * 64)
        assert tape1 != tape2

    def test_inequality_different_length(self):
        """Tapes with different lengths should not be equal."""
        tape1 = Tape(length=32, data=[0] * 32)
        tape2 = Tape(length=64, data=[0] * 64)
        assert tape1 != tape2


class TestTapeRandomness:
    """Test random initialization properties."""

    def test_random_seed_reproducibility(self):
        """Same seed should produce same random tape."""
        tape1 = Tape(length=64, seed=42)
        tape2 = Tape(length=64, seed=42)
        assert tape1.data == tape2.data

    def test_different_seeds_produce_different_tapes(self):
        """Different seeds should produce different tapes (with high probability)."""
        tape1 = Tape(length=64, seed=42)
        tape2 = Tape(length=64, seed=43)
        assert tape1.data != tape2.data


class TestTapeStatistics:
    """Test statistical properties."""

    def test_count_instructions(self):
        """Should count valid Brainfuck instructions (assuming 7 valid ops out of 256 values)."""
        # For Brainfuck: <, >, +, -, ,, [, ] are typically 60, 62, 43, 45, 44, 91, 93
        data = [60, 62, 43, 45, 44, 91, 93] + [0] * 57
        tape = Tape(length=64, data=data)

        # Count should identify these as valid instructions
        instruction_count = tape.count_instructions()
        assert instruction_count == 7

    def test_count_instructions_with_noise(self):
        """Should count only valid instructions, ignoring noise."""
        # Mix of valid and invalid bytes
        data = [60, 1, 62, 2, 43, 3, 45] + [0] * 57
        tape = Tape(length=64, data=data)

        instruction_count = tape.count_instructions()
        assert instruction_count == 4  # Only 60, 62, 43, 45 are valid
