# CLI Wordle — Design Spec

**Date:** 2026-06-18  
**Status:** Approved

---

## Overview

A single-file command-line Wordle clone in Python. No dependencies beyond the standard library. Players get 6 attempts to guess a secret 5-letter word; each guess is scored and rendered with ANSI color in the terminal.

---

## Structure

Single file: `wordle.py` at the repo root. Organized top-to-bottom:

1. ANSI color constants
2. `WORDS` — module-level list of ~2000 curated 5-letter words
3. `score_guess(guess, target)` — pure scoring function
4. `render_row(scored)` — renders one scored guess as a colored string
5. `print_board(history)` — redraws all rows
6. `print_keyboard(history)` — renders QWERTY keyboard with per-letter color state
7. `play()` — main game loop
8. `if __name__ == "__main__": play()`

---

## Game Logic

### Scoring

`score_guess(guess, target)` returns a list of `(letter, status)` tuples where `status` is one of `"correct"`, `"present"`, or `"absent"`.

Duplicate-letter handling matches the original Wordle rules:
1. First pass: lock in all `"correct"` (right letter, right position) matches.
2. Second pass: for remaining letters, match left-to-right against unmatched target letters for `"present"`.

This ensures a duplicate letter in a guess only gets `"present"` if the target has an unmatched copy remaining.

### Game Loop (`play()`)

1. Assert `WORDS` is non-empty.
2. Pick a random word from `WORDS` using `random.choice`.
3. Loop up to 6 attempts:
   - Prompt for input; strip whitespace and uppercase.
   - Validate (re-prompt on failure, no attempt consumed):
     - Exactly 5 characters.
     - All alphabetic.
     - Present in `WORDS`.
   - Score the guess; append `(guess, scored)` to history.
   - Clear screen and redraw board + keyboard.
   - If all letters are `"correct"`: print win message, exit.
4. After 6 failed attempts: reveal the target word.

---

## Display

### Board

Each guess row is rendered as 5 colored cells using ANSI background codes:

- `\033[42m` — green (correct position)
- `\033[43m` — yellow (present, wrong position)
- `\033[100m` — dark gray (absent)
- `\033[0m` — reset

Letters are printed white-on-color (`\033[97m`). Empty (future) rows show blank gray cells.

The full board (all rows, including empty) is redrawn from scratch after each guess. Screen is cleared with `\033[2J\033[H` before each redraw — no cursor manipulation required.

### Keyboard Tracker

26 letters laid out in QWERTY rows printed below the board. Each letter is colored by its best-known status: green > yellow > gray > unguessed (no color). Updated after every guess.

---

## Error Handling

Validation errors print a one-line message and re-prompt without consuming an attempt:

| Condition | Message |
|---|---|
| Not 5 characters | `"Guess must be 5 letters."` |
| Non-alphabetic | `"Letters only."` |
| Not in word list | `"Not in word list."` |

Startup guard: `assert WORDS, "Word list is empty"` — fails fast if the word list constant is accidentally empty.

No file I/O, no network calls, no other runtime failure surfaces.

---

## Word List

~2000 common 5-letter English words stored as a Python list literal in the source file, all uppercase. Serves as both the pool of valid target words and the set of accepted guesses (no separate valid-guesses list). Input is uppercased before lookup, so the list and all comparisons operate in uppercase throughout.

---

## Non-Goals

- No persistence, streaks, or stats tracking.
- No daily-word mode.
- No hard mode.
- No CLI flags or configuration.
