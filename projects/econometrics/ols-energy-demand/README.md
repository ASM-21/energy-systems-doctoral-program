# Computational Lab: OLS, Robust Inference, and Energy Demand

**Course:** Y1-04 Applied Quantitative Methods for Energy Research  
**Dataset:** Synthetic household-level teaching data, generated deterministically  
**Purpose:** Learn an end-to-end regression workflow without mistaking simulated data for empirical evidence.

## Run

    python -m pip install -r requirements.txt
    python analyze.py --output results
    python -m unittest discover -s . -p "test_*.py" -v

The script generates a reproducible CSV, estimates an OLS model, reports HC3 heteroskedasticity-robust standard errors, and writes a text summary.

## Data-generating process

The synthetic sample includes annual electricity use, floor area, household income, heating degree days, and an electric-heating indicator. The data-generating process is visible in the code. It is intentionally not a model of any particular state, utility, or population.

## Model

    annual_kwh_i = beta0
                 + beta1 * floor_area_i
                 + beta2 * income_1000s_i
                 + beta3 * heating_degree_days_i
                 + beta4 * electric_heat_i
                 + error_i

Interpret coefficients in the units defined by the script. HC3 standard errors address one form of variance misspecification in inference; they do not solve omitted-variable bias, reverse causality, measurement error, sample selection, or external-validity problems.

## Required analysis

1. Explain the unit of observation, outcome, regressors, and intended estimand.
2. Compare bivariate and multivariate estimates of floor-area association.
3. Explain why coefficient changes do not by themselves establish omitted-variable bias.
4. Compare conventional and HC3 standard errors.
5. Inspect residuals and discuss functional form.
6. Identify why the synthetic regression cannot support a real-world policy claim.
7. Propose a public dataset and a credible research design for a real empirical question.

## Submission

Commit the generated data, scripts, regression output, a data dictionary, diagnostic figures, and a 1,000–1,500 word analysis. Record package versions and random seed. Never cite the synthetic results as evidence about actual household energy use.