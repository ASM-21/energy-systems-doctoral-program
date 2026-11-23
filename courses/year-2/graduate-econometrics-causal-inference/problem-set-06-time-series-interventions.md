# Problem Set 6: Time-Series Interventions, Dynamic Models, and Forecasting

**Level:** Advanced graduate / doctoral preparation  
**Suggested effort:** 4–5 hours  
**Prerequisites:** OLS, probability, panel data, synthetic control, matrix algebra  
**Application:** Evaluating utility policy or infrastructure interventions using monthly or quarterly outcomes

## Problem 1. Segmented regression and estimands

Consider
\[
Y_t=\beta_0+\beta_1t+\beta_2D_t+\beta_3(t-T_0)D_t+u_t,
\]
where \(D_t=1(t\geq T_0)\).

1. Interpret each coefficient.
2. Derive the intervention-associated level change at \(T_0\) and the change in slope.
3. Derive the post-intervention difference from the no-intervention extrapolation at horizon \(h\).
4. Explain why this contrast is causal only under a stable counterfactual trend and absence of coincident shocks.
5. Explain why an intervention that changes the slope but not the level can have a zero immediate effect but a growing long-run gap.

## Problem 2. Autocorrelation and inference

Suppose regression errors follow \(u_t=\rho u_{t-1}+\epsilon_t\), with \(|\rho|<1\).

1. Explain why conventional OLS standard errors can be misleading even if OLS coefficients remain unbiased under strict exogeneity.
2. Explain the purpose of Newey–West heteroskedasticity-and-autocorrelation-consistent covariance estimation.
3. Why does HAC estimation not repair omitted variables, a wrong intervention date, or an invalid counterfactual?
4. Discuss bandwidth selection and the bias-variance trade-off.
5. Explain why a long monthly time series does not automatically justify a high-dimensional model with many break dates.

## Problem 3. Stationarity, unit roots, and spurious regression

Let \(x_t=x_{t-1}+\epsilon_t\) and \(y_t=y_{t-1}+\eta_t\), where the innovations are independent white noise.

1. Explain why regressing \(y_t\) on \(x_t\) in levels can produce misleading fit and conventional test statistics.
2. Define covariance stationarity.
3. State the null and alternative hypotheses of an augmented Dickey–Fuller test.
4. Explain why failure to reject a unit-root null is not proof that a series has a unit root.
5. Explain why differencing changes the estimand from a level relationship to a change relationship.

## Problem 4. Cointegration and error correction

Suppose \(y_t\) and \(x_t\) are each I(1), but \(z_t=y_t-\theta x_t\) is I(0).

1. Define cointegration and interpret \(\theta\).
2. Write an error-correction model:
\[
\Delta y_t=\alpha+\lambda(y_{t-1}-\theta x_{t-1})+
\sum_i\phi_i\Delta y_{t-i}+\sum_j\gamma_j\Delta x_{t-j}+e_t.
\]
3. Interpret the sign of \(\lambda\) when deviations from the long-run relation are corrected.
4. Explain why cointegration is not a causal identification strategy.
5. Discuss structural breaks and why a pre-break cointegrating relation may not persist after market redesign or major infrastructure change.

## Problem 5. Forecasting and evaluation

A utility analyst compares a seasonal-naive forecast, ARIMA, and a regression with weather and calendar variables.

1. Explain rolling-origin evaluation and why random train/test splitting is generally inappropriate for time series.
2. Define MAE, RMSE, and MASE. State when RMSE is more sensitive than MAE.
3. Explain forecast leakage from revised data, future weather observations, or policy variables not known at forecast time.
4. Distinguish prediction intervals from confidence intervals for mean outcomes.
5. Explain why lower forecast error does not establish a causal policy effect.

## Problem 6. Structural breaks and specification search

1. Distinguish a known-date intervention test from an unknown-break search.
2. Explain the multiple-testing problem when searching many candidate dates.
3. Describe a Chow test's assumptions and limitations.
4. Explain why CUSUM or sup-Wald tests can be useful but do not identify the economic cause of a break.
5. Propose a transparent protocol for pre-specifying a policy intervention date and separately reporting exploratory break detection.

## Problem 7. Applied energy-policy design

Write a 700–900 word empirical design for one monthly or quarterly outcome, such as interconnection applications, queue duration, distribution investment, load, wholesale price, or renewable deployment. Specify:

- outcome definition, unit, frequency, data vintage, and measurement changes;
- intervention date and institutional rationale;
- pre/post window and minimum observations;
- segmented-regression estimand and counterfactual trend;
- seasonality, weather, economic controls, and concurrent policies;
- autocorrelation diagnostics and HAC specification;
- stationarity and structural-break diagnostics where relevant;
- placebo dates, alternative windows, and outcome falsification tests;
- missingness, revisions, and forecast-vs-causal distinction.

Do not claim that HAC standard errors or a significant break make the intervention causal. If a concurrent event plausibly explains the outcome change, report the design as associational or not identified.

## Submission standard

Provide the time plot, intervention date rationale, model equation, coefficient interpretation in original units, residual diagnostics, covariance estimator and bandwidth, sensitivity analyses, and a limitations statement. Include the data extraction script and an immutable source snapshot or documented retrieval date.
