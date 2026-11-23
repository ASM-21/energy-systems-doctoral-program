# Y1-04 Problem Set 2 — Multiple Regression, Functional Form, and Diagnostics

**Level:** Graduate methods foundation  
**Suggested effort:** 3 hours  
**Prerequisites:** Y1-04 Problem Set 1; introductory probability, OLS, and statistical inference.

This assignment develops regression specification and interpretation. It does not require causal estimation. The goal is to identify what the model estimates, assess its assumptions, and communicate uncertainty without overclaiming.

## Problem 1 — Multiple regression and units

An analyst estimates annual household electricity consumption using floor area and household size:

`consumption_i = β_0 + β_1 area_i + β_2 household_size_i + u_i`

Consumption is measured in kWh/year, area in square feet, and household size in persons.

1. Interpret the units of β1 and β2.
2. Explain the difference between the bivariate regression of consumption on area and the multiple regression above.
3. Give an example of how omitting household size could affect the estimated area coefficient.
4. Explain why a coefficient is a conditional association and not automatically a causal effect.

## Problem 2 — Functional form and interactions

A model relates monthly electricity use to average monthly temperature:

`use_i = β_0 + β_1 temperature_i + u_i`

1. Explain why a linear temperature relationship may be inadequate across cold, mild, and hot conditions.
2. Propose a quadratic specification and explain how to interpret its marginal effect.
3. Propose a heating/cooling degree-day specification. Define the base temperature and explain why the choice matters.
4. Add an interaction between temperature and building floor area. Interpret the interaction coefficient.
5. Describe a plot or residual diagnostic that could reveal functional-form misspecification.

## Problem 3 — Heteroskedasticity and inference

Suppose residual dispersion increases with household income.

1. Define heteroskedasticity and distinguish it from omitted-variable bias.
2. Under the usual exogeneity condition, explain what heteroskedasticity does and does not imply for OLS coefficient estimates.
3. Explain why heteroskedasticity-consistent standard errors may be appropriate.
4. Explain why robust standard errors do not fix omitted variables, reverse causality, selection, or measurement error.
5. Identify one reason robust standard errors can still perform poorly in a small sample.

## Problem 4 — Model comparison and prediction

Two models predict monthly electricity consumption. Model A uses temperature only. Model B adds floor area, household size, and month fixed effects.

1. Explain why a higher in-sample R-squared does not by itself establish that Model B is better.
2. Describe a train/test split that respects time ordering if the goal is forecasting.
3. Explain how RMSE and MAE differ and why both may be useful.
4. State why prediction performance does not establish causal identification.
5. Describe one way to test whether model performance is sensitive to the sample period.

## Problem 5 — Interpretation and communication

You are given an OLS table with a statistically significant positive coefficient on floor area and a negative coefficient on average temperature. Write a short interpretation that:
- reports units and conditional meaning;
- distinguishes statistical from practical significance;
- notes uncertainty and model specification;
- avoids claiming that changing floor area or temperature would cause the estimated change;
- identifies at least two plausible omitted factors.

## Submission

Submit the written answers, equations, and a one-page model-diagnostics note. Where you use data, document the source, units, exclusions, and software. A correct answer explains the reasoning and the limits of the model, not only the sign of a coefficient.
