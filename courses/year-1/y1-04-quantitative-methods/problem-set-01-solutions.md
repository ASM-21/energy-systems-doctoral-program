# Y1-04 Problem Set 1 — Solution Notes

## Problem 1

Standard error = s/sqrt(n) = 240/10 = 24 kWh. Approximate 95% interval:

    850 +/- 1.96*24 = [802.96, 897.04] kWh

Under the sampling assumptions, this procedure has approximately 95% long-run coverage. It does not mean there is a 95% probability that this fixed parameter lies inside this particular frequentist interval. Nonresponse, frame coverage, clustering, and non-random selection can create bias not represented by the standard error.

## Problem 2

Minimize sum_i (y_i - beta_0 - beta_1 x_i)^2. The first-order conditions imply the fitted residuals sum to zero and are orthogonal to x. The slope estimator is:

    beta_1_hat = sum_i (x_i-xbar)(y_i-ybar) / sum_i (x_i-xbar)^2

The slope is the estimated conditional change in annual consumption MWh associated with one additional square foot in a linear bivariate model. It is not automatically causal. If income affects both house size and electricity use, omitted income can correlate with x and enter the error term. Exogeneity requires E[u|X]=0 for the relevant model and sampling design.

## Problem 3

Heteroskedasticity means conditional error variance is not constant; omitted-variable bias occurs when a relevant determinant is excluded and correlated with included regressors. Under exogeneity, heteroskedasticity alone does not bias OLS coefficients, but conventional homoskedastic standard errors are generally invalid. Heteroskedasticity-robust covariance estimators can improve inference under suitable regularity conditions. They do not remove omitted-variable bias, reverse causality, measurement error, or selection.

## Problem 4

Weather, prices, income, occupancy, economic conditions, seasonality, energy-efficiency upgrades, and other programs may change at the same time. A randomized rollout assigns eligible customers to treatment timing by lottery where feasible. A comparison-group design requires credible untreated outcomes.

Difference-in-differences relies on a parallel-trends assumption in the absence of treatment, along with appropriate treatment timing, no anticipation, stable composition, and no spillovers that invalidate the comparison. Pre-trend evidence is useful but cannot prove the assumption. Treatment selection can bias estimates if adoption correlates with changing outcomes or expected usage.

## Review standard

Distinguish estimand, estimator, identifying assumptions, statistical uncertainty, and external validity. A technically correct regression can answer the wrong question.