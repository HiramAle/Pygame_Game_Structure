import pygame

from src.config import Config


class Input:
    def __init__(self):
        self.mouseButtons = {}
        self.mousePosition = pygame.math.Vector2()
        self.keyboardKeys = {}
        self.reset()

    def reset(self):
        self.mouseButtons = {
            "left": False,
            "right": False,
            "left_hold": False,
            "right_hold": False,
            "left_release": False,
            "right_release": False,
            "scroll_up": False,
            "scroll_down": False,
        }

        for binding in Config.BINDINGS:
            self.keyboardKeys[binding] = False

    def soft_reset(self):
        for action in Config.BINDINGS:
            if Config.BINDINGS[action]["trigger"] == 'press':
                self.keyboardKeys[action] = False

        self.mouseButtons['left'] = False
        self.mouseButtons['right'] = False
        self.mouseButtons['left_release'] = False
        self.mouseButtons['right_release'] = False
        self.mouseButtons['scroll_up'] = False
        self.mouseButtons['scroll_down'] = False

    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.mousePosition.x = int(mouse_x / Config.WINDOW_WIDTH * Config.CANVAS_WIDTH)
        self.mousePosition.y = int(mouse_y / Config.WINDOW_HEIGHT * Config.CANVAS_HEIGHT)

        self.soft_reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                for binding in Config.BINDINGS:
                    if event.key == Config.BINDINGS[binding]["binding"]:
                        self.keyboardKeys[binding] = True

            if event.type == pygame.KEYUP:
                for binding in Config.BINDINGS:
                    if event.key == Config.BINDINGS[binding]["binding"]:
                        self.keyboardKeys[binding] = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.mouseButtons['left'] = True
                    self.mouseButtons['left_hold'] = True
                if event.button == 3:
                    self.mouseButtons['right'] = True
                    self.mouseButtons['right_hold'] = True
                if event.button == 4:
                    self.mouseButtons['scroll_up'] = True
                if event.button == 5:
                    self.mouseButtons['scroll_down'] = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouseButtons['left_release'] = True
                    self.mouseButtons['left_hold'] = False
                if event.button == 3:
                    self.mouseButtons['right_release'] = True
                    self.mouseButtons['right_hold'] = False
