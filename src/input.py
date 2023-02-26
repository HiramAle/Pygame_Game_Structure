import pygame
import src.window as Window
from src.config import *

mouseButtons = {}
mousePosition = pygame.math.Vector2()
keyboardKeys = {}
mouseHover = False


def init():
    global mouseButtons, keyboardKeys

    mouseButtons = {
        "left": False,
        "right": False,
        "left_hold": False,
        "right_hold": False,
        "left_release": False,
        "right_release": False,
        "scroll_up": False,
        "scroll_down": False,
    }

    for binding in BINDINGS:
        keyboardKeys[binding] = False


def soft_reset():
    global keyboardKeys, mouseButtons

    for action in BINDINGS:
        if BINDINGS[action]["trigger"] == 'press':
            keyboardKeys[action] = False

    mouseButtons['left'] = False
    mouseButtons['right'] = False
    mouseButtons['left_release'] = False
    mouseButtons['right_release'] = False
    mouseButtons['scroll_up'] = False
    mouseButtons['scroll_down'] = False


def update():
    global mousePosition, keyboardKeys, mouseButtons, mouseHover

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mousePosition.x = int(mouse_x / Window.width * CANVAS_WIDTH)
    mousePosition.y = int(mouse_y / Window.height * CANVAS_HEIGHT)

    soft_reset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            for binding in BINDINGS:
                if event.key == BINDINGS[binding]["binding"]:
                    keyboardKeys[binding] = True

        if event.type == pygame.KEYUP:
            for binding in BINDINGS:
                if event.key == BINDINGS[binding]["binding"]:
                    keyboardKeys[binding] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouseButtons['left'] = True
                mouseButtons['left_hold'] = True
            if event.button == 3:
                mouseButtons['right'] = True
                mouseButtons['right_hold'] = True
            if event.button == 4:
                mouseButtons['scroll_up'] = True
            if event.button == 5:
                mouseButtons['scroll_down'] = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                mouseButtons['left_release'] = True
                mouseButtons['left_hold'] = False
            if event.button == 3:
                mouseButtons['right_release'] = True
                mouseButtons['right_hold'] = False
