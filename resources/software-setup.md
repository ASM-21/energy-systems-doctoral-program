# Software and Research Environment

## Recommended stack
Python 3.11+ with venv or conda; JupyterLab or VS Code; pandas, NumPy, SciPy, statsmodels, matplotlib, scikit-learn; Pyomo for optimization; pandapower and/or PyPSA for power systems; Git/GitHub; Zotero for references. R and MATLAB are acceptable where they provide a methodological or compatibility advantage.

## Starter setup
Create a virtual environment, install only the packages needed for the project, and record the exact versions after validating the environment. A starter package set is numpy, pandas, scipy, matplotlib, statsmodels, jupyterlab, pyomo, and pandapower. Do not treat an unpinned starter environment as a production lockfile.

## Project conventions
- data/raw/: immutable source extracts, only where redistribution is permitted.
- data/processed/: derived datasets and documented scripts.
- notebooks/: exploratory analysis and narrative.
- src/: reusable code.
- tests/: validation and regression tests.
- outputs/figures/ and outputs/tables/: generated artifacts.
- references/: citation metadata and source notes.

## Reproducibility checklist
Fresh clone can be configured using documented steps; no secrets or local absolute paths required; source, retrieval date, and license documented; raw inputs not silently overwritten; transformations scripted and tested; random seeds fixed where relevant; outputs regenerated through documented workflow; limitations recorded.