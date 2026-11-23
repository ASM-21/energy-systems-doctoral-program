# Problem Set 6: Worked Solutions and Identification Notes

## Problem 1. Segmented regression

\(\beta_0\) is the baseline intercept and \(\beta_1\) is the pre-intervention trend per time period. \(\beta_2\) is the immediate level shift at \(T_0\). \(\beta_3\) is the change in slope. At horizon \(h\) after intervention, the fitted gap relative to the extrapolated pre-trend is \(\beta_2+\beta_3h\). This is a descriptive contrast unless the pre-trend is a credible untreated counterfactual and no coincident shock changes the outcome. With \(\beta_2=0\) and \(\beta_3\neq0\), the immediate gap is zero while the gap grows linearly with horizon.

## Problem 2. Serial dependence and HAC

Positive serial correlation makes nearby residuals contain overlapping information. The OLS point estimate may remain unbiased under strict exogeneity, but the iid covariance formula generally misstates uncertainty. Newey–West estimates a heteroskedasticity- and autocorrelation-consistent covariance matrix using weighted residual autocovariances up to a selected lag. It changes estimated uncertainty, not the identifying assumptions or the regression's conditional mean. Bandwidth that is too short misses dependence; bandwidth that is too long adds noisy covariance estimates. Report a primary rule and sensitivity to plausible alternatives.

## Problem 3. Unit roots

Independent random walks can drift together by chance in a finite sample, producing high R-squared and apparently significant t-statistics even without an economic relationship. Covariance stationarity requires a constant mean, finite constant variance, and autocovariance depending only on lag. The ADF null is a unit root; the alternative is stationarity around the deterministic terms included in the test. Failure to reject may reflect low power, especially near a unit root. Differencing removes a stochastic trend under appropriate conditions but changes the target from a level relation to a relation among changes.

## Problem 4. Cointegration

Two I(1) series are cointegrated if a nonzero linear combination is I(0). The coefficient \(\theta\) describes a long-run equilibrium relation, not necessarily a causal effect. In an error-correction model, a negative \(\lambda\) means a positive lagged deviation in \(y-\theta x\) predicts a reduction in subsequent \(\Delta y\), conditional on the model. Cointegration describes common stochastic trends; it does not establish exogenous variation. A policy regime, market redesign, technology shift, or measurement change can alter the long-run vector, so test stability and avoid imposing a full-sample relation across known breaks without justification.

## Problem 5. Forecast evaluation

Rolling-origin evaluation trains only on information available before each forecast origin and evaluates on subsequent observations. Random splitting can leak future regimes and serially adjacent observations into training. MAE is mean absolute error; RMSE is the square root of mean squared error and penalizes large errors more heavily; MASE scales MAE by an in-sample naive benchmark. Prediction intervals describe uncertainty for future observations, including irreducible innovation noise; confidence intervals describe uncertainty in estimated parameters or a conditional mean. Forecast accuracy concerns prediction, not a counterfactual causal effect.

## Problem 6. Break tests

A known-date intervention test evaluates a date specified by external institutional knowledge. An unknown-break search estimates candidate break dates from outcomes and must account for the search procedure. Searching many dates and reporting the most significant one inflates false-positive risk. A Chow test compares parameter stability at a specified date under its model assumptions; it is not a universal detector and may be invalid with serial dependence unless inference is adapted. CUSUM and sup-Wald tests detect instability patterns but do not identify the cause. Freeze policy dates from primary institutional records; label data-driven break dates exploratory and adjust inference for the search.

## Problem 7. Design memo rubric

A high-quality memo distinguishes the immediate level effect, trend change, and horizon-specific fitted gap; documents the policy date; demonstrates a plausible counterfactual; handles seasonality and serial correlation; assesses stationarity and breaks; and pre-specifies windows and placebo dates. It reports coefficients in interpretable units and includes an explicit statement that model diagnostics do not prove causal identification. If a plausible concurrent shock cannot be separated, the result must be labeled associational.
