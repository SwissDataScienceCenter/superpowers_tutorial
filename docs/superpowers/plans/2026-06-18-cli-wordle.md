# CLI Wordle Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a single-file CLI Wordle clone in Python with ANSI color output, a bundled word list, and 6-attempt gameplay.

**Architecture:** Everything lives in `wordle.py` at the repo root — ANSI constants, word list, pure scoring/rendering functions, and the game loop. A companion `tests/test_wordle.py` covers the pure functions. No dependencies beyond the standard library.

**Tech Stack:** Python 3.8+, stdlib only (`random`, `sys`), pytest for tests.

## Global Constraints

- Python 3.8+ (no walrus operator, no match/case)
- Zero third-party dependencies
- All words and comparisons in UPPERCASE throughout
- Exactly 6 attempts, exactly 5-letter words
- No file I/O, no network calls

---

### Task 1: Scaffold `wordle.py` with ANSI constants and word list

**Files:**
- Create: `wordle.py`
- Create: `tests/__init__.py` (empty)
- Create: `tests/test_wordle.py`

**Interfaces:**
- Produces:
  - `GREEN`, `YELLOW`, `GRAY`, `WHITE`, `RESET` — module-level string constants
  - `WORDS` — `list[str]`, uppercase 5-letter words, ~2000 entries
  - `CLEAR` — module-level string constant for clearing the screen

- [ ] **Step 1: Create `wordle.py` with ANSI constants and word list**

The raw list may contain a handful of non-5-letter entries; wrapping it with a filter ensures `WORDS` is always clean.

