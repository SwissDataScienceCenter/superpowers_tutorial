# Demo Repo Design: Superpowers Tutorial

**Date:** 2026-06-18
**Author:** SDSC

## Purpose

A lightweight, self-contained git repo for demonstrating the superpowers plugin to Claude Code users at SDSC. The audience already knows Claude Code — this repo shows them *when* and *how* superpowers helps, with a focus on TDD-driven development.

The repo must be quick to clone, readable in under 5 minutes, and immediately runnable.

## Target Audience

Claude Code users who have never used superpowers. They understand agentic coding but want to see the structured workflow (brainstorm → spec → plan → TDD) in practice before adopting it themselves.

## Approach

Single repo with two branches:

- **`main`** — The starting point as-is: README (what superpowers is + the exercise), a minimal CLAUDE.md, and the `docs/superpowers/` scaffold (specs and plans directories). Participants clone this and run the exercise themselves.
- **`solution`** — Created by actually following the exercise instructions on `main`. Contains the Wordle code, tests, spec, and plan produced by a real superpowers run. Not designed separately — it is the direct output of the exercise.

## Repo Structure

### `main` branch — starting point for participants
```
superpowers_tutorial/
├── README.md                        # What superpowers is + the exercise instructions
├── CLAUDE.md                        # Minimal — superpowers provides its own instructions via the plugin
└── docs/
    └── superpowers/
        ├── specs/                   # Where brainstorming skill writes the spec
        └── plans/                   # Where writing-plans skill writes the plan
```

### `solution` branch — output of a real superpowers run (following the exercise)
```
superpowers_tutorial/
├── README.md
├── CLAUDE.md
├── docs/
│   └── superpowers/
│       ├── specs/
│       │   └── <date>-wordle.md     # Spec produced by brainstorming skill
│       └── plans/
│           └── <date>-wordle.md     # Plan produced by writing-plans skill
└── wordle/
    ├── wordle.py
    ├── words.py
    └── tests/
        └── test_wordle.py
```

## Component Designs

### README.md (`main` branch)

Three short sections that fit on one screen:

1. **What is superpowers?** — Two sentences on the methodology (brainstorm → spec → plan → TDD), link to official plugin page.
2. **Install** — Clone this repo, open a Claude Code session inside it, install the superpowers plugin. One command, scoped to this project directory.
3. **The exercise** — *"Build a CLI Wordle game using Claude Code + superpowers."* Brief pointers on how to start (e.g. `/brainstorm` or just describe the goal to Claude). Ends with: check the `solution` branch afterward to compare your output.

### `solution` branch

The solution branch is created by following the exercise instructions on `main` — not designed separately. A real superpowers run on *"Build a CLI Wordle game"* produces the spec, plan, and implementation, which are committed as-is.

**`docs/superpowers/specs/<date>-wordle.md`** — Verbatim spec output from the brainstorming skill.

**`docs/superpowers/plans/<date>-wordle.md`** — Verbatim plan output from the writing-plans skill.

**`wordle/`** — Direct TDD output: `wordle.py`, `words.py`, `tests/test_wordle.py`. Not cleaned up.

## Constraints

- No dependencies beyond Python stdlib + pytest for the Wordle
- README readable in under 2 minutes
- Repo clone under a few MB (word list kept short — ~2000 common words)
- No secrets, no personal data, no environment variables required

## Success Criteria

- A colleague can clone, read the demo, and understand what superpowers contributed in under 10 minutes
- A colleague can complete either exercise path in one sitting
- Running `pytest wordle/tests/` passes with no setup beyond `pip install pytest`
