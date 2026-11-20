# Getting Started

## First study session

1. Read the program overview and academic standards.
2. Review the Year 1 course sequence and prerequisites.
3. Set up Python, Git, and a reference manager.
4. Create a research log entry with your baseline knowledge and current questions.
5. Start Y1-01 with a diagnostic review of AC circuits, three-phase power, and linear algebra.

## Weekly rhythm

Use a sustainable 3–5 hour weekly allocation. A suggested pattern is one focused technical reading session, one primary-source or research-paper session, one problem/coding session, and a short synthesis entry.

## What counts as progress

A topic is not complete because a summary exists. Record solved problems, tested code, source notes, written analysis, and project artifacts. Link evidence from the progress tracker.

## How the program is maintained

The curriculum is intentionally adaptive. New resources and courses are added only when they strengthen a defined competency. The maintainer should prioritize substantive course materials and validated project work over catalog size.

## Local development

Install Python 3.10 or newer. From the repository root:

    make test
    make docs

The test target installs each lab's declared dependencies, runs its unit tests, and fails on the first unsuccessful project. The docs target stages Markdown and static assets, then builds the MkDocs site in strict mode. If Make is unavailable, see the commands in the individual project README files and run the documentation steps in the Makefile directly.