```python
import random
import sys

GREEN  = "\033[42m"
YELLOW = "\033[43m"
GRAY   = "\033[100m"
WHITE  = "\033[97m"
RESET  = "\033[0m"
CLEAR  = "\033[2J\033[H"

_WORDS = [  # filtered to exactly 5 letters and deduped into WORDS below
    "ABOUT", "ABOVE", "ABUSE", "ACTOR", "ACUTE", "ADMIT", "ADOPT", "ADULT",
    "AFTER", "AGAIN", "AGENT", "AGREE", "AHEAD", "ALARM", "ALBUM", "ALERT",
    "ALIKE", "ALIGN", "ALIVE", "ALLEY", "ALLOW", "ALONE", "ALONG", "ALTER",
    "ANGEL", "ANGER", "ANGLE", "ANGRY", "ANIME", "ANNEX", "ANNOY", "ANTIC",
    "ANVIL", "AORTA", "APART", "APPLE", "APPLY", "APRON", "APTLY", "ARENA",
    "ARGUE", "ARISE", "ARMOR", "AROMA", "AROSE", "ARRAY", "ARROW", "ARTSY",
    "ASCOT", "ASIDE", "ASKED", "ATONE", "ATTIC", "AUDIO", "AUDIT", "AUGUR",
    "AVAIL", "AVERT", "AVOID", "AWAKE", "AWARD", "AWARE", "AWFUL", "AWKWARD",
    "AZURE", "BADGE", "BADLY", "BAGEL", "BANJO", "BANKS", "BARON", "BASIC",
    "BASIS", "BATCH", "BATHE", "BAYOU", "BEACH", "BEADY", "BEARD", "BEAST",
    "BEGAN", "BEGIN", "BEING", "BELOW", "BENCH", "BERRY", "BESET", "BEVEL",
    "BIRCH", "BIRTH", "BISON", "BITER", "BLAND", "BLANK", "BLAST", "BLAZE",
    "BLEAK", "BLEAT", "BLEED", "BLEND", "BLESS", "BLIMP", "BLIND", "BLINK",
    "BLISS", "BLOAT", "BLOCK", "BLOOD", "BLOOM", "BLOWN", "BLUNT", "BLURB",
    "BLURT", "BOAST", "BONUS", "BOOST", "BOOTH", "BOTCH", "BOUGH", "BOUND",
    "BOXER", "BRACE", "BRAID", "BRAIN", "BRAND", "BRAVE", "BRAWL", "BRAWN",
    "BREAK", "BREED", "BREVE", "BRIAR", "BRICK", "BRIDE", "BRIEF", "BRINE",
    "BRINK", "BRINY", "BRISK", "BROOD", "BROOK", "BROTH", "BROWN", "BRUNT",
    "BRUSH", "BRUTE", "BUILD", "BUILT", "BULGE", "BUMPY", "BUNCH", "BURLY",
    "BURST", "BYLAW", "CABAL", "CABIN", "CAMEL", "CANDY", "CARGO", "CARRY",
    "CATCH", "CAUSE", "CEDAR", "CHAIN", "CHAIR", "CHAMP", "CHAOS", "CHARM",
    "CHART", "CHASE", "CHEAP", "CHECK", "CHEEK", "CHEER", "CHESS", "CHEST",
    "CHIEF", "CHILD", "CHILL", "CHIMP", "CHOIR", "CHOKE", "CHORD", "CHOSE",
    "CINCH", "CIVIC", "CIVIL", "CLAIM", "CLAMP", "CLANK", "CLASH", "CLASP",
    "CLASS", "CLAW", "CLEAN", "CLEAR", "CLERK", "CLICK", "CLIFF", "CLING",
    "CLINK", "CLOAK", "CLOCK", "CLONE", "CLOSE", "CLOTH", "CLOUD", "CLOUT",
    "CLOWN", "CLUCK", "CLUMP", "COACH", "COAST", "COLOR", "COMET", "COMIC",
    "COMMA", "CORAL", "COULD", "COUNT", "COURT", "COVER", "CRACK", "CRAFT",
    "CRAMP", "CRANE", "CRASH", "CREAK", "CREED", "CREEK", "CREEP", "CREST",
    "CRIME", "CRIMP", "CRISP", "CROAK", "CROSS", "CROWD", "CROWN", "CRUEL",
    "CRUSH", "CRUST", "CRYPT", "CUBIC", "CUPID", "CURSE", "CURVE", "CYCLE",
    "CYNIC", "DAISY", "DANCE", "DATUM", "DEALT", "DECAY", "DECOY", "DEFER",
    "DELTA", "DENSE", "DEPOT", "DEPTH", "DERBY", "DETOX", "DEVIL", "DIARY",
    "DIGIT", "DINER", "DIRTY", "DISCO", "DITCH", "DITTY", "DIZZY", "DODGE",
    "DOING", "DOUBT", "DOUGH", "DOWRY", "DRAFT", "DRAIN", "DRAMA", "DRANK",
    "DRAPE", "DRAWL", "DREAD", "DREAM", "DRESS", "DRIED", "DRIFT", "DRILL",
    "DRINK", "DRIVE", "DRONE", "DROOL", "DROOP", "DROVE", "DROWN", "DRUID",
    "DRUNK", "DRYER", "DUNCE", "DWARF", "DYING", "EARLY", "EARTH", "EATEN",
    "EBONY", "EDGED", "EIGHT", "ELECT", "ELITE", "EMBER", "EMOTE", "EMPTY",
    "ENACT", "ENDOW", "ENJOY", "ENSUE", "ENTER", "ENTRY", "ENVOY", "EPOCH",
    "EQUAL", "EQUIP", "ERROR", "ESSAY", "ETHIC", "EVADE", "EVENT", "EVERY",
    "EVICT", "EVOKE", "EXACT", "EXERT", "EXILE", "EXIST", "EXPEL", "EXTRA",
    "EXULT", "FABLE", "FACET", "FAINT", "FAIRY", "FAITH", "FANCY", "FATAL",
    "FAULT", "FEAST", "FERAL", "FETCH", "FEUD", "FEVER", "FEWER", "FIBER",
    "FIEND", "FIFTH", "FIFTY", "FIGHT", "FINAL", "FINCH", "FIXED", "FJORD",
    "FLAME", "FLANK", "FLARE", "FLASH", "FLASK", "FLAUNT", "FLAW", "FLEET",
    "FLESH", "FLICK", "FLING", "FLINT", "FLIRT", "FLOAT", "FLOCK", "FLOOD",
    "FLOOR", "FLORA", "FLOSS", "FLOUR", "FLOUT", "FLOWN", "FLUKE", "FLUTE",
    "FOCAL", "FOGGY", "FORCE", "FORGE", "FORTE", "FORUM", "FOUND", "FRAME",
    "FRANK", "FRAUD", "FREAK", "FRESH", "FRONT", "FROST", "FROZE", "FRUIT",
    "FRUGAL", "FUNGI", "FUNNY", "GAUNT", "GAUZE", "GAVEL", "GAWKY", "GEARS",
    "GECKO", "GENRE", "GHOST", "GIANT", "GIVEN", "GLAND", "GLARE", "GLASS",
    "GLEAM", "GLIDE", "GLINT", "GLOAT", "GLOOM", "GLOSS", "GLOVE", "GLYPH",
    "GNASH", "GOING", "GOURD", "GRACE", "GRADE", "GRAIN", "GRAND", "GRANT",
    "GRASP", "GRASS", "GRATE", "GRAVE", "GRAZE", "GREED", "GREET", "GRIEF",
    "GRILL", "GRIND", "GRIPE", "GROAN", "GROOM", "GROPE", "GROSS", "GROUP",
    "GROVE", "GROWL", "GRUEL", "GRUFF", "GRUMP", "GUARD", "GUILE", "GUISE",
    "GULCH", "GUSTO", "GYPSY", "HABIT", "HARSH", "HAVEN", "HAZEL", "HEART",
    "HEAVY", "HEDGE", "HEIST", "HENCE", "HERON", "HINGE", "HIPPO", "HOIST",
    "HOLLY", "HOMER", "HONEY", "HONOR", "HORDE", "HOTEL", "HOUND", "HOUSE",
    "HUMAN", "HUMID", "HUMOR", "HYDRA", "IDEAL", "IDIOM", "IDIOT", "IGLOO",
    "IMAGE", "IMBUE", "IMPLY", "INDEX", "INDIE", "INEPT", "INERT", "INFER",
    "INGOT", "INNER", "INPUT", "INTER", "INTRO", "IRATE", "IRONY", "ISSUE",
    "IVORY", "JAUNT", "JAZZY", "JEWEL", "JOUST", "JUDGE", "JUICE", "JUICY",
    "JUMBO", "KARMA", "KAYAK", "KNACK", "KNEEL", "KNIFE", "KNOCK", "KNOLL",
    "KNOWN", "KUDOS", "LABEL", "LANCE", "LARGE", "LASER", "LATCH", "LATER",
    "LATTE", "LAUGH", "LAYER", "LEACH", "LEARN", "LEASE", "LEASH", "LEAST",
    "LEDGE", "LEGAL", "LEMON", "LEVEL", "LIGHT", "LILAC", "LIMIT", "LINER",
    "LINGO", "LIVER", "LIVID", "LOCAL", "LODGE", "LOGIC", "LOOSE", "LOTTO",
    "LOUSY", "LOVER", "LOWER", "LUCID", "LUCKY", "LUNAR", "LUSTY", "LYING",
    "MAGIC", "MAJOR", "MAKER", "MANOR", "MAPLE", "MARCH", "MASSE", "MATCH",
    "MAXIM", "MAYOR", "MEDIA", "MERIT", "MERRY", "METER", "MICRO", "MIGHT",
    "MIMIC", "MIRTH", "MISER", "MOIST", "MONEY", "MONTH", "MOOSE", "MORAL",
    "MOURN", "MUDDY", "MULTI", "MURAL", "MUSIC", "MUSTY", "NAIVE", "NANNY",
    "NAVAL", "NERVE", "NEVER", "NIECE", "NIGHT", "NINJA", "NOBLE", "NOISE",
    "NORTH", "NOTCH", "NOTED", "NOVEL", "NUDGE", "NYMPH", "OCCUR", "OCTET",
    "OFFAL", "OFFER", "ONSET", "OPERA", "OPTIC", "ORBIT", "ORDER", "ORGAN",
    "OTHER", "OUGHT", "OUTDO", "OUTER", "OUTRUN", "OVARY", "OVOID", "OXIDE",
    "OZONE", "PAINT", "PANDA", "PANEL", "PANIC", "PARSE", "PARTY", "PASTE",
    "PATCH", "PAUSE", "PEACE", "PEACH", "PEARL", "PENAL", "PERCH", "PERIL",
    "PERKY", "PHASE", "PIANO", "PICKY", "PILOT", "PINCH", "PITCH", "PIXEL",
    "PIZZA", "PLACE", "PLAID", "PLAIN", "PLANK", "PLANT", "PLATE", "PLAZA",
    "PLEAD", "PLUCK", "PLUMB", "PLUME", "PLUMP", "PLUNK", "PLUSH", "POACH",
    "POINT", "POLAR", "POLKA", "POLYP", "POOCH", "PORCH", "POSSE", "POUND",
    "POUTY", "POWER", "PRANK", "PRAWN", "PRESS", "PRICE", "PRICK", "PRIDE",
    "PRIME", "PRIMP", "PRIOR", "PRISM", "PRIVY", "PROBE", "PRONE", "PROOF",
    "PROSE", "PROUD", "PROVE", "PROWL", "PRUDE", "PRUNE", "PSALM", "PULSE",
    "PUNCH", "PUPIL", "PYGMY", "QUACK", "QUALM", "QUERY", "QUEST", "QUEUE",
    "QUICK", "QUIET", "QUIRK", "QUOTA", "QUOTE", "RABBI", "RADAR", "RADIO",
    "RAINY", "RALLY", "RANCH", "RANGE", "RAPID", "RAVEN", "REACH", "REALM",
    "REBEL", "RECAP", "RECON", "RECUT", "REEDY", "REGAL", "REIGN", "RELAX",
    "RELAY", "RELIC", "REMIT", "RERUN", "REVEL", "RIDER", "RIDGE", "RIFLE",
    "RIGHT", "RISKY", "RIVAL", "ROAST", "ROBOT", "ROCKY", "ROGUE", "ROMAN",
    "ROOST", "ROSTER", "ROUGE", "ROUGH", "ROUND", "ROUSE", "ROYAL", "RUDDY",
    "RULER", "RURAL", "RUSTY", "SADLY", "SAINT", "SALAD", "SALSA", "SALTY",
    "SALVE", "SANDY", "SAUCE", "SAUCY", "SAVOR", "SCALD", "SCALE", "SCALP",
    "SCANT", "SCARE", "SCARF", "SCENE", "SCONE", "SCOOP", "SCOPE", "SCORE",
    "SCOUT", "SCOWL", "SCRAM", "SCRAP", "SCUFF", "SEIZE", "SENSE", "SERVE",
    "SEVEN", "SHAFT", "SHAKE", "SHALL", "SHALE", "SHAME", "SHAPE", "SHARE",
    "SHARK", "SHARP", "SHAWL", "SHEEN", "SHEER", "SHELF", "SHELL", "SHIFT",
    "SHIRE", "SHIRT", "SHOCK", "SHORE", "SHOUT", "SHOVE", "SHOWY", "SHRED",
    "SHRUB", "SHRUG", "SIEGE", "SIREN", "SKILL", "SKIMP", "SKUNK", "SLACK",
    "SLAIN", "SLANT", "SLASH", "SLATE", "SLEEK", "SLEET", "SLEPT", "SLICE",
    "SLIDE", "SLIME", "SLIMY", "SLING", "SLINK", "SLOPE", "SLOSH", "SLOTH",
    "SLUMP", "SLUNG", "SLUNK", "SMACK", "SMALL", "SMART", "SMASH", "SMEAR",
    "SMELL", "SMELT", "SMILE", "SMIRK", "SMITE", "SMOKE", "SMOKY", "SNACK",
    "SNAKY", "SNARE", "SNEAK", "SNEER", "SNIDE", "SNIFF", "SNORE", "SNORT",
    "SNOUT", "SNOWY", "SOAPY", "SOLAR", "SOLVE", "SONIC", "SORRY", "SOUTH",
    "SPACE", "SPADE", "SPARE", "SPARK", "SPAWN", "SPEAK", "SPEAR", "SPECK",
    "SPEED", "SPEND", "SPICY", "SPILL", "SPINE", "SPITE", "SPLAT", "SPLIT",
    "SPOKE", "SPOOF", "SPOOK", "SPOOL", "SPORT", "SPOUT", "SPRAY", "SPREE",
    "SPRIG", "SPUNK", "SQUAD", "SQUAT", "SQUID", "STACK", "STAFF", "STAGE",
    "STAIN", "STAIR", "STAKE", "STALE", "STALK", "STALL", "STAMP", "STAND",
    "STANK", "STARK", "START", "STASH", "STATE", "STAYS", "STEAK", "STEAL",
    "STEAM", "STEEP", "STEER", "STERN", "STIFF", "STILL", "STING", "STINK",
    "STOCK", "STOIC", "STOMP", "STONE", "STOOD", "STOOP", "STORE", "STORK",
    "STORM", "STORY", "STOUT", "STOVE", "STRAP", "STRAW", "STRAY", "STRIP",
    "STRUT", "STUCK", "STUDY", "STUMP", "STUNG", "STUNK", "STUNT", "STYLE",
    "SUAVE", "SUGAR", "SUITE", "SULKY", "SUNNY", "SUPER", "SURGE", "SWAMP",
    "SWARM", "SWEAR", "SWEAT", "SWEEP", "SWEET", "SWIFT", "SWILL", "SWIPE",
    "SWIRL", "SWOON", "SWORD", "SWORE", "SWARM", "SWUNG", "SYNTH", "TABBY",
    "TALON", "TANGY", "TAPIR", "TAUNT", "TAWNY", "TENSE", "TENTH", "TEPID",
    "TERSE", "THEME", "THERE", "THESE", "THICK", "THING", "THINK", "THORN",
    "THOSE", "THREE", "THREW", "THROW", "THUMB", "THUMP", "TIARA", "TIDAL",
    "TIGER", "TIGHT", "TILDE", "TIMID", "TIPSY", "TITAN", "TITHE", "TODAY",
    "TOKEN", "TOPIC", "TORCH", "TOTAL", "TOUCH", "TOUGH", "TOWEL", "TOXIC",
    "TRACK", "TRADE", "TRAIL", "TRAIN", "TRAMP", "TRASH", "TRAWL", "TREAD",
    "TREED", "TREND", "TRIAL", "TRICK", "TROOP", "TROTH", "TROUT", "TROVE",
    "TRUCE", "TRUCK", "TRUER", "TRULY", "TRUMP", "TRUNK", "TRUSS", "TRUST",
    "TRUTH", "TULIP", "TUMOR", "TUNER", "TUNIC", "TWEAK", "TWILL", "TWINE",
    "TWIRL", "TWIST", "TYING", "ULTRA", "UMBRA", "UNDUE", "UNIFY", "UNION",
    "UNITE", "UNTIL", "UNZIP", "UPSET", "URBAN", "USHER", "UTTER", "UVULA",
    "VAGUE", "VALID", "VALOR", "VALUE", "VALVE", "VAPOR", "VAULT", "VAUNT",
    "VENOM", "VERGE", "VERSE", "VICAR", "VIGOR", "VIRAL", "VISOR", "VISTA",
    "VITAL", "VIVID", "VIXEN", "VOGUE", "VOICE", "VOILA", "VOTER", "VOUCH",
    "VULVA", "WACKY", "WALTZ", "WASTE", "WATCH", "WATER", "WEARY", "WEAVE",
    "WEDGE", "WEEDY", "WEIRD", "WHACK", "WHALE", "WHIFF", "WHILE", "WHINE",
    "WHIRL", "WHISK", "WITTY", "WOMAN", "WORLD", "WORRY", "WORSE", "WORST",
    "WORTH", "WOULD", "WOUND", "WRATH", "WRING", "WRIST", "WRONG", "YACHT",
    "YEARN", "YOUNG", "YOURS", "YOUTH", "ZAPPY", "ZEBRA", "ZILCH", "ZIPPY",
    "ZONAL", "ZONED", "ZIPPY",
]
WORDS = list({w for w in _WORDS if len(w) == 5})  # dedupe + enforce 5-letter constraint


if __name__ == "__main__":
    pass
```

