import pygame

from src.scenes.scene import Scene
from src.config import *

stackScene: list[Scene] = []


def init(scene: Scene) -> None:
    set_current_scene(scene)


def get_current_scene() -> Scene:
    global stackScene
    if stackScene:
        return stackScene[-1]


def set_current_scene(scene: Scene) -> None:
    stackScene.append(scene)


def switch_scene(new_scene: Scene) -> None:
    set_current_scene(new_scene)


def exit_scene() -> None:
    stackScene.pop()


def update(dt: float) -> None:
    get_current_scene().update(dt)


def render(screen: pygame.Surface) -> None:
    get_current_scene().render()
    screen.blit(pygame.transform.scale(get_current_scene().display, (WINDOW_WIDTH, WINDOW_HEIGHT)), (0, 0))
