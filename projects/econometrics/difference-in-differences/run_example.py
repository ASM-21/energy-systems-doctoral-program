from did import group_time_att, make_synthetic_panel


def main():
    results = group_time_att(make_synthetic_panel(n_per_cohort=20))
    print("Synthetic staggered-adoption panel; known heterogeneous effects.")
    for row in results:
        print(
            f"cohort={row['cohort']} period={row['period']} "
            f"ATT={row['att']:.2f} "
            f"n_treated={row['n_treated']} n_control={row['n_control']}"
        )


if __name__ == "__main__":
    main()
