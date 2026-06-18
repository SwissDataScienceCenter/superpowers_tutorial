import pytest
from wordle import score_guess


def test_all_correct():
    result = score_guess("CRANE", "CRANE")
    assert result == [
        ("C", "correct"),
        ("R", "correct"),
        ("A", "correct"),
        ("N", "correct"),
        ("E", "correct"),
    ]


def test_all_absent():
    result = score_guess("FIZZY", "CRANE")
    statuses = [s for _, s in result]
    assert statuses == ["absent", "absent", "absent", "absent", "absent"]


def test_present():
    result = score_guess("RACED", "CRANE")
    # R is present (in CRANE but not at pos 0), A present (pos 1, in CRANE at 2), C present, E present, D absent
    assert result[0] == ("R", "present")
    assert result[1] == ("A", "present")
    assert result[4] == ("D", "absent")


def test_duplicate_in_guess_only_one_yellow():
    # Target CRANE has one R; guess RARER has R at 0,2,4
    result = score_guess("RARER", "CRANE")
    statuses = {i: s for i, (_, s) in enumerate(result)}
    # Only one R should be non-absent (the first unmatched one)
    r_statuses = [s for l, s in result if l == "R"]
    assert r_statuses.count("absent") == 2  # two of the three Rs are absent


def test_duplicate_correct_beats_present():
    # Target SPEED, guess SEEDS: S correct, E correct pos1, E present pos2 (one E left), D absent, S absent
    result = score_guess("SEEDS", "SPEED")
    assert result[0] == ("S", "correct")   # S at 0 matches
    assert result[4] == ("S", "absent")    # second S, target S already matched
