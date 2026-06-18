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

## Further Reading

- [ponytail](https://github.com/DietrichGebert/ponytail) — an interesting addition worth exploring
