import pygame
import src.input as input
import src.window as window
import src.time as time
import src.scenes.scene_manager as scene_manager
from src.scenes.loading_scene import LoadingScreen
from src.modules.subnetting.subnetting_creator import *


class Game:
    def __init__(self):
        window.init()
        input.init()
        scene_manager.init(LoadingScreen())

    def run(self):
        while True:
            input.update()
            scene_manager.update()
            scene_manager.render(window.screen)
            time.update()
            pygame.display.update()


if __name__ == '__main__':
    # generate_json_exercise()
    Game().run()
