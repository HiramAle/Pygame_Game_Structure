import pygame
from src.scenes.scene import Stage, StagedScene
from src.ui_objects import *
from src.commons import sin_wave
from src.scenes.options_menu_stage import OptionsStage
import src.time as time


class Logo(GUIImage):
    def __init__(self, position: tuple, image: pygame.Surface, *groups):
        super().__init__(position, image, *groups)
        self.scale(4)
        self.set_centered(False)

    def update(self):
        if not self.isEnabled:
            return
        self.y = sin_wave(93, 5, 200)


class MainStage(Stage):
    def __init__(self, scene: StagedScene):
        super().__init__("main_stage", scene)
        # Logo
        self.logo = Logo((147, 93), assets.misc["logo"], self.sprites)
        # Options
        self.newGame = Option("- NEW GAME -", (96, 167), self.sprites)
        self.continueGame = Option("- CONTINUE -", (96, 197), self.sprites)
        self.options = Option("- OPTIONS -", (96, 227), self.sprites)
        self.exit = Option("- EXIT -", (96, 257), self.sprites)

        # self.sprites.disable()

        self.optionsIndex = 0
        self.optionsTimer = time.Timer(0.2)
        self.optionsTimer.start()
        self.loaded = False

    def update(self) -> None:
        self.update_groups()
        if self.exit.released():
            exit()

        if self.options.released():
            self.scene.set_stage(OptionsStage(self.scene))

    def render(self) -> None:
        self.render_groups()
