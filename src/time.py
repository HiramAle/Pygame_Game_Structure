import pygame

dt = 0.2
clock = pygame.time.Clock()


def update():
    global dt
    global clock
    dt = clock.tick() / 1000


class Timer:
    def __init__(self, duration_seconds: int):
        self.startingTime = pygame.time.get_ticks()
        self.duration = duration_seconds * 1000
        self.done = False

    def start(self):
        self.startingTime = pygame.time.get_ticks()
        self.done = False

    def update(self):
        if not self.done and pygame.time.get_ticks() - self.startingTime > self.duration:
            self.done = True
