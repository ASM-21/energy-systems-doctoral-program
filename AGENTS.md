# Agent and Maintainer Instructions

This repository is an independent doctoral-level curriculum and research portfolio. Treat it as a maintained academic product, not a disposable generated document.

## Primary responsibilities
- Maintain academic rigor, technical correctness, and source traceability.
- Build sequenced curriculum, assessments, computational labs, and research projects.
- Verify institutional course references and regulatory materials against primary sources.
- Improve navigation, accessibility, reproducibility, and website quality.
- Identify weak assumptions, outdated sources, missing prerequisites, and gaps proactively.
- Keep the repository's progress record honest: never mark learning or project work complete without user-produced evidence.

## Non-negotiable standards
- Never fabricate citations, course numbers, syllabi, data, findings, or external review.
- Distinguish proposed materials from completed work.
- Prefer primary sources for laws, tariffs, orders, standards, and market rules.
- Cite exact versions/effective dates for time-sensitive regulatory material.
- Label synthetic data clearly.
- Do not commit credentials, proprietary employer data, confidential utility information, or restricted datasets.
- Do not claim an analysis is causal without a defensible identification strategy.
- Preserve reproducibility and document assumptions.

## Working style
- Make substantive progress without asking the user to approve routine editorial or technical decisions.
- Ask only when a decision materially changes the program's direction, requires personal information, creates a cost/account/security implication, or cannot be safely inferred.
- Prefer complete, reviewable increments over superficial bulk.
- Run tests and link checks where possible before publishing.
- Keep main branch coherent; use focused commits.
- Provide concise change summaries with material caveats.

## Academic design
At 3–5 hours/week, prioritize a small number of deep courses and substantial projects. Avoid an inflated course catalog. Each course must follow the shared curriculum/course-template.md structure and specify status, prerequisites, learning outcomes, sequence, workload, required versus optional material, assessments, solution availability, computational resources, completion evidence, and next steps. Keep navigation hierarchical: year → course → assignments/solutions; do not maintain a flat list of dozens of problem sets.

## Publication and website
The website must clearly state the program is not accredited. It should be generated from canonical repository content, accessible, responsive, searchable, and maintainable. Do not copy third-party copyrighted materials into the repository.

## Local validation commands
- Run make test to install each computational lab's dependencies and execute its tests.
- Run make docs to stage Markdown/static assets and build the MkDocs site in strict mode.
- Keep Makefile, CI matrix, and project inventory synchronized when adding or removing a computational lab.
