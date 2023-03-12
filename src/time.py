import pygame

dt = 0.2
clock = pygame.time.Clock()


def update():
    global dt
    global clock
    dt = clock.tick() / 1000


class Timer:
    def __init__(self, duration_seconds: int | float):
        self.startingTime = pygame.time.get_ticks()
        self.duration = duration_seconds * 1000
        self.done = True
        self._started = False

    def start(self):
        self._started = True
        self.startingTime = pygame.time.get_ticks()
        self.done = False

    def update(self) -> bool:
        if not self._started:
            return False
        if not self.done and pygame.time.get_ticks() - self.startingTime > self.duration:
            self.done = True
            self._started = False
            return True
        return False
