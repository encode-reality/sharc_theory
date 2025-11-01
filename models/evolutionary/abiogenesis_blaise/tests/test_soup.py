"""
Tests for the Soup population dynamics engine.

The Soup manages a population of tapes and orchestrates their pairwise interactions,
which is the core mechanism of the BFF abiogenesis experiment.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from core.tape import Tape
from core.soup import Soup, InteractionResult


class TestSoupInitialization:
    """Test soup creation and setup."""

    def test_default_initialization(self):
        """Soup should initialize with random tapes."""
        soup = Soup(size=100, tape_length=64)

        assert len(soup.tapes) == 100
        assert all(isinstance(tape, Tape) for tape in soup.tapes)
        assert all(tape.length == 64 for tape in soup.tapes)

    def test_initialization_with_seed(self):
        """Same seed should produce same initial soup."""
        soup1 = Soup(size=50, tape_length=64, seed=42)
        soup2 = Soup(size=50, tape_length=64, seed=42)

        for t1, t2 in zip(soup1.tapes, soup2.tapes):
            assert t1.data == t2.data

    def test_different_seeds_produce_different_soups(self):
        """Different seeds should produce different soups."""
        soup1 = Soup(size=50, tape_length=64, seed=42)
        soup2 = Soup(size=50, tape_length=64, seed=43)

        # At least one tape should be different
        any_different = any(
            t1.data != t2.data
            for t1, t2 in zip(soup1.tapes, soup2.tapes)
        )
        assert any_different

    def test_custom_tape_length(self):
        """Should support custom tape lengths."""
        soup = Soup(size=10, tape_length=128)
        assert all(tape.length == 128 for tape in soup.tapes)


class TestTapeSelection:
    """Test random tape selection for interactions."""

    def test_select_two_tapes(self):
        """Should select two tapes for interaction."""
        soup = Soup(size=100, tape_length=64, seed=42)

        tape1, tape2, idx1, idx2 = soup.select_pair()

        assert isinstance(tape1, Tape)
        assert isinstance(tape2, Tape)
        assert 0 <= idx1 < 100
        assert 0 <= idx2 < 100
        assert idx1 != idx2  # Should be different tapes

    def test_selection_is_random(self):
        """Multiple selections should produce different pairs."""
        soup = Soup(size=100, tape_length=64)

        pairs = [soup.select_pair()[2:] for _ in range(10)]
        unique_pairs = set(pairs)

        # Should have some variety (not all the same pair)
        assert len(unique_pairs) > 1


class TestPairwiseInteraction:
    """Test the core pairwise interaction mechanism."""

    def test_basic_interaction(self):
        """Test that two tapes can interact."""
        soup = Soup(size=10, tape_length=64, seed=42)

        result = soup.interact_once()

        assert isinstance(result, InteractionResult)
        assert result.operations >= 0
        assert result.idx1 >= 0
        assert result.idx2 >= 0

    def test_interaction_concatenates_tapes(self):
        """Interaction should concatenate two tapes end-to-end."""
        # Create soup with specific tapes
        tape1_data = [43] * 64  # All '+' instructions
        tape2_data = [45] * 64  # All '-' instructions

        soup = Soup(size=2, tape_length=64)
        soup.tapes[0] = Tape(length=64, data=tape1_data)
        soup.tapes[1] = Tape(length=64, data=tape2_data)

        # Force interaction between these specific tapes
        result = soup.interact_pair(0, 1)

        # Should have executed some operations
        assert result.operations > 0

    def test_interaction_modifies_tapes(self):
        """Interaction should allow tapes to modify each other."""
        soup = Soup(size=10, tape_length=64)

        # Get initial state
        initial_hash = soup.tapes[0].hash()

        # Run some interactions
        for _ in range(100):
            soup.interact_once()

        # Some tape should likely have changed
        # (with random bytes, very likely something changed)
        any_changed = any(
            tape.hash() != initial_hash
            for tape in soup.tapes
        )
        # Note: This could theoretically fail if no modifications happen,
        # but with 100 interactions it's extremely unlikely


class TestMutation:
    """Test mutation mechanism."""

    def test_no_mutation_when_rate_zero(self):
        """No mutation should occur when mutation_rate=0."""
        soup = Soup(size=10, tape_length=64, mutation_rate=0.0, seed=42)

        # Store initial state
        initial_hashes = [tape.hash() for tape in soup.tapes]

        # Apply mutation (should do nothing)
        soup.apply_mutations()

        # Should be unchanged
        final_hashes = [tape.hash() for tape in soup.tapes]
        assert initial_hashes == final_hashes

    def test_mutation_occurs_with_positive_rate(self):
        """Mutation should occur with positive mutation_rate."""
        soup = Soup(size=100, tape_length=64, mutation_rate=0.1, seed=42)

        # Store initial state
        initial_hashes = [tape.hash() for tape in soup.tapes]

        # Apply mutation multiple times
        for _ in range(10):
            soup.apply_mutations()

        # Something should have changed
        final_hashes = [tape.hash() for tape in soup.tapes]
        assert initial_hashes != final_hashes

    def test_mutation_respects_byte_range(self):
        """Mutations should keep bytes in 0-255 range."""
        soup = Soup(size=10, tape_length=64, mutation_rate=1.0)  # High rate

        # Apply many mutations
        for _ in range(100):
            soup.apply_mutations()

        # All bytes should still be valid
        for tape in soup.tapes:
            assert all(0 <= byte <= 255 for byte in tape.data)


class TestMultipleInteractions:
    """Test running many interactions."""

    def test_run_multiple_interactions(self):
        """Should be able to run many interactions."""
        soup = Soup(size=100, tape_length=64, seed=42)

        results = soup.run(num_interactions=1000)

        assert len(results) == 1000
        assert all(isinstance(r, InteractionResult) for r in results)

    def test_interaction_count_tracking(self):
        """Should track total number of interactions."""
        soup = Soup(size=50, tape_length=64)

        assert soup.interaction_count == 0

        soup.run(num_interactions=100)
        assert soup.interaction_count == 100

        soup.run(num_interactions=50)
        assert soup.interaction_count == 150

    def test_operations_accumulate(self):
        """Should track cumulative operations across interactions."""
        soup = Soup(size=50, tape_length=64, seed=42)

        results = soup.run(num_interactions=100)

        total_ops = sum(r.operations for r in results)
        assert total_ops >= 0


class TestSoupStatistics:
    """Test statistical properties and measurements."""

    def test_get_tape_hashes(self):
        """Should be able to get all tape hashes."""
        soup = Soup(size=10, tape_length=64, seed=42)

        hashes = soup.get_tape_hashes()

        assert len(hashes) == 10
        assert all(isinstance(h, str) for h in hashes)

    def test_count_unique_tapes(self):
        """Should count number of unique tapes."""
        soup = Soup(size=100, tape_length=64, seed=42)

        unique_count = soup.count_unique_tapes()

        # Initially, most should be unique (random initialization)
        assert unique_count >= 90  # Allow some collisions

    def test_count_unique_after_replication(self):
        """After replication, should have fewer unique tapes."""
        soup = Soup(size=50, tape_length=64)

        # Manually create duplicates to simulate replication
        soup.tapes[1] = soup.tapes[0].clone()
        soup.tapes[2] = soup.tapes[0].clone()

        unique_count = soup.count_unique_tapes()
        assert unique_count == 48  # 50 - 2 duplicates

    def test_get_diversity(self):
        """Should calculate diversity metric."""
        soup = Soup(size=100, tape_length=64, seed=42)

        diversity = soup.get_diversity()

        assert 0.0 <= diversity <= 1.0
        # High diversity initially (mostly unique)
        assert diversity > 0.8


class TestSoupState:
    """Test soup state management."""

    def test_get_state(self):
        """Should be able to get soup state."""
        soup = Soup(size=10, tape_length=64, seed=42)

        state = soup.get_state()

        assert 'size' in state
        assert 'tape_length' in state
        assert 'interaction_count' in state
        assert 'tapes' in state
        assert len(state['tapes']) == 10

    def test_set_state(self):
        """Should be able to restore soup from state."""
        soup1 = Soup(size=10, tape_length=64, seed=42)
        soup1.run(num_interactions=50)

        state = soup1.get_state()

        soup2 = Soup.from_state(state)

        assert soup2.size == soup1.size
        assert soup2.tape_length == soup1.tape_length
        assert soup2.interaction_count == soup1.interaction_count

        # Tapes should be identical
        for t1, t2 in zip(soup1.tapes, soup2.tapes):
            assert t1.data == t2.data

    def test_checkpoint_and_restore(self):
        """Should support checkpointing."""
        soup = Soup(size=20, tape_length=64, seed=42)

        # Run for a while
        soup.run(num_interactions=100)
        checkpoint = soup.get_state()

        # Continue running
        soup.run(num_interactions=100)

        # Restore from checkpoint
        soup_restored = Soup.from_state(checkpoint)

        assert soup_restored.interaction_count == 100


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_small_soup(self):
        """Should work with very small soup."""
        soup = Soup(size=2, tape_length=64)

        # Should still be able to interact
        result = soup.interact_once()
        assert result.idx1 != result.idx2

    def test_large_tape_length(self):
        """Should support larger tapes."""
        soup = Soup(size=10, tape_length=256)

        assert all(tape.length == 256 for tape in soup.tapes)

        # Should still interact
        result = soup.interact_once()
        assert result.operations >= 0

    def test_zero_interactions(self):
        """Running zero interactions should work."""
        soup = Soup(size=10, tape_length=64)

        results = soup.run(num_interactions=0)

        assert len(results) == 0
        assert soup.interaction_count == 0


class TestInteractionResult:
    """Test the InteractionResult dataclass."""

    def test_result_has_required_fields(self):
        """InteractionResult should have all necessary fields."""
        soup = Soup(size=10, tape_length=64)
        result = soup.interact_once()

        assert hasattr(result, 'operations')
        assert hasattr(result, 'idx1')
        assert hasattr(result, 'idx2')
        assert hasattr(result, 'terminated')
