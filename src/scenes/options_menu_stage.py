from src.scenes.scene import Stage, StagedScene
from src.ui_objects import *
import src.time as time
import src.window as window
import src.input as input
from src.config import update_preferences


def format_size(size: tuple):
    return f"{size[0]} x {size[1]}"


class OptionsStage(Stage):
    def __init__(self, scene: StagedScene):
        super().__init__("optionsStage", scene)
        self.optionsTitle = GUIText((209, 61), "OPTIONS", 32, WHITE_MOTION, False, 0, self.sprites)
        self.optionsTitle.set_centered(False)
        self.topTitleLine = GUIImage((51, 54), assets.misc["doted_line"], self.sprites)
        self.topTitleLine.set_centered(False)

        self.bottomTitleLine = GUIImage((51, 99), assets.misc["doted_line"], self.sprites)
        self.bottomTitleLine.set_centered(False)

        self.sizes = [(960, 540), (1280, 720), (1920, 1080)]
        self.sizeIndex = 1
        self.displaySize = GUIText((250, 150), format_size(self.sizes[self.sizeIndex]), 32, BLUE_MOTION, False, 0,
                                   self.sprites)

        self.leftArrow = ArrowButton((96 + 70, 150), "right", self.sprites)
        self.rightArrow = ArrowButton((96 + 310 - 70, 150), "left", self.sprites)

        self.applyButton = TextButton("- APPLY -", (197, 200), self.sprites)

        self.topDescriptionLine = GUIImage((51, 246), assets.misc["doted_line"], self.sprites)
        self.topDescriptionLine.set_centered(False)

        self.bottomDescriptionLine = GUIImage((51, 290), assets.misc["doted_line"], self.sprites)
        self.bottomDescriptionLine.set_centered(False)

        description = "Changes the way the game looks! Or maybe it’s\njust the window size changer."
        self.description = GUIText((116, 255), description, 16, WHITE_MOTION, False, 0, self.sprites)
        self.description.set_centered(False)

        self.closeButton = ExitButton((110, 69), self.sprites)

        self.stageTimer = time.Timer(0.5)

    def update(self) -> None:
        self.update_groups()
        if self.leftArrow.released():
            self.sizeIndex -= 1
            if self.sizeIndex < 0:
                self.sizeIndex = len(self.sizes) - 1
            self.displaySize.text = format_size(self.sizes[self.sizeIndex])
        if self.rightArrow.released():
            self.sizeIndex += 1
            if self.sizeIndex > len(self.sizes) - 1:
                self.sizeIndex = 0
            self.displaySize.text = format_size(self.sizes[self.sizeIndex])

        if self.applyButton.released():
            pygame.display.set_mode(self.sizes[self.sizeIndex])
            window.width = self.sizes[self.sizeIndex][0]
            window.height = self.sizes[self.sizeIndex][1]

            update_preferences({"window_width": window.width,
                                "window_height": window.height})

        if self.closeButton.released() or input.keyboardKeys["ESC"]:
            self.scene.exit_stage()

    def render(self) -> None:
        self.render_groups()
