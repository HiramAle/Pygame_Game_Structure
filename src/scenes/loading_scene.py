import pygame
import src.assets as assets
import src.scenes.scene_manager as scene_manager
from threading import Event, Thread
from src.config import *
from src.scenes.scene import Scene
from src.ui_objects import Text
from time import sleep
from src.scenes.mainmenu_scene import MainMenu


class LoadingScreen(Scene):
    """
    Loads assets and initialize game settings
    """

    def __init__(self):
        super().__init__("LoadingScene")
        self.loading = Event()
        pygame.mouse.set_visible(False)
        assets.preload()
        self.loadingStages = 0
        Thread(name="Loading", target=self.load).start()
        self.sprites = self.new_group()
        self.sprites.add(Text((160, 90), "L O A D I N G", WHITE_MOTION, 32))

    def load(self):
        self.loading.set()
        assets.load()
        sleep(0.25)
        self.loadingStages += 1
        sleep(0.25)
        self.loadingStages += 1
        sleep(0.25)
        self.loadingStages += 1
        sleep(0.25)
        self.loading.clear()

    def update(self):
        if not self.loading.is_set():
            scene_manager.switch_scene(MainMenu())

    def render(self):
        self.display.fill(BLACK_MOTION)
        self.sprites.render(self.display)

        if self.loadingStages > 0:
            pygame.draw.circle(self.display, DARK_BLACK_MOTION, (140, 101), 1)
            pygame.draw.circle(self.display, WHITE_MOTION, (140, 100), 1)

        if self.loadingStages > 1:
            pygame.draw.circle(self.display, DARK_BLACK_MOTION, (160, 101), 1)
            pygame.draw.circle(self.display, WHITE_MOTION, (160, 100), 1)

        if self.loadingStages > 2:
            pygame.draw.circle(self.display, DARK_BLACK_MOTION, (180, 101), 1)
            pygame.draw.circle(self.display, WHITE_MOTION, (180, 100), 1)

        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
