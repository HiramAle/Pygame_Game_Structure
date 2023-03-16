import pygame
import src.window as Window
from src.config import *
from src.load import load_json
from src.constants import INPUT_DATA, CANVAS_WIDTH, CANVAS_HEIGHT

bindings = load_json(INPUT_DATA)
mouseButtons = {}
mousePosition = pygame.math.Vector2()
keyboardKeys = {}
mouseHover = False
keyDown = False
keyPressed = None


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

    for binding in bindings:
        keyboardKeys[binding] = False


def soft_reset():
    global keyboardKeys, mouseButtons, keyDown, keyPressed

    for action in bindings:
        if bindings[action]["trigger"] == 'press':
            keyboardKeys[action] = False

    mouseButtons['left'] = False
    mouseButtons['right'] = False
    mouseButtons['left_release'] = False
    mouseButtons['right_release'] = False
    mouseButtons['scroll_up'] = False
    mouseButtons['scroll_down'] = False

    if keyDown:
        keyDown = False

    if keyPressed:
        keyPressed = None


def update():
    global mousePosition, keyboardKeys, mouseButtons, mouseHover, keyDown, keyPressed

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mousePosition.x = int(mouse_x / Window.width * CANVAS_WIDTH)
    mousePosition.y = int(mouse_y / Window.height * CANVAS_HEIGHT)

    soft_reset()

    for event in pygame.event.get():
        event: pygame.event.Event

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            keyDown = True
            keyPressed = event.unicode
            for binding in bindings:
                if event.key == bindings[binding]["binding"]:
                    keyboardKeys[binding] = True

        if event.type == pygame.KEYUP:
            for binding in bindings:
                if event.key == bindings[binding]["binding"]:
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
