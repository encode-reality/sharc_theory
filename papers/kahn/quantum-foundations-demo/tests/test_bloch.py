"""Tests for Bloch sphere coordinate mapping."""

import numpy as np
import pytest
from quantum_demo.bloch import bloch_coordinates


class TestBlochCoordinates:
    """Test bloch_coordinates with known qubit states."""

    def test_zero_state(self):
        """|0> should map to north pole (0, 0, 1)."""
        state = np.array([1, 0], dtype=complex)
        x, y, z = bloch_coordinates(state)
        assert x == pytest.approx(0, abs=1e-10)
        assert y == pytest.approx(0, abs=1e-10)
        assert z == pytest.approx(1, abs=1e-10)

    def test_one_state(self):
        """|1> should map to south pole (0, 0, -1)."""
        state = np.array([0, 1], dtype=complex)
        x, y, z = bloch_coordinates(state)
        assert x == pytest.approx(0, abs=1e-10)
        assert y == pytest.approx(0, abs=1e-10)
        assert z == pytest.approx(-1, abs=1e-10)

    def test_plus_state(self):
        """(|0>+|1>)/sqrt(2) should map to (1, 0, 0)."""
        state = np.array([1, 1], dtype=complex) / np.sqrt(2)
        x, y, z = bloch_coordinates(state)
        assert x == pytest.approx(1, abs=1e-10)
        assert y == pytest.approx(0, abs=1e-10)
        assert z == pytest.approx(0, abs=1e-10)

    def test_minus_state(self):
        """(|0>-|1>)/sqrt(2) should map to (-1, 0, 0)."""
        state = np.array([1, -1], dtype=complex) / np.sqrt(2)
        x, y, z = bloch_coordinates(state)
        assert x == pytest.approx(-1, abs=1e-10)
        assert y == pytest.approx(0, abs=1e-10)
        assert z == pytest.approx(0, abs=1e-10)

    def test_plus_i_state(self):
        """(|0>+i|1>)/sqrt(2) should map to (0, 1, 0)."""
        state = np.array([1, 1j], dtype=complex) / np.sqrt(2)
        x, y, z = bloch_coordinates(state)
        assert x == pytest.approx(0, abs=1e-10)
        assert y == pytest.approx(1, abs=1e-10)
        assert z == pytest.approx(0, abs=1e-10)

    def test_coordinates_on_unit_sphere(self):
        """All Bloch coordinates for normalized states should lie on the unit sphere."""
        rng = np.random.default_rng(42)
        for _ in range(50):
            # Generate a random normalized state
            raw = rng.standard_normal(2) + 1j * rng.standard_normal(2)
            state = raw / np.linalg.norm(raw)
            x, y, z = bloch_coordinates(state)
            radius = np.sqrt(x**2 + y**2 + z**2)
            assert radius == pytest.approx(1.0, abs=1e-10)
