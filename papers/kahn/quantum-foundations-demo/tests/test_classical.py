"""Tests for classical probability utilities."""

import numpy as np
import pytest

from quantum_demo.classical import (
    apply_stochastic_matrix,
    indicator_distribution,
    normalize_probabilities,
    sample_classical,
)


# ── normalize_probabilities ──────────────────────────────────────────

class TestNormalizeProbabilities:
    def test_already_normalized(self):
        p = np.array([0.25, 0.25, 0.5])
        result = normalize_probabilities(p)
        np.testing.assert_allclose(result, p)
        assert np.isclose(result.sum(), 1.0)

    def test_unnormalized_vector(self):
        p = np.array([2.0, 3.0, 5.0])
        result = normalize_probabilities(p)
        np.testing.assert_allclose(result, [0.2, 0.3, 0.5])
        assert np.isclose(result.sum(), 1.0)

    def test_single_element(self):
        p = np.array([7.0])
        result = normalize_probabilities(p)
        np.testing.assert_allclose(result, [1.0])

    def test_zeros_raises(self):
        p = np.array([0.0, 0.0, 0.0])
        with pytest.raises(ValueError):
            normalize_probabilities(p)

    def test_output_is_nonnegative(self):
        p = np.array([1.0, 0.0, 3.0, 0.0])
        result = normalize_probabilities(p)
        assert np.all(result >= 0)
        assert np.isclose(result.sum(), 1.0)


# ── sample_classical ─────────────────────────────────────────────────

class TestSampleClassical:
    def test_deterministic_distribution(self):
        """A distribution with all weight on one index should always return that index."""
        p = np.array([0.0, 0.0, 1.0])
        for _ in range(20):
            assert sample_classical(p) == 2

    def test_seeded_rng_reproducibility(self):
        """Two generators seeded identically must produce the same sample."""
        p = np.array([0.1, 0.2, 0.3, 0.4])
        rng1 = np.random.default_rng(42)
        rng2 = np.random.default_rng(42)
        assert sample_classical(p, rng=rng1) == sample_classical(p, rng=rng2)

    def test_returns_valid_index(self):
        p = np.array([0.25, 0.25, 0.25, 0.25])
        rng = np.random.default_rng(0)
        for _ in range(50):
            idx = sample_classical(p, rng=rng)
            assert 0 <= idx < len(p)

    def test_return_type_is_int(self):
        p = np.array([0.5, 0.5])
        result = sample_classical(p, rng=np.random.default_rng(99))
        assert isinstance(result, (int, np.integer))

    def test_statistical_distribution(self):
        """Over many samples the frequencies should roughly match the distribution."""
        p = np.array([0.7, 0.2, 0.1])
        rng = np.random.default_rng(12345)
        counts = np.zeros(3)
        n = 10_000
        for _ in range(n):
            counts[sample_classical(p, rng=rng)] += 1
        freq = counts / n
        np.testing.assert_allclose(freq, p, atol=0.03)


# ── apply_stochastic_matrix ──────────────────────────────────────────

class TestApplyStochasticMatrix:
    def test_identity_matrix(self):
        p = np.array([0.3, 0.7])
        T = np.eye(2)
        result = apply_stochastic_matrix(p, T)
        np.testing.assert_allclose(result, p)

    def test_swap_matrix(self):
        p = np.array([1.0, 0.0])
        T = np.array([[0.0, 1.0],
                       [1.0, 0.0]])
        result = apply_stochastic_matrix(p, T)
        np.testing.assert_allclose(result, [0.0, 1.0])

    def test_output_is_probability_distribution(self):
        p = np.array([0.5, 0.3, 0.2])
        T = np.array([[0.1, 0.6, 0.3],
                       [0.4, 0.2, 0.4],
                       [0.5, 0.2, 0.3]])
        result = apply_stochastic_matrix(p, T)
        assert np.all(result >= 0)
        assert np.isclose(result.sum(), 1.0)

    def test_known_transition(self):
        """Manually compute T @ p and compare."""
        p = np.array([1.0, 0.0, 0.0])
        T = np.array([[0.2, 0.3, 0.5],
                       [0.4, 0.4, 0.2],
                       [0.4, 0.3, 0.3]])
        result = apply_stochastic_matrix(p, T)
        expected = T @ p  # first column of T
        np.testing.assert_allclose(result, expected)


# ── indicator_distribution ───────────────────────────────────────────

class TestIndicatorDistribution:
    def test_basic(self):
        d = indicator_distribution(0, 3)
        np.testing.assert_allclose(d, [1.0, 0.0, 0.0])

    def test_middle_index(self):
        d = indicator_distribution(2, 5)
        expected = np.array([0.0, 0.0, 1.0, 0.0, 0.0])
        np.testing.assert_allclose(d, expected)

    def test_last_index(self):
        d = indicator_distribution(3, 4)
        np.testing.assert_allclose(d, [0.0, 0.0, 0.0, 1.0])

    def test_sums_to_one(self):
        for dim in range(1, 6):
            for idx in range(dim):
                d = indicator_distribution(idx, dim)
                assert np.isclose(d.sum(), 1.0)

    def test_shape(self):
        d = indicator_distribution(1, 4)
        assert d.shape == (4,)

    def test_invalid_index_raises(self):
        with pytest.raises((IndexError, ValueError)):
            indicator_distribution(5, 3)

    def test_negative_index_raises(self):
        with pytest.raises((IndexError, ValueError)):
            indicator_distribution(-1, 3)