- [ ] **Step 2: Create `tests/__init__.py`**

```bash
mkdir -p tests && touch tests/__init__.py
```

- [ ] **Step 3: Verify file exists**

```bash
python -c "import wordle; print(len(wordle.WORDS), 'words loaded')"
```
Expected output: `<N> words loaded` (N > 0)

- [ ] **Step 4: Commit**

```bash
git add wordle.py tests/__init__.py
git commit -m "feat: scaffold wordle.py with ANSI constants and word list"
```

---

### Task 2: Implement `score_guess`

**Files:**
- Modify: `wordle.py`
- Create: `tests/test_wordle.py`

**Interfaces:**
- Consumes: `WORDS: list[str]` from Task 1
- Produces: `score_guess(guess: str, target: str) -> list[tuple[str, str]]`
  - Returns list of 5 `(letter, status)` tuples; status is `"correct"`, `"present"`, or `"absent"`

- [ ] **Step 1: Write failing tests**

Create `tests/test_wordle.py`:

```python
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
    # R is present (in CRANE but not at pos 0), A correct (pos 2), C present, E present, D absent
    assert result[0] == ("R", "present")
    assert result[2] == ("A", "correct")
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
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_wordle.py -v
```
Expected: errors like `ImportError: cannot import name 'score_guess'`

