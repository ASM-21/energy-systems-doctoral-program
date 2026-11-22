# Advanced Mathematical Methods for Energy Systems and Infrastructure Research

**Status:** Planned future course; not part of the current Year 1 workload  
**Placement:** Year 2, before or alongside advanced optimization and system-modeling work  
**Suggested duration:** 2 semesters or 24–30 modular weeks  
**Target study time:** Approximately 2–3 hours/week within the existing 3–5 hour weekly program budget; reduce parallel course load rather than treating this as extra required time  
**Level:** Advanced graduate / doctoral preparation

## Purpose

Build the mathematical maturity needed to formulate, analyze, solve, and critique models of electric power systems, energy markets, infrastructure investment, and energy policy. The course emphasizes derivation and interpretation, not just the use of numerical solvers.

The course should connect each mathematical tool to a real modeling task:
- matrix methods to network equations, power flow, and input-output relationships;
- differential equations and dynamical systems to frequency, voltage, storage, and control;
- probability and stochastic processes to renewable output, load, outages, and market uncertainty;
- convex analysis and duality to dispatch, optimal power flow, market prices, and investment constraints;
- graph theory to grid topology, network flow, and resilience;
- numerical analysis to the stability, accuracy, and limitations of computational models.

## Prerequisite gate

Before starting, demonstrate working fluency in:
- single- and multivariable calculus, partial derivatives, chain rule, Taylor approximations;
- linear algebra: matrix operations, rank, null spaces, eigenvalues/eigenvectors, least squares;
- ordinary differential equations at an introductory engineering level;
- probability, expectation, variance, common distributions, and basic statistical inference;
- Python numerical computing (NumPy, SciPy, plotting, tests) and basic Git.

Use the diagnostic in curriculum/prerequisites.md. Remediate specific gaps rather than repeating entire undergraduate courses.

## Learning outcomes

By the end, the learner should be able to:
1. Prove and use core results about vector spaces, matrix decompositions, norms, eigenvalues, and conditioning.
2. Analyze nonlinear functions using gradients, Hessians, Taylor expansions, and local curvature.
3. Formulate constrained optimization problems and derive KKT conditions, Lagrangians, and dual problems.
4. Explain convexity, strong/weak duality, complementary slackness, and shadow prices.
5. Construct and analyze stochastic models for load, renewable generation, outages, and uncertain investment outcomes.
6. Use graph-theoretic representations and network-flow formulations to analyze grid constraints and infrastructure topology.
7. Analyze linear dynamical systems, stability, state-space models, and feedback control.
8. Select numerical algorithms with an understanding of convergence, conditioning, approximation error, and computational complexity.
9. Translate mathematical results into physical, economic, and regulatory interpretations, including explicit limits on what a model can establish.

## Course sequence

| Module | Core mathematics | Energy-system application | Required evidence |
|---|---|---|---|
| 0. Mathematical maturity | Logic, sets, functions, proof techniques, counterexamples, asymptotic notation | Reading and auditing model assumptions | Short proof portfolio |
| 1. Linear algebra and matrix analysis | Vector spaces, rank, orthogonality, projections, eigenstructure, SVD, positive-definite matrices, matrix norms, conditioning | Bus-admittance matrices, least squares, network sensitivity, dimensional reduction | Derive and test a small network model |
| 2. Multivariable calculus and real-analysis foundations | Gradients, Jacobians, Hessians, Taylor theorem, continuity, differentiability, directional derivatives | Nonlinear power-flow equations, cost curves, local sensitivity | Derivations and numerical sensitivity study |
| 3. Differential equations and dynamical systems | First- and second-order ODEs, linear systems, equilibria, eigenvalue stability, state-space form | Generator/load dynamics, storage state of charge, control response | Simulate and interpret a dynamic system |
| 4. Probability and stochastic processes | Conditional expectation, joint distributions, covariance, LLN/CLT, Markov chains, Poisson processes, Brownian-motion concepts | Load/weather uncertainty, outages, renewable production, queueing and reliability | Reproducible uncertainty model |
| 5. Convex analysis and optimization | Convex sets/functions, epigraphs, separation, subgradients, KKT, Lagrangian and conic duality | Economic dispatch, OPF relaxations, storage scheduling, capacity constraints | Derive primal/dual pair and interpret multipliers |
| 6. Numerical optimization | Gradient/Newton/quasi-Newton methods, line search, interior-point methods, proximal methods, convergence rates, conditioning | Large-scale dispatch, parameter estimation, planning models | Compare solver behavior and diagnose convergence |
| 7. Graph theory and network optimization | Directed/undirected graphs, incidence matrices, cuts, paths, trees, max-flow/min-cut, Laplacians | Transmission/distribution topology, congestion, network resilience | Network-flow model and graph sensitivity |
| 8. Stochastic, robust, and dynamic optimization | Two-stage recourse, scenario trees, chance constraints, robust sets, dynamic programming, Bellman equations | Renewable uncertainty, resource adequacy, resilient investment, storage control | Stochastic or robust planning model |
| 9. Synthesis | Model selection, approximation, sensitivity, uncertainty propagation, reproducibility | Integrated energy-system decision model | Technical paper with mathematical appendix |

