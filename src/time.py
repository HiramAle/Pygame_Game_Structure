import pygame


class Time:
    dt = 0.2
    clock = pygame.time.Clock()

    def update(self):
        self.dt = self.clock.tick() / 1000