- [ ] **Step 3: Implement `score_guess` in `wordle.py`** (add after the `WORDS` list, before `if __name__ == "__main__"`)

```python
def score_guess(guess: str, target: str) -> list:
    result = [None] * 5
    target_remaining = list(target)

    # First pass: correct positions
    for i, (g, t) in enumerate(zip(guess, target)):
        if g == t:
            result[i] = (g, "correct")
            target_remaining[i] = None

    # Second pass: present letters
    for i, g in enumerate(guess):
        if result[i] is not None:
            continue
        if g in target_remaining:
            result[i] = (g, "present")
            target_remaining[target_remaining.index(g)] = None
        else:
            result[i] = (g, "absent")

    return result
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_wordle.py -v
```
Expected: all 5 tests PASS

- [ ] **Step 5: Commit**

```bash
git add wordle.py tests/test_wordle.py
git commit -m "feat: implement score_guess with duplicate-letter handling"
```

---

### Task 3: Implement `render_row` and `print_board`

**Files:**
- Modify: `wordle.py`
- Modify: `tests/test_wordle.py`

**Interfaces:**
- Consumes: `score_guess` → `list[tuple[str, str]]`; `GREEN`, `YELLOW`, `GRAY`, `WHITE`, `RESET` from Task 1
- Produces:
  - `render_row(scored: list[tuple[str, str]]) -> str` — returns a single printable string with ANSI codes
  - `render_empty_row() -> str` — returns a blank row string (5 gray cells)
  - `print_board(history: list[tuple[str, list[tuple[str, str]]]]) -> None` — prints all 6 rows

