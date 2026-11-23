# Y1-04 Problem Set 2 — Solution Notes

These notes provide a benchmark for reasoning. Exact specifications may differ if the learner clearly defines the estimand, units, and assumptions.

## Problem 1 — Multiple regression and units

- β1 is the conditional change in predicted annual consumption, measured in kWh/year, associated with one additional square foot, holding household size constant.
- β2 is the conditional change in predicted annual consumption associated with one additional household member, holding floor area constant.
- A bivariate area regression combines the association of area with any correlated factors. The multiple regression conditions on household size, so its coefficient may differ.
- If larger homes tend to have more occupants and household size is positively related to consumption, omitting household size can load part of the household-size association onto area. The direction and magnitude depend on the correlations and the true model.
- Conditional association is not causation. Unobserved income, appliance stock, insulation, climate, occupancy, and selection into housing can affect both regressors and consumption.

## Problem 2 — Functional form and interactions

A linear model assumes a constant marginal association across the observed temperature range. Heating and cooling demand can produce a U-shaped or piecewise relationship.

A quadratic model is:

`use_i = β_0 + β_1 T_i + β_2 T_i^2 + u_i`

The marginal association is `β_1 + 2β_2 T_i`, which varies with temperature. The turning point, when β2 is nonzero, is `-β_1/(2β_2)`; it should be interpreted only if it lies within the observed data range.

A degree-day model can use heating degree days `HDD = max(0, T_base - T)` and cooling degree days `CDD = max(0, T - T_base)`. The base temperature is an assumed balance point and should be justified or tested for sensitivity. A model may include both HDD and CDD.

An interaction model can be written:

`use_i = β_0 + β_1 T_i + β_2 area_i + β_3(T_i × area_i) + u_i`

The marginal temperature association is `β_1 + β_3 area_i`. The interaction coefficient describes how the temperature association changes with floor area, conditional on the model. Centering variables can make main effects easier to interpret.

Residual-versus-fitted plots, residuals against temperature, partial-residual plots, and out-of-sample error patterns can reveal nonlinearity or heterogeneity. No single diagnostic proves a specification is correct.

## Problem 3 — Heteroskedasticity and inference

Heteroskedasticity means the conditional error variance differs across observations. It is distinct from omitted-variable bias, which arises when an excluded determinant of the outcome is correlated with included regressors.

Under exogeneity, heteroskedasticity alone does not generally bias the OLS coefficient estimator, but OLS is no longer efficient among linear unbiased estimators under the usual Gauss-Markov conditions, and conventional homoskedastic standard-error formulas are invalid. Heteroskedasticity-consistent covariance estimators provide inference robust to specified forms of nonconstant variance under appropriate large-sample conditions.

Robust standard errors change the estimated covariance matrix, not the regression's conditional-mean specification. They do not correct endogeneity, selection, measurement error, serial dependence, clustering, or a misspecified functional form. Small-sample behavior can be poor, especially with high leverage or few independent clusters.

## Problem 4 — Model comparison and prediction

R-squared cannot decrease when regressors are added to an OLS model with an intercept on the same sample, even if the added variables are noise. Model selection should consider adjusted fit, theory, diagnostics, parsimony, and out-of-sample performance.

For forecasting, train on earlier periods and evaluate on a later untouched period. Avoid random splitting that leaks future information into training. RMSE penalizes large errors more heavily because errors are squared; MAE is more robust to large outliers and has the same units as the outcome. Compare performance across plausible forecast origins or rolling windows.

Prediction evaluates forecasts, not counterfactual treatment effects. A predictive model can be useful without identifying any causal parameter.

## Problem 5 — Interpretation and communication

A strong response states the outcome and regressor units, describes the coefficient as a conditional association given the included covariates, reports uncertainty and the sample/model context, and distinguishes statistical from practical significance. Plausible omitted variables include income, household size, insulation, appliance stock, occupancy, building age, and local weather patterns. Do not infer an intervention effect from an observational OLS coefficient without a separate identification argument.

## Common errors

- Interpreting β1 without holding the other regressors constant.
- Ignoring units or scaling.
- Treating a significant coefficient as practically large or causal.
- Using R-squared alone to select a forecasting model.
- Assuming robust standard errors fix a misspecified regression.
- Extrapolating a quadratic model beyond the observed temperature range.
