import os
import pygame
from src.load import load_json
from random import choice, randint, shuffle
from src.scenes.scene import Scene
from src.config import *
from src.ui_objects import *
from src.modules.subnetting.subnetting_objects import *
import src.scenes.scene_manager as scene_manager
import src.input as input


class Subnet:
    def __init__(self, name: str, data: dict):
        self.name = name
        self.id: str = data["id"]
        self.broadcast: str = data["broadcast"]
        self.firstUsable: str = data["first"]

    def __repr__(self):
        return f"{self.name}: {self.id}"


class CustomMaskProblem:
    def __init__(self, exercise_file=choice(os.listdir(SUBNETTING_EXERCISES_PATH))):
        self.data: dict = load_json(f"{SUBNETTING_EXERCISES_PATH}/{exercise_file}")
        self.ip: str = self.data["ip"]
        self.ipClass: str = self.data["class"]
        self.defaultMask: str = self.data["default_mask"]
        self.subnetsNeeded: int = self.data["subnets_needed"]
        self.customMask: str = self.data["custom_mask"]
        self.subnets: list[Subnet] = [Subnet(name, data) for name, data in self.data["subnets"].items()]
        self.blanks = self.defaultMask.count("0")
        self.correctAnswers = self.customMask.split(".")[4 - self.blanks:]
        print(self.customMask, self.blanks, self.correctAnswers)


class IpMaskScene(Scene):
    def __init__(self):
        super().__init__("IpMaskScene")
        # ---------- Data ----------
        self.customData = CustomMaskProblem()
        self.problemFile = choice(os.listdir(SUBNETTING_EXERCISES_PATH))
        self.problemData = load_json(f"{SUBNETTING_EXERCISES_PATH}/{self.problemFile}")
        mask_count = self.problemData["default_mask"].count("0")
        mask_split: list = self.problemData["custom_mask"].split(".")
        self.correctAnswers = mask_split[4 - mask_count:]
        # ---------- Groups ----------
        self.textGroup = self.new_group()
        self.classButtonsGroup = self.new_group()
        self.mapGroup = self.new_group()
        self.blanksGroup = self.new_group()
        self.optionsGroup = self.new_group()
        # ---------- Text ----------
        self.ipText = Text((160, 10), f"Ip: {self.problemData['ip']}", WHITE_MOTION, centered=False)
        self.defaultMaskText = Text((160, 25), f"Default mask: {self.problemData['default_mask']}", WHITE_MOTION,
                                    centered=False)
        self.customMaskTitle = Text((160, 60), f"Custom mask: {self.problemData['custom_mask']}", WHITE_MOTION,
                                    centered=False)
        self.textGroup.add(self.ipText)
        self.textGroup.add(self.defaultMaskText)
        self.textGroup.add(self.customMaskTitle)
        # ---------- Blanks ----------
        # Exercise blanks
        padding = 50
        blank_initial = 320 - mask_count * padding
        for blank in range(mask_count):
            x_position = blank_initial + padding * blank
            y_position = self.customMaskTitle.rect.centery
            self.blanksGroup.add(Blank((x_position, y_position), f"custom_{blank + 1}"))
        # Options blanks
        empty_blanks = []
        rows = 2
        columns = 3
        x_positions = [160 + 30 * x for x in range(columns)]
        y_positions = [90 + 30 * x for x in range(rows)]
        counter = 0
        for y in range(rows):
            for x in range(columns):
                counter += 1
                blank = Blank((x_positions[x], y_positions[y]), f"blank_{counter}", True)
                empty_blanks.append(blank)
                self.blanksGroup.add(blank)
        # ---------- Options ----------
        self.shuffleAnswers = self.correctAnswers.copy()
        last_options = 6 - len(self.correctAnswers)
        for index in range(last_options):
            self.shuffleAnswers.append(randint(0, 255))
        shuffle(self.shuffleAnswers)

        for index, option in enumerate(self.shuffleAnswers):
            self.optionsGroup.add(Option(option, empty_blanks[index]))

        # ---------- Buttons ----------
        self.classAButton = Button((220, 50), "A", "blue_small")
        self.classBButton = Button((240, 50), "B", "blue_small")
        self.classCButton = Button((260, 50), "C", "blue_small")

        self.reload = Button((20, 20), "Reload", "blue_large")

        self.classButtonsGroup.add(self.classAButton)
        self.classButtonsGroup.add(self.classBButton)
        self.classButtonsGroup.add(self.classCButton)
        self.classButtonsGroup.add(self.reload)
        # ---------- Map ----------
        self.mapGrid = [[0] * 7 for i in range(8)]
        for subnet in range(self.problemData["subnets_needed"]):
            x_cord = randint(0, 6)
            y_cord = randint(0, 7)

            while self.mapGrid[y_cord][x_cord] != 0:
                x_cord = randint(0, 2)
                y_cord = randint(0, 3)
            self.mapGrid[y_cord][x_cord] = subnet + 1

        map_surface = pygame.Surface((140, 160))
        map_surface.fill(BLUE_MOTION2)
        self.mapBackground = Image((80, 90), map_surface)

        self.mapGroup.add(self.mapBackground)

        for y, row in enumerate(self.mapGrid):
            for x, subnet in enumerate(row):
                if subnet != 0:
                    x_cord = 20 + x * 20
                    y_cord = 20 + y * 20

                    self.mapGroup.add(Image((x_cord, y_cord), assets.subnetting["house"]))
        # ---------- Drag ----------
        self.dragging = False
        self.mouseOffsetX = 0
        self.mouseOffsetY = 0
        self.oldPosition = 0, 0
        self.selectedBlank: Blank = None
        self.selectedOption: Option = None

    def drag(self):
        if not self.optionsGroup.active:
            return
        # Start dragging
        if not self.dragging and input.mouseButtons["left_hold"]:
            for option in self.optionsGroup.sprites:
                option: Option
                if option.rect.collidepoint(input.mousePosition):
                    self.dragging = True
                    self.selectedOption = option
                    self.selectedOption.shadowActive = False
                    self.mouseOffsetX = input.mousePosition.x - option.x
                    self.mouseOffsetY = input.mousePosition.y - option.y
                    self.oldPosition = option.x, option.y
                    self.selectedOption.dragging = True
                    break

        # On dragging
        if self.dragging:
            self.selectedOption.x = input.mousePosition.x - self.mouseOffsetX
            self.selectedOption.y = input.mousePosition.y - self.mouseOffsetY

            for blank in self.blanksGroup.sprites:
                blank: Blank
                if blank.rect.collidepoint(input.mousePosition):
                    self.selectedBlank = blank
                    break
                self.selectedBlank = None

        # End dragging
        if self.dragging and not input.mouseButtons["left_hold"]:
            if self.selectedBlank:

                option = next((option for option in self.optionsGroup.sprites if option.blank == self.selectedBlank),
                              None)
                if option:
                    option.blank = self.selectedOption.blank
                else:
                    self.selectedOption.blank.empty = True
                self.selectedOption.blank = self.selectedBlank
                self.selectedBlank.empty = False

            self.selectedOption.shadowActive = True
            self.selectedOption.dragging = False
            self.selectedOption = None
            self.dragging = False

    def update(self) -> None:
        self.update_cursor()
        self.update_groups()

        self.drag()

        if self.reload.released():
            scene_manager.swap_scene(self, IpMaskScene())

    def render(self) -> None:
        self.display.fill(YELLOW_MOTION)
        self.render_groups()