- [ ] **Step 1: Write failing tests**

Add to `tests/test_wordle.py`:

```python
from wordle import render_row, render_empty_row, GREEN, YELLOW, GRAY, WHITE, RESET


def test_render_row_contains_green_for_correct():
    scored = [("C", "correct"), ("R", "absent"), ("A", "absent"), ("N", "absent"), ("E", "absent")]
    row = render_row(scored)
    assert GREEN in row
    assert "C" in row


def test_render_row_contains_yellow_for_present():
    scored = [("C", "present"), ("R", "absent"), ("A", "absent"), ("N", "absent"), ("E", "absent")]
    row = render_row(scored)
    assert YELLOW in row


def test_render_row_contains_gray_for_absent():
    scored = [("C", "absent"), ("R", "absent"), ("A", "absent"), ("N", "absent"), ("E", "absent")]
    row = render_row(scored)
    assert GRAY in row


def test_render_empty_row_has_five_cells():
    row = render_empty_row()
    # Should contain GRAY (blank cells) and RESET
    assert GRAY in row
    assert RESET in row
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_wordle.py::test_render_row_contains_green_for_correct -v
```
Expected: `ImportError: cannot import name 'render_row'`

- [ ] **Step 3: Implement `render_row`, `render_empty_row`, and `print_board` in `wordle.py`**

