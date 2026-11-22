import unittest

from trial import (
    cluster_design_effect,
    estimate_difference_in_means,
    mde_two_sided_80_power,
    random_assignment,
    randomization_test,
    simulate_outcomes,
)


class RandomizedExperimentTests(unittest.TestCase):
    def test_complete_randomization_is_fixed_size_and_reproducible(self):
        a = random_assignment(100, 40, seed=8)
        b = random_assignment(100, 40, seed=8)
        self.assertEqual(a, b)
        self.assertEqual(sum(a), 40)

    def test_difference_in_means_and_neyman_standard_error(self):
        outcomes = [1, 0, 1, 1, 0, 0, 1, 0]
        assignment = [1, 1, 1, 1, 0, 0, 0, 0]
        result = estimate_difference_in_means(outcomes, assignment)
        self.assertAlmostEqual(result["estimate"], 0.5)
        self.assertEqual(result["n_treated"], 4)
        self.assertEqual(result["n_control"], 4)
        self.assertGreater(result["standard_error"], 0)

    def test_randomization_test_is_reproducible_and_bounded(self):
        outcomes = [1, 0, 1, 1, 0, 0, 1, 0]
        assignment = [1, 1, 1, 1, 0, 0, 0, 0]
        a = randomization_test(outcomes, assignment, permutations=999, seed=3)
        b = randomization_test(outcomes, assignment, permutations=999, seed=3)
        self.assertEqual(a, b)
        self.assertGreaterEqual(a["p_value"], 1 / 1000)
        self.assertLessEqual(a["p_value"], 1.0)

    def test_mde_and_cluster_design_effect(self):
        mde = mde_two_sided_80_power(0.4876, 500, 500)
        self.assertAlmostEqual(mde, 0.0864, places=3)
        self.assertAlmostEqual(cluster_design_effect(20, 0.05), 1.95)

    def test_simulated_outcomes_reproducible(self):
        x = [-1, -0.5, 0, 0.5, 1]
        assignment = [1, 0, 1, 0, 1]
        a = simulate_outcomes(x, assignment, 0.2, heterogeneity=0.1, seed=5)
        b = simulate_outcomes(x, assignment, 0.2, heterogeneity=0.1, seed=5)
        self.assertEqual(a, b)

    def test_invalid_inputs_fail(self):
        with self.assertRaises(ValueError):
            random_assignment(10, 10)
        with self.assertRaises(ValueError):
            estimate_difference_in_means([1, 2], [1, 1])
        with self.assertRaises(ValueError):
            randomization_test([1, 2], [1, 0], permutations=0)
        with self.assertRaises(ValueError):
            mde_two_sided_80_power(0, 10, 10)
        with self.assertRaises(ValueError):
            cluster_design_effect(20, 1.1)


if __name__ == "__main__":
    unittest.main()
