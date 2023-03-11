import pygame
import src.assets as assets
import src.scenes.scene_manager as scene_manager
import math
from threading import Event, Thread
from src.config import *
from src.scenes.scene import Scene
from src.sprite import Sprite, SpriteGroup
from src.ui_objects import GUIText
from time import sleep
from src.scenes.mainmenu_scene import MainMenu


class Circle(Sprite):
    def __init__(self):
        image = pygame.Surface((180, 180))
        image.set_colorkey((0, 0, 0))
        pygame.draw.circle(image, GREEN_MOTION, (90, 90), 90)
        super().__init__("circle", (440, 180), image)
        self.rotationPosition = self.x, self.y

    def update(self):
        self.x = int(self.rotationPosition[0] + (8 * math.cos(pygame.time.get_ticks() / 500)))
        self.y = int(self.rotationPosition[1] + (8 * math.sin(pygame.time.get_ticks() / 500)))


class Point(Sprite):
    def __init__(self, position: tuple, *groups: SpriteGroup):
        diameter = 6
        radius = diameter / 2
        image = pygame.Surface((diameter, diameter + 1))
        image.set_colorkey((0, 0, 0))
        pygame.draw.circle(image, DARK_BLACK_MOTION, (radius, radius + 1), radius)
        pygame.draw.circle(image, WHITE_MOTION, (radius, radius), radius)
        super().__init__("point", position, image, *groups)


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
        GUIText((200, 180), "LOADING", 48, WHITE_MOTION, True, 0, self.sprites)
        self.veilSurface = self.display.copy()
        self.veilSurface.set_colorkey(GREEN_MOTION)
        self.circle = Circle()
        self.point1 = Point((160, 220), self.sprites)
        self.point1.disable()
        self.point2 = Point((200, 220), self.sprites)
        self.point2.disable()
        self.point3 = Point((240, 220), self.sprites)
        self.point3.disable()

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
        self.circle.update()
        if not self.loading.is_set():
            scene_manager.swap_scene(self, MainMenu())

    def render(self):
        self.display.fill(BLUE_MOTION2)
        self.veilSurface.fill(BLACK_MOTION)
        self.sprites.render(self.veilSurface)

        if self.loadingStages > 0:
            self.point1.enable()
        if self.loadingStages > 1:
            self.point2.enable()
        if self.loadingStages > 2:
            self.point3.enable()

        self.circle.render(self.veilSurface)

        self.display.blit(self.veilSurface, (0, 0))

        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