## Assessment

The course is assessed through evidence of mathematical reasoning, not only code execution.

- **Problem sets (35%)**: derivations, proofs, counterexamples, and analytical exercises.
- **Computational laboratories (25%)**: tested Python implementations, numerical experiments, and solver diagnostics.
- **Oral or written technical examinations (15%)**: explain assumptions, derive key conditions, and interpret results without relying on code.
- **Final research project (25%)**: a mathematically explicit energy-system model with a reproducible implementation, sensitivity analysis, and limitations statement.

A passing project must show that the learner can explain why the mathematical formulation is appropriate, not merely that a solver returned an answer.

## Suggested capstone directions

1. Derive DC optimal power flow as a constrained optimization problem; interpret nodal prices as dual variables and test the assumptions behind the approximation.
2. Formulate a two-stage stochastic storage or resource-adequacy model under uncertain load and renewable output.
3. Analyze how graph topology and line limits affect congestion and resilience in a small transmission network.
4. Compare deterministic, stochastic, and robust distribution planning under uncertain DER adoption.
5. Build a state-space model for storage or inverter response and analyze local stability.

## Core texts and open course materials

- Stephen Boyd and Lieven Vandenberghe, *Convex Optimization* (Cambridge University Press, 2004). [Author-hosted text and course materials](https://web.stanford.edu/~boyd/cvxbook/).
- Dimitri P. Bertsekas, *Convex Optimization Theory* (Athena Scientific, 2009). Use for deeper theory after the introductory convex optimization material.
- Jorge Nocedal and Stephen J. Wright, *Numerical Optimization*, 2nd ed. (Springer, 2006). [Publisher record](https://link.springer.com/book/10.1007/978-0-387-40065-5).
- Sheldon M. Ross, *Introduction to Probability Models*, 12th ed. (Academic Press, 2019). Use selected chapters for stochastic-process foundations.
- Gilbert Strang, *Introduction to Linear Algebra*, 6th ed. (Wellesley-Cambridge Press, 2023). Use selectively for matrix foundations and geometric intuition.
- Åström and Murray, *Feedback Systems: An Introduction for Scientists and Engineers*. [Free online text](https://fbsbook.org/).
- MIT OpenCourseWare, [6.7220J Nonlinear Optimization (Spring 2025)](https://ocw.mit.edu/courses/6-7220j-nonlinear-optimization-spring-2025/). Graduate benchmark for optimality conditions, convex analysis, Lagrangian duality, and optimization algorithms.
- MIT OpenCourseWare, [6.253 Convex Analysis and Optimization](https://ocw.mit.edu/courses/6-253-convex-analysis-and-optimization-spring-2012/). Graduate benchmark emphasizing proofs, convexity, duality, and algorithmic theory.
- MIT OpenCourseWare, [15.094J Systems Optimization: Models and Computation](https://ocw.mit.edu/courses/15-094j-systems-optimization-models-and-computation-sma-5223-spring-2004/). Application-oriented reference for network, discrete, nonlinear, stochastic, and large-scale optimization.

## Problem sets and assessment sequence

The problem sets are designed to require derivation, interpretation, and reproducible numerical checks. They are deliberately spaced so the mathematics can be learned alongside energy-system applications.

1. [Problem Set 1: Matrix Analysis and Network Structure](problem-set-01-matrix-analysis.md) and [worked solutions](problem-set-01-matrix-analysis-solutions.md). Covers vector spaces, rank-nullity, incidence matrices, graph Laplacians, DC network equations, eigenvalues, positive definiteness, conditioning, and sensitivity.
2. [Problem Set 2: Multivariable Calculus, Curvature, and Local Models](problem-set-02-multivariable-calculus.md) and [worked solutions](problem-set-02-multivariable-calculus-solutions.md). Covers gradients, directional derivatives, Hessian convexity, Jacobians, Newton linearization, Taylor error, and local dynamical stability.
3. [Problem Set 3: Constrained Optimization, KKT Conditions, and Electricity-Market Duality](problem-set-03-constrained-optimization-duality.md) and [worked solutions](problem-set-03-constrained-optimization-duality-solutions.md). Covers convex quadratic dispatch, primal and dual linear programs, KKT conditions, complementary slackness, value functions, and electricity-market price interpretation.
4. [Problem Set 4: Differential Equations, State-Space Models, and Numerical Stability](problem-set-04-differential-equations-dynamics.md) and [worked solutions](problem-set-04-differential-equations-dynamics-solutions.md). Covers storage dynamics, a simplified frequency-response model, eigenmode interpretation, matrix exponentials, explicit-Euler stability, and model validation.
5. [Problem Set 5: Probability, Stochastic Processes, and Reliability Modeling](problem-set-05-probability-stochastic-processes.md) and [worked solutions](problem-set-05-probability-stochastic-processes-solutions.md). Covers correlated net-load uncertainty, Bayes' theorem, Poisson outage arrivals, Markov weather regimes, chance constraints, and Monte Carlo precision.
6. [Problem Set 6: Numerical Optimization, Conditioning, and Convergence](problem-set-06-numerical-optimization.md) and [worked solutions](problem-set-06-numerical-optimization-solutions.md). Covers gradient descent, Newton's method, Armijo line search, preconditioning, least-squares conditioning, and solver verification.
7. [Problem Set 7: Graph Theory, Network Flows, and Infrastructure Resilience](problem-set-07-graph-theory-network-flows.md) and [worked solutions](problem-set-07-graph-theory-network-flows-solutions.md). Covers incidence matrices, cycle spaces, graph Laplacians, max-flow/min-cut, edge connectivity, capacity-aware contingencies, and the distinction between graph screening and electrical feasibility.
8. [Problem Set 8: Stochastic and Robust Optimization for Energy Systems](problem-set-08-stochastic-robust-optimization.md) and [worked solutions](problem-set-08-stochastic-robust-optimization-solutions.md). Covers two-stage recourse, VSS/EVPI, budgeted uncertainty, chance constraints, CVaR, and nonanticipativity.

**Computational companions:** [Stochastic resource-adequacy screening lab](../../../projects/power-systems/stochastic-adequacy/README.md), with reproducible Markov weather and repairable-unit Monte Carlo simulation; and [network-flow and resilience lab](../../../projects/power-systems/network-flow-resilience/README.md), with an Edmonds-Karp solver and minimum-cut certificate. Both are synthetic teaching models, not operational utility assessments.

Do not treat access to worked solutions as a substitute for attempting the derivations. For a useful assessment, complete the assignment first, record uncertainty or errors, then compare against the solution notes and revise the derivation.

## Sequencing and scope control

This is a planned advanced course, not a prerequisite to the current Year 1 work. Do not attempt to complete every module before making progress in energy systems. The recommended order is to finish Year 1 foundations, complete targeted mathematics remediation, then take Modules 1–6 before advanced OPF and stochastic planning. Modules 7–9 can follow or run as research needs dictate.

At 3–5 hours/week, the full course should be spread across two academic years if necessary. Depth and retention take priority over calendar completion. The course should be revised after the first Year 2 optimization and econometrics assignments reveal actual mathematical gaps.