Add after `score_guess`:

```python
def render_row(scored: list) -> str:
    COLOR = {"correct": GREEN, "present": YELLOW, "absent": GRAY}
    cells = []
    for letter, status in scored:
        cells.append(f"{COLOR[status]}{WHITE} {letter} {RESET}")
    return " ".join(cells)


def render_empty_row() -> str:
    cell = f"{GRAY}   {RESET}"
    return " ".join([cell] * 5)


def print_board(history: list) -> None:
    for guess, scored in history:
        print(render_row(scored))
    for _ in range(6 - len(history)):
        print(render_empty_row())
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
python -m pytest tests/test_wordle.py -v
```
Expected: all tests PASS

- [ ] **Step 5: Commit**

```bash
git add wordle.py tests/test_wordle.py
git commit -m "feat: implement render_row, render_empty_row, print_board"
```

---

### Task 4: Implement `print_keyboard`

**Files:**
- Modify: `wordle.py`
- Modify: `tests/test_wordle.py`

**Interfaces:**
- Consumes: `GREEN`, `YELLOW`, `GRAY`, `WHITE`, `RESET`; `history: list[tuple[str, list[tuple[str, str]]]]`
- Produces: `print_keyboard(history: list[tuple[str, list[tuple[str, str]]]]) -> None`

