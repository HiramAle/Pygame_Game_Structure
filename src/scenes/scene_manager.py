import pygame
import src.window as Window
import src.time as Time
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


def transition_scene(from_scene: Scene, to_scene: Scene):
    set_current_scene(CircleTransition(from_scene, to_scene))


def exit_scene() -> None:
    stackScene.pop()


def update() -> None:
    get_current_scene().update()


def render(screen: pygame.Surface) -> None:
    get_current_scene().render()
    screen.blit(pygame.transform.scale(get_current_scene().display, (Window.width, Window.height)), (0, 0))


class Transition(Scene):
    def __init__(self, name: str, to_scene: Scene, from_scene: Scene):
        super().__init__(name)
        self.fromScene: Scene = to_scene
        self.toScene: Scene = from_scene
        self.transitionSpeed = 300


class CircleTransition(Transition):
    def __init__(self, to_scene: Scene, from_scene: Scene):
        super().__init__("circle_transition", to_scene, from_scene)
        self.transitionSurface = from_scene.display.copy()
        self.transitionSurface.set_colorkey(WHITE_MOTION)
        self.circlePosition = self.fromScene.playerPosition
        self.maxCircleRadius = 320
        self.circleRadius = self.maxCircleRadius
        self.transitioningIn = True

    def update(self):
        if self.transitioningIn:
            self.circleRadius -= Time.dt * self.transitionSpeed
            if self.circleRadius <= 0:
                self.transitioningIn = False
                self.circlePosition = self.toScene.playerPosition
        else:
            self.circleRadius += Time.dt * self.transitionSpeed
            if self.circleRadius >= self.maxCircleRadius:
                switch_scene(self.toScene)

    def render(self) -> None:
        if self.transitioningIn:
            self.fromScene.render()
            self.display.blit(self.fromScene.display, (0, 0))
        else:
            self.toScene.render()
            self.display.blit(self.toScene.display, (0, 0))
        self.transitionSurface.fill(DARK_BLACK_MOTION)
        pygame.draw.circle(self.transitionSurface, WHITE_MOTION, self.circlePosition, self.circleRadius)
        self.display.blit(self.transitionSurface, (0, 0))
