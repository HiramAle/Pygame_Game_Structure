import pygame

from src.load import *
from src.config import Config
from src.text import Font


class Assets:
    cursors: dict[str, pygame.Surface] = {}
    effects: dict[str, pygame.Surface] = {}
    fonts: dict[str, dict[str, Font]] = {}
    buttons: dict[str, dict[str, pygame.Surface]] = {}
    misc: dict[str, pygame.Surface] = {}

    def preload(self):
        self.effects = load_image_directory(Config.EFFECTS_PATH)
        self.fonts = load_fonts(Config.FONTS_PATH)

    def load(self):
        self.cursors = load_image_directory(Config.CURSORS_PATH)
        self.buttons = load_buttons(Config.BUTTONS_PATH)
        self.misc = load_image_directory(Config.MISC_PATH)

    def set_cursor(self, cursor: str):
        cursor_surface = pygame.transform.scale_by(self.cursors[cursor], 3)
        cursor = pygame.cursors.Cursor((0, 0), cursor_surface)
        pygame.mouse.set_cursor(cursor)
