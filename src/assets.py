import pygame

from src.load import *
from src.config import *
from src.text import Font

cursors: dict[str, pygame.cursors.Cursor] = {}
effects: dict[str, pygame.Surface] = {}
fonts: dict[str, dict[int, pygame.font.Font]] = {}
buttons: dict[str, dict[str, pygame.Surface]] = {}
misc: dict[str, pygame.Surface] = {}


def preload() -> None:
    global effects, fonts
    effects = load_image_directory(EFFECTS_PATH)
    fonts = load_fonts(FONTS_PATH)


def load() -> None:
    global cursors, buttons, misc
    cursors = load_cursors(CURSORS_PATH)
    buttons = load_buttons(BUTTONS_PATH)
    misc = load_image_directory(MISC_PATH)
# class Assets:
#     buttons: dict[str, dict[str, pygame.Surface]] = {}
#     misc: dict[str, pygame.Surface] = {}
#
#     def load(self):
#         self.cursors = load_image_directory(CURSORS_PATH)
#         self.buttons = load_buttons(BUTTONS_PATH)
#         self.misc = load_image_directory(MISC_PATH)
#
#     def set_cursor(self, cursor: str):
#         cursor_surface = pygame.transform.scale_by(self.cursors[cursor], 3)
#         cursor = pygame.cursors.Cursor((0, 0), cursor_surface)
#         pygame.mouse.set_cursor(cursor)
