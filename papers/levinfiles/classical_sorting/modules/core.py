"""
Core data structures for morphogenesis sorting algorithms experiment.

This module defines the fundamental classes and types used throughout
the sorting algorithm experiments.
"""

from dataclasses import dataclass
from typing import Literal, Optional

# Type definitions
Algotype = Literal["bubble", "insertion", "selection"]
FrozenType = Literal["active", "movable", "immovable"]
Direction = Literal["inc", "dec"]


@dataclass
class Cell:
    """
    Represents a single cell in the sorting array.

    In the biological analogy, each cell is like an organ or tissue type
    that needs to find its correct position along the body axis.

    Attributes:
        value: The numerical value (like an identity marker)
        algotype: Which sorting algorithm this cell follows
        frozen_type: Whether the cell can move or be moved
        direction: Whether sorting increasingly or decreasingly
    """
    value: int
    algotype: Algotype
    frozen_type: FrozenType = "active"
    direction: Direction = "inc"

    def can_initiate_move(self) -> bool:
        """
        Check if this cell can initiate a swap.

        Only "active" cells can decide to move on their own.
        Frozen cells cannot initiate movement.
        """
        return self.frozen_type == "active"

    def can_be_moved(self) -> bool:
        """
        Check if this cell can be moved by another cell.

        "active" and "movable" frozen cells can be displaced by others.
        "immovable" frozen cells are completely stuck.
        """
        return self.frozen_type in ("active", "movable")


@dataclass
class StepCounter:
    """
    Tracks computational steps during sorting.

    In biology, this represents metabolic cost:
    - Comparisons = sensing the environment
    - Swaps = active movement
    """
    comparisons: int = 0
    swaps: int = 0

    @property
    def total(self) -> int:
        """Total computational cost."""
        return self.comparisons + self.swaps

    def __repr__(self) -> str:
        return f"StepCounter(comparisons={self.comparisons}, swaps={self.swaps}, total={self.total})"


class Probe:
    """
    Records the state of a sorting experiment over time.

    Like a microscope observing cells during development,
    this captures snapshots of the sorting process.
    """

    def __init__(self):
        self.sortedness_history = []
        self.states = []  # Full array states at key moments
        self.swap_count = 0
        self.comparison_count = 0

    def record_swap(self, array_state, sortedness_value):
        """Record a state after a swap operation."""
        self.swap_count += 1
        self.sortedness_history.append(sortedness_value)
        self.states.append(array_state.copy())

    def record_comparison(self):
        """Record that a comparison was made."""
        self.comparison_count += 1

    def get_final_sortedness(self) -> float:
        """Get the final sortedness value."""
        return self.sortedness_history[-1] if self.sortedness_history else 0.0

    def get_trajectory(self):
        """Get the complete trajectory through sortedness space."""
        return list(enumerate(self.sortedness_history))


# Global configuration
DEFAULT_SEED = 42
N_CELLS = 100
N_REPEATS = 100
MAX_STEPS = 100000


def set_experiment_seed(base_seed: int, experiment_idx: int):
    """
    Set reproducible random seed for an experiment.

    This ensures that each experimental repeat gets a consistent
    but different random initialization.
    """
    import random
    import numpy as np

    seed = base_seed + experiment_idx
    random.seed(seed)
    np.random.seed(seed)