Priority rule: `"correct"` > `"present"` > `"absent"` > unguessed.

- [ ] **Step 1: Write failing test**

Add to `tests/test_wordle.py`:

```python
from wordle import print_keyboard
import io


def test_print_keyboard_shows_correct_color(capsys):
    scored = score_guess("CRANE", "CRANE")
    history = [("CRANE", scored)]
    print_keyboard(history)
    out = capsys.readouterr().out
    # All letters of CRANE are correct, so GREEN should appear
    assert GREEN in out


def test_print_keyboard_correct_beats_present(capsys):
    # First guess marks C as present, second marks C as correct
    scored1 = [("C", "present"), ("R", "absent"), ("A", "absent"), ("N", "absent"), ("E", "absent")]
    scored2 = [("C", "correct"), ("R", "absent"), ("A", "absent"), ("N", "absent"), ("E", "absent")]
    history = [("CRANZ", scored1), ("CRANE", scored2)]
    print_keyboard(history)
    out = capsys.readouterr().out
    assert GREEN in out
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
python -m pytest tests/test_wordle.py::test_print_keyboard_shows_correct_color -v
```
Expected: `ImportError: cannot import name 'print_keyboard'`

- [ ] **Step 3: Implement `print_keyboard` in `wordle.py`**

Add after `print_board`:

```python
QWERTY = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
PRIORITY = {"correct": 3, "present": 2, "absent": 1}


def print_keyboard(history: list) -> None:
    state = {}
    for _, scored in history:
        for letter, status in scored:
            current = state.get(letter)
            if current is None or PRIORITY[status] > PRIORITY[current]:
                state[letter] = status

    COLOR = {"correct": GREEN, "present": YELLOW, "absent": GRAY}
    print()
    for row in QWERTY:
        cells = []
        for letter in row:
            status = state.get(letter)
            if status:
                cells.append(f"{COLOR[status]}{WHITE} {letter} {RESET}")
            else:
                cells.append(f" {letter} ")
        print(" ".join(cells))
```

- [ ] **Step 4: Run all tests to verify they pass**

```bash
python -m pytest tests/test_wordle.py -v
```
Expected: all tests PASS

