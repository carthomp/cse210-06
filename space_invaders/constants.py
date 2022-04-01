import pathlib
from game.casting.color import Color

# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_NAME = "Space Invaders"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "space_invaders/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
BOUNCE_SOUND = "space_invaders/assets/sounds/boing.wav"
WELCOME_SOUND = "space_invaders/assets/sounds/start.wav"
OVER_SOUND = "space_invaders/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "space_invaders/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# --------------------------------------------------------------------------------------------------
# SCRIPTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# --------------------------------------------------------------------------------------------------
# CASTING CONSTANTS
# --------------------------------------------------------------------------------------------------

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 3
MAXIMUM_LIVES = 3

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BULLET
BULLET_GROUP = "balls"
BULLET_IMAGE = "space_invaders/assets/images/000.png"
BULLET_WIDTH = 20
BULLET_HEIGHT = 20
BULLET_VELOCITY = 20

# Ship
SHIP_GROUP = "ships"
SHIP_IMAGES = [
    f"space_invaders/assets/images/{n:03}.png" for n in range(100, 103)]
SHIP_WIDTH = 90
SHIP_HEIGHT = 100
SHIP_RATE = 6
SHIP_VELOCITY = 7

# ENEMY
ENEMY_GROUP = "bricks"
ENEMY_IMAGES = {
    "b": [f"space_invaders/assets/images/{i:03}.png" for i in range(20, 21)],
    "g": [f"space_invaders/assets/images/{i:03}.png" for i in range(22, 23)],
    "p": [f"space_invaders/assets/images/{i:03}.png" for i in range(24, 25)],
    "y": [f"space_invaders/assets/images/{i:03}.png" for i in range(26, 27)]
}
ENEMY_WIDTH = 64
ENEMY_HEIGHT = 64
ENEMY_DELAY = 0.5
ENEMY_RATE = 4
ENEMY_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"
