import pygame
from src.testing import input_test
from src.config import Config


class Game:
    def __init__(self):
        pygame.init()
        input_test.init()
        self.window = pygame.display.set_mode((320, 180))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            input_test.update()
            self.window.fill(Config.RED_MOTION2)
            self.clock.tick()
            print(input_test.mouseButtons["left_hold"])
            pygame.display.update()


if __name__ == '__main__':
    Game().run()
