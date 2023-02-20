from src.scenes.scene import Scene
from src.config import *
import src.input as input
import src.scenes.scene_manager as scene_manager


class TestScene1(Scene):
    def __init__(self):
        super().__init__("TestScene1")

    def update(self, dt: float):
        if input.mouseButtons["left"]:
            scene_manager.switch_scene(TestScene2())

    def render(self):
        self.display.fill(RED_MOTION2)


class TestScene2(Scene):
    def __init__(self):
        super().__init__("TestScene2")

    def update(self, dt: float):
        if input.mouseButtons["left"]:
            scene_manager.exit_scene()

    def render(self):
        self.display.fill(YELLOW_MOTION)
