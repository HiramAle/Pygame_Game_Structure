import pygame

from src.window import Window
from src.time import Time
from src.input import Input
from src.scenes.scene import SceneManager
from src.assets import Assets
from src.scenes.loading_scene import LoadingScreen
from src.audio import Audio


class Game:
    def __init__(self):
        self.window = Window()
        self.time = Time()
        self.input = Input()
        self.assets = Assets()
        self.audio = Audio()
        self.sceneManager = SceneManager(self.input, self.assets, self.audio)
        self.sceneManager.switch_scene(LoadingScreen)

    def run(self):
        while True:
            self.input.update()
            self.sceneManager.update(self.time.dt)
            self.sceneManager.render(self.window.screen)
            self.time.update()
            pygame.display.update()


if __name__ == '__main__':
    Game().run()
