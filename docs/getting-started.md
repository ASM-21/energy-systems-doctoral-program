# Getting Started

## First study session

1. Read [How to Use the Program](../curriculum/learning-guide.md) and the [program overview](../curriculum/program-overview.md).
2. Review the [curriculum map](../curriculum/course-map.md), prerequisite diagnostic, and academic standards.
3. Set up Python, Git, and a reference manager using the [software setup guide](../resources/software-setup.md).
4. Create a research-log entry with baseline knowledge, current questions, and a realistic weekly study window.
5. Begin Y1-01 with a diagnostic review of AC circuits, three-phase power, and linear algebra.

## Recommended starting point

Use the Year 1 sequence rather than browsing the repository randomly. Start with power systems, then energy economics. Introduce quantitative methods once the data and programming prerequisites are comfortable, and take markets/regulation after the basic engineering and economic concepts are established. The [Year 1 guide](../courses/year-1/README.md) explains the integration project.

## Weekly rhythm

Use a sustainable 3–5 hour weekly allocation. A typical week includes technical reading, one primary source or research paper, a problem set or coding session, and a short synthesis entry. The learning guide provides a time budget and a repeatable study cycle.

## Problem sets and solutions

Attempt each assignment before opening its worked solution. Compare your derivation, identify errors, correct the work, and record the evidence. Reading a solution is not equivalent to solving the problem.

## What counts as progress

A topic is not complete because a summary exists. Record solved problems, tested code, source notes, written analysis, and project artifacts. Link evidence from the progress tracker and record actual hours rather than intended hours.

## How the program is maintained

The curriculum is intentionally adaptive. New resources and courses are added only when they strengthen a defined competency. The maintainer should prioritize substantive course materials, clear prerequisites, validated project work, and coherent navigation over catalog size. Course status labels distinguish active materials from planned and optional content.

## Local development

Install Python 3.10 or newer. From the repository root:

    make test
    make docs

The test target installs each lab's declared dependencies, runs its unit tests, and fails on the first unsuccessful project. The docs target stages Markdown and static assets, then builds the MkDocs site in strict mode. If Make is unavailable, see the commands in the individual project README files and run the documentation steps in the Makefile directly.
