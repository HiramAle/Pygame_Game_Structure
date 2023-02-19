import pygame
import os
from src.commons import *
from src.text import Font
from src.config import Config


def load_image(path: str, color_key=(0, 0, 0)) -> pygame.Surface:
    image = pygame.image.load(path).convert_alpha()
    image.set_colorkey(color_key)
    return image


def load_image_directory(path: str) -> dict[str, pygame.Surface]:
    directory = {}
    for file in os.listdir(path):
        if os.path.isfile(f"{path}/{file}"):
            filename = file.split(".")[0]
            image = load_image(f"{path}/{file}")
            directory[filename] = image
    return directory


def load_buttons(path: str) -> dict[str, dict[str, pygame.Surface]]:
    directory = {}
    for button in os.listdir(path):
        directory[button] = {}
        for state in os.listdir(f"{path}/{button}"):
            directory[button][state.split(".")[0]] = load_image(f"{path}/{button}/{state}")

    return directory


def load_fonts(path: str) -> dict[str, dict[str, Font]]:
    directory = {}
    for font_file in os.listdir(path):
        if os.path.isfile(f"{path}/{font_file}"):
            font_name = font_file.split(".")[0]

            font_white = Font(f"{path}/{font_file}", Config.WHITE_MOTION)
            font_black = Font(f"{path}/{font_file}", Config.DARK_BLACK_MOTION)
            font_red = Font(f"{path}/{font_file}", Config.RED_MOTION2)
            directory[f"{font_name}"] = {"white": font_white, "black": font_black, "red": font_red}

    return directory
