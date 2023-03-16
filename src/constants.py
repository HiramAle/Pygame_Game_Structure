from os.path import dirname, join

# Canvas
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 360
CAPTION = "Structure"
# Fonts
FONT_SIZES = [16, 32, 48, 64]
# Motion Colours
RED_MOTION = "#de5451"
BLUE_MOTION = "#1ab8d2"
YELLOW_MOTION = "#ffc66d"
GREEN_MOTION = "#99c47a"
WHITE_MOTION = "#f2f2f2"
DARK_BLACK_MOTION = "#101010"
BLACK_MOTION = "#242424"
GRAY_MOTION = "#666666"
# Paths


CURSORS_PATH = "data/images/cursors"
EFFECTS_PATH = "data/images/effects"
FONTS_PATH = "data/gui/fonts"
SOUNDS_PATH = "data/audio"
BUTTONS_PATH = "data/images/buttons"
MISC_PATH = "data/images/misc"
CONTROLLERS_PATH = "data/images/controllers"
CABLES_PATH = "data/images/cables_scene"
SUBNETTING_PATH = "data/images/subnetting_scene"
BACKGROUNDS_PATH = "data/images/backgrounds"
PROJECT_PATH = dirname(dirname(__file__))
SUBNETTING_EXERCISES_PATH = "data/scenes/subnetting"
DEFAULT_PREFERENCES_PATH = "data/files/default_preferences.json"
USER_DATA_PATH = "data/user/preferences.json"
INPUT_DATA = "data/files/input.json"
# Cables Data
CABLES = ["PLAIN_GREEN",
          "STRIP_GREEN",
          "PLAIN_ORANGE",
          "STRIP_ORANGE",
          "PLAIN_BLUE",
          "STRIP_BLUE",
          "PLAIN_BROWN",
          "STRIP_BROWN"]

CABLES_568_A = ["STRIP_GREEN",
                "PLAIN_GREEN",
                "STRIP_ORANGE",
                "PLAIN_BLUE",
                "STRIP_BLUE",
                "PLAIN_ORANGE",
                "STRIP_BROWN",
                "PLAIN_BROWN"]

CABLES_568_B = ["STRIP_ORANGE",
                "PLAIN_ORANGE",
                "STRIP_GREEN",
                "PLAIN_BLUE",
                "STRIP_BLUE",
                "PLAIN_GREEN",
                "STRIP_BROWN",
                "PLAIN_BROWN"]

CABLE_STANDARDS = {"A": CABLES_568_A, "B": CABLES_568_B}
