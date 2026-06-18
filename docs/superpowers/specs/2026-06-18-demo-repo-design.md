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

- **`main`** — A blank slate. Contains only the top-level README (what superpowers is, how to install it, what to build) and a minimal CLAUDE.md. Participants clone this and run superpowers themselves from scratch.
- **`solution`** — The reference output from a real superpowers run: Wordle code, tests, spec, implementation plan, and annotated transcript. Participants can check this branch after completing the exercise to compare their output.

## Repo Structure

### `main` branch — blank slate for participants
```
superpowers_tutorial/
├── README.md      # What superpowers is, how to install it, what to build
└── CLAUDE.md      # Minimal — superpowers provides its own instructions via the plugin
```

### `solution` branch — reference output from a real superpowers run
```
superpowers_tutorial/
├── README.md
├── CLAUDE.md
├── docs/
│   └── demo/
│       ├── README.md        # Narrative walkthrough of the run
│       ├── spec.md          # Design doc produced by brainstorming skill
│       ├── plan.md          # Implementation plan produced by writing-plans skill
│       └── transcript.md   # Curated annotated highlights from the agent run
└── wordle/
    ├── wordle.py
    ├── words.py
    └── tests/
        └── test_wordle.py
```

## Component Designs

### README.md (`main` branch)

Four short sections that fit on one screen:

1. **What is superpowers?** — Two sentences on the methodology (brainstorm → spec → plan → TDD), link to official plugin.
2. **Install** — Clone this repo, open a Claude Code session inside it, run `/plugin install superpowers@claude-plugins-official`. Superpowers is scoped to this project directory, not installed globally.
3. **Your mission** — One sentence: *"Build a CLI Wordle game using Claude Code."* That's it — superpowers will guide the rest.
4. **Compare your result** — After completing the exercise, check the `solution` branch to see the spec, plan, and Wordle produced by a reference run. Two optional extensions are suggested there (hard mode, session stats) for those who want to go further.

### docs/demo/ (`solution` branch)

**`README.md`** — Four sections telling the story of the reference run:
1. The prompt that started it
2. What superpowers did (clarifying questions → spec → plan → red/green TDD)
3. The result (how to run the game and tests, with static test output)
4. Why it worked (three bullets: spec before code, TDD enforced, no scope creep)

**`transcript.md`** — Curated excerpts (not a full dump) of the most instructive moments: brainstorming questions, first failing test, first passing test, final test suite summary. Each excerpt has a one-line annotation.

**`spec.md` and `plan.md`** — Verbatim output from the superpowers run. The Wordle is built by running Claude Code + superpowers on *"Let's build a CLI Wordle game"*, answering its clarifying questions, and letting it execute the TDD plan. Outputs are committed unedited.

### wordle/ — The Wordle Implementation

A Python CLI game with no dependencies beyond stdlib. Tests use `pytest` only.

Core mechanics to implement (and test):
- Word validation (5 letters, in word list)
- Letter match scoring (correct / wrong position / absent)
- Game loop (6 guesses, win/loss detection)
- Display (colour-coded feedback in terminal)

The implementation is the direct output of the superpowers TDD run — not cleaned up — so participants see realistic agent output.

## Constraints

- No dependencies beyond Python stdlib + pytest for the Wordle
- README readable in under 2 minutes
- Repo clone under a few MB (word list kept short — ~2000 common words)
- No secrets, no personal data, no environment variables required

## Success Criteria

- A colleague can clone, read the demo, and understand what superpowers contributed in under 10 minutes
- A colleague can complete either exercise path in one sitting
- Running `pytest wordle/tests/` passes with no setup beyond `pip install pytest`
