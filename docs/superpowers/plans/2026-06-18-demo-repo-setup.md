# Demo Repo Setup (main branch) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Set up the `main` branch of the superpowers tutorial repo with a README, minimal CLAUDE.md, and the docs scaffold — the complete starting point participants clone before running the exercise.

**Architecture:** Three files to create/update (README.md, CLAUDE.md, docs/superpowers/plans/.gitkeep), each committed separately. The `solution` branch is out of scope — it is created later by actually following the exercise.

**Tech Stack:** Git, Markdown

## Global Constraints

- README readable in under 2 minutes
- No code dependencies, no secrets, no environment variables
- `docs/superpowers/specs/` and `docs/superpowers/plans/` must both exist in the committed tree

---

### Task 1: Write README.md

**Files:**
- Create: `README.md`

**Interfaces:**
- Produces: primary onboarding document; participants read this before opening Claude Code

- [ ] **Step 1: Write README.md**

```markdown
# Superpowers Tutorial

**Superpowers** is a plugin for Claude Code that structures your AI coding sessions: it brainstorms requirements with you, writes a spec, produces a step-by-step implementation plan, and drives development test-first. Instead of vibes-driven prompting, you get a repeatable workflow — brainstorm → spec → plan → TDD.

Plugin page: https://claude.com/plugins/superpowers

## Install

Clone this repo, then open a Claude Code session inside it:

```bash
git clone <repo-url>
cd superpowers_tutorial
claude
```

In the Claude Code session, install superpowers scoped to this directory:

```
/plugin install superpowers@claude-plugins-official
```

## The Exercise

**Build a CLI Wordle game using Claude Code + superpowers.**

Start by telling Claude what you want to build:

> "Let's build a CLI Wordle game."

Superpowers will ask clarifying questions, write a spec, produce an implementation plan, and guide you through test-driven development. Let it lead — the structured workflow is the point.

When you're done, check the `solution` branch to compare your output with a reference run:

```bash
git checkout solution
```
```

- [ ] **Step 2: Verify the README**

Read the file aloud or in a previewer. Check:
- Fits on one screen (under 2 minutes to read)
- `/plugin install superpowers@claude-plugins-official` is copy-pasteable
- The exercise instruction leaves no ambiguity about what to build

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add README with superpowers intro and Wordle exercise"
```

Expected: commit succeeds, `git log --oneline -1` shows the message.

---

### Task 2: Write CLAUDE.md

**Files:**
- Modify: `CLAUDE.md` (currently empty)

**Interfaces:**
- Produces: minimal project context Claude reads when participants open a session in this directory

- [ ] **Step 1: Write CLAUDE.md**

```markdown
# superpowers_tutorial

A tutorial repo for the superpowers plugin for Claude Code.

## Structure

- `docs/superpowers/specs/` — brainstorming skill writes specs here
- `docs/superpowers/plans/` — writing-plans skill writes plans here
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "docs: add minimal CLAUDE.md"
```

Expected: commit succeeds.

---

### Task 3: Track empty plans directory

**Files:**
- Create: `docs/superpowers/plans/.gitkeep`

The `specs/` directory is already tracked (it contains the design doc). The `plans/` directory is empty and needs a `.gitkeep` so git includes it.

- [ ] **Step 1: Add .gitkeep**

```bash
touch docs/superpowers/plans/.gitkeep
```

- [ ] **Step 2: Verify both scaffold directories exist**

```bash
ls docs/superpowers/specs/
ls docs/superpowers/plans/
```

Expected output:
```
# specs/:
2026-06-18-demo-repo-design.md

# plans/:
.gitkeep  2026-06-18-demo-repo-setup.md
```

- [ ] **Step 3: Commit**

```bash
git add docs/superpowers/plans/.gitkeep
git commit -m "chore: track empty plans directory"
```

Expected: commit succeeds.

---

### Task 4: Verify final main branch state

- [ ] **Step 1: Confirm committed tree**

```bash
git ls-files
```

Expected output (order may vary):
```
CLAUDE.md
README.md
docs/superpowers/plans/.gitkeep
docs/superpowers/plans/2026-06-18-demo-repo-setup.md
docs/superpowers/specs/2026-06-18-demo-repo-design.md
```

- [ ] **Step 2: Confirm clean working tree**

```bash
git status
```

Expected: `nothing to commit, working tree clean`

- [ ] **Step 3: Smoke-test clone experience**

Mentally walk through the participant flow:
1. Clone → `README.md` is the first thing they see ✓
2. Open Claude Code → `CLAUDE.md` gives Claude the project structure ✓
3. Install plugin → `docs/superpowers/specs/` and `docs/superpowers/plans/` exist for the skills to write into ✓
4. Start exercise → tell Claude "Let's build a CLI Wordle game" ✓
