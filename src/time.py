import pygame

dt = 0.2
clock = pygame.time.Clock()


def update():
    global dt
    global clock
    dt = clock.tick() / 1000