- [ ] **Step 5: Commit**

```bash
git add wordle.py tests/test_wordle.py
git commit -m "feat: implement print_keyboard with priority-based coloring"
```

---

### Task 5: Implement `play()` and wire up `__main__`

**Files:**
- Modify: `wordle.py`

**Interfaces:**
- Consumes: `WORDS`, `CLEAR`, `score_guess`, `print_board`, `print_keyboard` from prior tasks
- Produces: fully playable game via `python wordle.py`

No unit tests for `play()` — it's an I/O loop. Tested manually.

- [ ] **Step 1: Implement `play()` and update `__main__` in `wordle.py`**

Replace the `if __name__ == "__main__": pass` block and add `play()` before it:

```python
def play() -> None:
    assert WORDS, "Word list is empty"
    target = random.choice(WORDS)
    history = []
    error = ""

    for attempt in range(6):
        print(CLEAR, end="")
        print(f"  WORDLE  —  Attempt {attempt + 1}/6\n")
        print_board(history)
        print_keyboard(history)
        if error:
            print(f"\n{error}")
            error = ""
        guess = input("\nGuess: ").strip().upper()

        if len(guess) != 5:
            error = "Guess must be 5 letters."
            attempt -= 1  # re-do this attempt
            # use a loop instead
            # redo via continue after decrementing is not valid in for-loops
            # use while loop below
            continue
        if not guess.isalpha():
            error = "Letters only."
            continue
        if guess not in WORDS:
            error = "Not in word list."
            continue

        scored = score_guess(guess, target)
        history.append((guess, scored))

        if all(s == "correct" for _, s in scored):
            print(CLEAR, end="")
            print(f"  WORDLE\n")
            print_board(history)
            print_keyboard(history)
            print(f"\nYou got it in {len(history)}! The word was {target}.")
            return

    print(CLEAR, end="")
    print(f"  WORDLE\n")
    print_board(history)
    print_keyboard(history)
    print(f"\nGame over! The word was {target}.")


if __name__ == "__main__":
    play()
```

**Note:** The `for`-loop `continue` on invalid input does NOT consume an attempt because `attempt` is re-used via `continue` — but Python's `for` loop auto-increments. Replace the `for` loop with a `while` loop so invalid input truly doesn't consume an attempt:

```python
def play() -> None:
    assert WORDS, "Word list is empty"
    target = random.choice(WORDS)
    history = []
    error = ""
    attempt = 0

    while attempt < 6:
        print(CLEAR, end="")
        print(f"  WORDLE  —  Attempt {attempt + 1}/6\n")
        print_board(history)
        print_keyboard(history)
        if error:
            print(f"\n{error}")
            error = ""

        guess = input("\nGuess: ").strip().upper()

        if len(guess) != 5:
            error = "Guess must be 5 letters."
            continue
        if not guess.isalpha():
            error = "Letters only."
            continue
        if guess not in WORDS:
            error = "Not in word list."
            continue

        scored = score_guess(guess, target)
        history.append((guess, scored))
        attempt += 1

        if all(s == "correct" for _, s in scored):
            print(CLEAR, end="")
            print(f"  WORDLE\n")
            print_board(history)
            print_keyboard(history)
            print(f"\nYou got it in {len(history)}! The word was {target}.")
            return

    print(CLEAR, end="")
    print(f"  WORDLE\n")
    print_board(history)
    print_keyboard(history)
    print(f"\nGame over! The word was {target}.")


if __name__ == "__main__":
    play()
```

- [ ] **Step 2: Run all existing tests to confirm nothing broke**

```bash
python -m pytest tests/test_wordle.py -v
```
Expected: all tests PASS

- [ ] **Step 3: Smoke test the game manually**

```bash
python wordle.py
```
Expected: board renders with 6 empty rows, keyboard shows below, prompt appears. Play one full game — win or lose — and verify the final message and word reveal are correct.

- [ ] **Step 4: Commit**

```bash
git add wordle.py
git commit -m "feat: implement play() game loop — game is now playable"
```
