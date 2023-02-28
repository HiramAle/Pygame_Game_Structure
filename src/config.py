import pygame.cursors

# Screen
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
CAPTION = "Structure"
# Canvas
CANVAS_WIDTH = 320
CANVAS_HEIGHT = 180
FONT_SIZES = [16, 32]
# Colors
BACKGROUND_COLOR = "#1E1E1E"
WHITE = "#E2E2E2"
BLACK = "#FFFFFF"
RED = "#EA5E5E"
YELLOW = "#F7BA3E"
BLUE = "#56B3B4"
PURPLE = "#BF85BF"
GRAY = "#465862"
# Motion
RED_MOTION = "#ff6470"
YELLOW_MOTION = "#ffc66d"
BLUE_MOTION = "#68ABDF"
GREEN_MOTION = "#99c47a"
WHITE_MOTION = "#f2f2f2"
DARK_BLACK_MOTION = "#101010"
BLACK_MOTION = "#242424"
GRAY_MOTION = "#666666"
BLUE_MOTION2 = "#1ab8d2"
RED_MOTION2 = "#de5451"
# Paths
CURSORS_PATH = "data/images/cursors"
EFFECTS_PATH = "data/images/effects"
FONTS_PATH = "data/text"
SOUNDS_PATH = "data/audio"
BUTTONS_PATH = "data/images/buttons"
MISC_PATH = "data/images/misc"
CONTROLLERS_PATH = "data/images/controllers"
CABLES_PATH = "data/images/cables_scene"
SUBNETTING_PATH = "data/images/subnetting_scene"
# Input
BINDINGS = {
    "UP": {
        "trigger": "press",
        "binding": 119
    },
    "LEFT": {
        "trigger": "press",
        "binding": 97
    },
    "DOWN": {
        "trigger": "press",
        "binding": 115
    },
    "RIGHT": {
        "trigger": "press",
        "binding": 100
    },
    "INTERACT": {
        "trigger": "press",
        "binding": 101
    },
    "TAB": {
        "trigger": "press",
        "binding": 9
    },
    "ESC": {
        "trigger": "press",
        "binding": 27
    },
    "SPACE": {
        "trigger": "press",
        "binding": 32
    }

}
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

MOUSE_HOVER_EVENT = pygame.USEREVENT + 1
