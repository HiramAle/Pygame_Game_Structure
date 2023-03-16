import pygame
import src.input as input
import src.window as window
import src.time as time
import src.scenes.scene_manager as scene_manager
from src.scenes.loading_scene import LoadingScreen
from src.scenes.game_selector_scene import GameSelectorScene
import src.config as config


class Game:
    def __init__(self):
        pygame.init()
        config.init()
        window.init()
        input.init()
        scene_manager.init(LoadingScreen())

    def run(self):
        while True:
            input.update()
            time.update()
            scene_manager.update()
            scene_manager.render(window.screen)
            pygame.display.update()


if __name__ == '__main__':
    Game().run()
