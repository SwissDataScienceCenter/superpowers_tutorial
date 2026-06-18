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
