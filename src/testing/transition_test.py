import pygame
import math
import src.input as Input
import src.time as Time
import src.scenes.scene_manager as SceneManager
from src.scenes.scene import Scene
from src.config import *


class Test1(Scene):
    def __init__(self):
        super().__init__("test1")
        self.playerPosition = (0,0)

    def calculate_circular_position(self, radius: int | float, center: tuple):
        x = center[0] + (radius * math.cos(pygame.time.get_ticks() / 500))
        y = center[1] + (radius * math.sin(pygame.time.get_ticks() / 500))

        self.circlePosition = int(x), int(y)

    def update(self) -> None:
        if Input.keyboardKeys["ESC"]:
            SceneManager.transition_scene(self, Test3())

    def render(self) -> None:
        self.display.fill(RED_MOTION)


class Test3(Scene):
    def __init__(self):
        super().__init__("test3")
        self.playerPosition = (160, 90)

    def render(self) -> None:
        self.display.fill(BLUE_MOTION2)


class Test2(Scene):
    def __init__(self):
        super().__init__("test2")
        self.transitioning = True
        self.transitionSurface = self.display.copy()
        self.transitionSurface.set_colorkey(WHITE_MOTION)
        self.circlePosition = (160, 80)
        self.circleRadius = 0
        self.transitionSpeed = 300

    def update_transition(self):
        if not self.transitioning:
            return
        if self.way == "out":
            self.circleRadius -= Time.dt * self.transitionSpeed
            if self.circleRadius <= 0:
                SceneManager.switch_scene(Test2())
        else:
            self.circleRadius += Time.dt * self.transitionSpeed
            if self.circleRadius >= 160:
                self.transitioning = False

    def render_transition(self):
        if not self.transitioning:
            return
        self.transitionSurface.fill(DARK_BLACK_MOTION)
        pygame.draw.circle(self.transitionSurface, WHITE_MOTION, self.circlePosition, self.circleRadius)
        self.display.blit(self.transitionSurface, (0, 0))

    def update(self) -> None:
        self.update_transition()

    def render(self) -> None:
        self.display.fill(YELLOW_MOTION)
        self.render_transition()
