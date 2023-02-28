import pygame
import src.assets as assets
import src.scenes.scene_manager as scene_manager
import math
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
        self.sprites.add(Text((50, 120), "LOADING", WHITE_MOTION, 32))
        self.veilSurface = self.display.copy()
        self.veilSurface.set_colorkey(GREEN_MOTION)
        self.circlePosition = [160, 90]
        self.defaultCircle = (200, 90)

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
        self.circlePosition[0] = int(self.defaultCircle[0] + (8 * math.cos(pygame.time.get_ticks() / 500)))
        self.circlePosition[1] = int(self.defaultCircle[1] + (8 * math.sin(pygame.time.get_ticks() / 500)))

        if not self.loading.is_set():
            scene_manager.swap_scene(self, MainMenu())

    def render(self):
        self.display.fill(BLUE_MOTION2)
        self.veilSurface.fill(BLACK_MOTION)
        self.sprites.render(self.veilSurface)

        if self.loadingStages > 0:
            pygame.draw.circle(self.veilSurface, DARK_BLACK_MOTION, (80, 121), 1)
            pygame.draw.circle(self.veilSurface, WHITE_MOTION, (80, 120), 1)

        if self.loadingStages > 1:
            pygame.draw.circle(self.veilSurface, DARK_BLACK_MOTION, (90, 121), 1)
            pygame.draw.circle(self.veilSurface, WHITE_MOTION, (90, 120), 1)

        if self.loadingStages > 2:
            pygame.draw.circle(self.veilSurface, DARK_BLACK_MOTION, (100, 121), 1)
            pygame.draw.circle(self.veilSurface, WHITE_MOTION, (100, 120), 1)

        pygame.draw.circle(self.veilSurface, GREEN_MOTION, self.circlePosition, 50)
        self.display.blit(self.veilSurface, (0, 0))

        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
