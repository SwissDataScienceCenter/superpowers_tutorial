# Demo Repo Design: Superpowers Tutorial

**Date:** 2026-06-18
**Author:** christian.donner@datascience.ch

## Purpose

A lightweight, self-contained git repo for demonstrating the superpowers plugin to Claude Code users at SDSC. The audience already knows Claude Code — this repo shows them *when* and *how* superpowers helps, with a focus on TDD-driven development.

The repo must be quick to clone, readable in under 5 minutes, and immediately runnable.

## Target Audience

Claude Code users who have never used superpowers. They understand agentic coding but want to see the structured workflow (brainstorm → spec → plan → TDD) in practice before adopting it themselves.

## Approach

Single linear repo (Option A). Everything — spec, plan, finished code, tests, annotated transcript — lives in one place. No branch switching, no submodules.

## Repo Structure

```
superpowers_tutorial/
├── README.md                        # What superpowers is, how to install, where to start
├── CLAUDE.md                        # Minimal — superpowers provides its own instructions
│
├── docs/
│   ├── demo/
│   │   ├── README.md                # Narrative walkthrough of the demo run
│   │   ├── spec.md                  # Design doc produced by brainstorming skill
│   │   ├── plan.md                  # Implementation plan produced by writing-plans skill
│   │   └── transcript.md           # Curated annotated highlights from the agent run
│   │
│   └── exercise/
│       └── README.md                # Two exercise paths with reflection prompt
│
└── wordle/                          # Finished Wordle CLI — pre-built by superpowers
    ├── wordle.py
    ├── words.py
    └── tests/
        └── test_wordle.py
```

## Component Designs

### Top-level README.md

Three short sections that fit on one screen:

1. **What is superpowers?** — Two sentences on the methodology (brainstorm → spec → plan → TDD), link to official plugin.
2. **Install** — Copy-paste commands for Claude Code and the superpowers plugin (`/plugin install superpowers@claude-plugins-official`).
3. **What's in this repo** — One-line description of `docs/demo/` and `docs/exercise/`, pointer to start at `docs/demo/README.md`.

### docs/demo/README.md

Four sections telling the story of the Wordle build:

1. **The prompt** — The single sentence that started the session: *"Let's build a CLI Wordle game."*
2. **What happened** — Brief narrative: superpowers paused, asked clarifying questions, produced a spec, then a plan, then ran red/green TDD cycles per mechanic. Links to annotated moments in `transcript.md`.
3. **The result** — How to run the game (`python wordle/wordle.py`) and tests (`pytest wordle/tests/`). Static test output shown so nothing needs to run.
4. **Why it worked** — Three bullets on superpowers' contribution: spec before code, TDD discipline enforced, no scope creep.

### docs/demo/transcript.md

Curated excerpts (not a full dump) showing the most instructive moments:
- The brainstorming clarifying questions
- The first failing test (red)
- The first passing test (green)
- The final test suite summary

Each excerpt has a one-line annotation explaining what superpowers was doing and why.

### docs/demo/spec.md and plan.md

The actual design doc and implementation plan produced during the demo run. These are committed verbatim so participants can see the quality of output superpowers produces.

### docs/exercise/README.md

Two clearly labelled paths:

**Path 1 — Re-run the full flow (30–60 min)**
Start a fresh Claude Code session in an empty directory. Prompt: *"Let's build a CLI Wordle game."* Compare your spec and plan against `docs/demo/spec.md` and `docs/demo/plan.md`.

**Path 2 — Extend the finished Wordle (15–30 min)**
Start a Claude Code session in `wordle/`. Choose a feature:
- Hard mode (guesses must reuse confirmed letters)
- Session stats (win/loss tracking across games)
- Daily word mode (date-seeded word selection)

Both paths end with the reflection question: *"What would you have done differently without superpowers?"*

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
