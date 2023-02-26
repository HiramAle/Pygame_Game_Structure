import pygame
from src.config import *

mouseButtons = {}
mousePosition = pygame.math.Vector2()
keyboardKeys = {}


def init():
    reset()


def reset():
    global mouseButtons
    global keyboardKeys

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
    global keyboardKeys
    global mouseButtons

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
    global mousePosition
    global keyboardKeys
    global mouseButtons

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mousePosition.x = int(mouse_x / WINDOW_WIDTH * Config.CANVAS_WIDTH)
    mousePosition.y = int(mouse_y / WINDOW_HEIGHT * Config.CANVAS_HEIGHT)

    soft_reset()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            print(pygame.key.key_code(event.name))
            for binding in Config.BINDINGS:
                if event.key == Config.BINDINGS[binding]["binding"]:
                    keyboardKeys[binding] = True

        if event.type == pygame.KEYUP:
            for binding in Config.BINDINGS:
                if event.key == Config.BINDINGS[binding]["binding"]:
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
