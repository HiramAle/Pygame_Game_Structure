import pygame
import math


def swap_color(image: pygame.Surface, from_color: str | tuple, to_color: str | tuple) -> pygame.Surface:
    bg_surface = image.copy()
    bg_surface.fill(to_color)
    surface = image.copy()
    surface.set_colorkey(from_color)
    bg_surface.blit(surface, (0, 0))
    return bg_surface


def clip_surface(surface: pygame.Surface, clip_x, clip_y, clip_width, clip_height) -> pygame.Surface:
    clip = pygame.Surface((clip_width, clip_height))
    clip.set_colorkey(surface.get_colorkey())
    clip_area = pygame.Rect(clip_x, clip_y, clip_width, clip_height)
    clip.blit(surface, (0, 0), clip_area)
    return clip


def sin_wave(value: int | float, distance: int, speed: int, time=1280) -> int:
    time = pygame.time.get_ticks() / 2 % time
    return int(value + math.sin(time / speed) * distance)
