import pygame
from src.load import load_json, save_json
from src.constants import USER_DATA_PATH, DEFAULT_PREFERENCES_PATH

WINDOW_WIDTH = 0
WINDOW_HEIGHT = 0
SOUNDS = 0
MUSIC = 0


def init():
    global WINDOW_WIDTH, WINDOW_HEIGHT, SOUNDS, MUSIC

    try:
        preferences = load_json(USER_DATA_PATH)
    except FileNotFoundError:
        display_data = pygame.display.Info()
        preferences = load_json(DEFAULT_PREFERENCES_PATH)
        preferences["window_width"] = display_data.current_w
        preferences["window_height"] = display_data.current_h
        save_json(DEFAULT_PREFERENCES_PATH, preferences)
        save_json(USER_DATA_PATH, preferences)

    WINDOW_WIDTH = preferences["window_width"]
    WINDOW_HEIGHT = preferences["window_height"]
    SOUNDS = preferences["sounds"]
    MUSIC = preferences["music"]


def update_preferences(data: dict):
    preferences = load_json(DEFAULT_PREFERENCES_PATH)
    for key, value in data.items():
        preferences[key] = value
    save_json(USER_DATA_PATH, preferences)
