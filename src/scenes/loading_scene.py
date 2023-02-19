import pygame
from threading import Event, Thread

from src.config import Config
from src.scenes.scene import Scene, SceneManager
from src.scenes.mainmenu_scene import MainMenu


class LoadingScreen(Scene):
    """
    Loads assets and initialize game settings
    """

    def __init__(self, manager: SceneManager):
        super().__init__(manager)
        self.loading = Event()
        self.assets.preload()
        pygame.mouse.set_visible(False)
        Thread(name="Loading", target=self.load).start()
        self.loading_offset = 160 - self.assets.fonts["monogram"]["white"].width("L O A D I N G") / 2
        self.loadingStates = 0
        # self.audio.play_sound("loading")

    def load(self):
        self.loading.set()
        self.assets.load()
        # sleep(2)
        self.loadingStates += 1
        # sleep(2)
        self.loadingStates += 1
        # sleep(1.5)
        self.loadingStates += 1
        # self.audio.fade_out_sound("loading", 1)
        # sleep(1)
        self.loading.clear()

    def update(self, dt: float):
        if not self.loading.is_set():
            self.manager.switch_scene(MainMenu)

    def render(self):
        self.display.fill(Config.BLACK_MOTION)
        self.assets.fonts["monogram"]["black"].render("L O A D I N G", self.display, (self.loading_offset, 71))
        self.assets.fonts["monogram"]["white"].render("L O A D I N G", self.display, (self.loading_offset, 70))

        if self.loadingStates > 0:
            pygame.draw.circle(self.display, Config.DARK_BLACK_MOTION, (140, 101), 1)
            pygame.draw.circle(self.display, Config.WHITE_MOTION, (140, 100), 1)

        if self.loadingStates > 1:
            pygame.draw.circle(self.display, Config.DARK_BLACK_MOTION, (160, 101), 1)
            pygame.draw.circle(self.display, Config.WHITE_MOTION, (160, 100), 1)

        if self.loadingStates > 2:
            pygame.draw.circle(self.display, Config.DARK_BLACK_MOTION, (180, 101), 1)
            pygame.draw.circle(self.display, Config.WHITE_MOTION, (180, 100), 1)

        self.display.blit(self.assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
