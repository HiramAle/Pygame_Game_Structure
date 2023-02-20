import pygame
import os
import json
from src.commons import *
from src.text import Font
from src.config import *


def load_image(path: str, color_key=(0, 0, 0)) -> pygame.Surface:
    image = pygame.image.load(path).convert_alpha()
    image.set_colorkey(color_key)
    return image


def load_json(path: str) -> dict:
    with open(path, "r") as json_file:
        data = json.load(json_file)
    return data


def load_font(path: str, size: int) -> pygame.font.Font:
    return pygame.font.Font(path, size)


def load_image_directory(path: str) -> dict[str, pygame.Surface]:
    directory = {}
    for file in os.listdir(path):
        if os.path.isfile(f"{path}/{file}"):
            filename = file.split(".")[0]
            image = load_image(f"{path}/{file}")
            directory[filename] = image
    return directory


def load_cursors(path: str) -> dict[str, pygame.cursors.Cursor]:
    directory = {}
    for cursor_image in os.listdir(path):
        filename = cursor_image.split(".")[0]
        image = pygame.transform.scale_by(load_image(f"{path}/{cursor_image}"), 3)
        directory[filename] = pygame.cursors.Cursor((0, 0), image)
    return directory


def load_buttons(path: str) -> dict[str, dict[str, pygame.Surface]]:
    directory = {}
    for button in os.listdir(path):
        directory[button] = {}
        for state in os.listdir(f"{path}/{button}"):
            directory[button][state.split(".")[0]] = load_image(f"{path}/{button}/{state}")

    return directory


def load_fonts(path: str) -> dict[str, dict[int, pygame.font.Font]]:
    directory = {}
    for font_file in os.listdir(path):
        font_name = font_file.split(".")[0]
        directory[font_name] = {}
        for size in FONT_SIZES:
            directory[font_name][size] = pygame.font.Font(f"{path}/{font_file}", size)
    return directory

# def load_fonts(path: str) -> dict[str, dict[str, Font]]:
#     directory = {}
#     for font_file in os.listdir(path):
#         if os.path.isfile(f"{path}/{font_file}"):
#             font_name = font_file.split(".")[0]
#
#             font_white = Font(f"{path}/{font_file}", WHITE_MOTION)
#             font_black = Font(f"{path}/{font_file}", DARK_BLACK_MOTION)
#             font_red = Font(f"{path}/{font_file}", RED_MOTION2)
#             directory[f"{font_name}"] = {"white": font_white, "black": font_black, "red": font_red}
#
#     return directory
