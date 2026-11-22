from trial import (
    cluster_design_effect,
    estimate_difference_in_means,
    mde_two_sided_80_power,
    random_assignment,
    randomization_test,
    simulate_outcomes,
)


def main():
    n = 1000
    assignment = random_assignment(n, 500, seed=2026)
    x = [((i % 101) - 50) / 25 for i in range(n)]
    outcomes = simulate_outcomes(
        x, assignment, effect=0.07, heterogeneity=0.02, noise_sd=0.49, seed=2027
    )
    estimate = estimate_difference_in_means(outcomes, assignment)
    inference = randomization_test(outcomes, assignment, permutations=1999, seed=2028)
    mde = mde_two_sided_80_power(0.4876, 500, 500)
    design_effect = cluster_design_effect(20, 0.05)
    print("Synthetic randomized experiment; no real utility data.")
    print(f"ITT estimate: {estimate['estimate']:.4f}")
    print(f"Neyman standard error: {estimate['standard_error']:.4f}")
    print(f"Randomization-inference p-value: {inference['p_value']:.4f}")
    print(f"Approximate 80%-power MDE: {mde:.4f}")
    print(f"Cluster design effect (m=20, ICC=.05): {design_effect:.2f}")


if __name__ == "__main__":
    main()
