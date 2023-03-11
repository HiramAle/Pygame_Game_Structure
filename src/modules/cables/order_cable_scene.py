import pygame
import src.input as input
from src.scenes.scene import Scene
from src.ui_objects import *
from src.modules.cables.cable_objects import Cable
from src.modules.cables.crimp_cable_scene import CrimpCableScene
from random import choice, shuffle
import src.scenes.scene_manager as scene_manager


class OrderCableScene(Scene):
    def __init__(self):
        super().__init__("orderCableScene")
        pygame.mouse.set_visible(True)
        self.cables = []
        self.cableYPositions = []
        self.selectedCable = None
        self.dragging = False
        self.mouseOffset = 0
        self.stage = "ordering"
        self.cableSurface = pygame.Surface((320, 180))
        self.cableSurface.set_colorkey((0, 0, 0))
        self.animationDone = False
        self.animationSpeed = 5
        self.cableSprites = self.new_group()
        self.instructionsGroup = self.new_group()
        self.buttonGroup = self.new_group()
        self.readyButton = SquareButton((280, 100), "check")
        self.buttonGroup.add(self.readyButton)
        self.buttonGroup.active = False
        self.ordered = False
        self.cableCoverForeground = Image((30, 90), assets.cables["cable_cover_top_v2"])
        # self.cableCoverForeground.scale = 4
        self.cableCoverBackground = Image((111, 90), assets.cables["cable_cover_down_v2"])
        # self.cableCoverBackground.scale = 4
        mask = pygame.mask.from_surface(self.cableCoverForeground.image)
        cable_shadow_surface = mask.to_surface(unsetcolor=(0, 0, 0, 0), setcolor=DARK_BLACK_MOTION)
        cable_shadow_surface.set_colorkey((0, 0, 0))
        cable_shadow_surface.set_alpha(90)
        self.cableCoverShadow = Image((14, 93), cable_shadow_surface)

        # Cable Standards
        self.standardName = choice(list(CABLE_STANDARDS.keys()))
        self.standard = CABLE_STANDARDS[self.standardName].copy()
        self.instruction = Text((280, 80), f"568-{self.standardName}", WHITE_MOTION)
        self.instructionsGroup.add(self.instruction)
        shuffled_cables = self.standard.copy()
        # shuffle(shuffled_cables)

        self.cableSprites.add(self.cableCoverShadow)
        self.cableSprites.add(self.cableCoverBackground)

        for i, cableName in enumerate(shuffled_cables):
            position = (int(self.display.get_width() / 2), 20 + (i * 20))
            self.cableYPositions.append(position[1])
            color = cableName.split("_")[1]
            cable = Cable(position, color, cableName)
            self.cables.append(cable)
            self.cableSprites.add(cable)

        self.cableSprites.add(self.cableCoverForeground)

    def check_cable_order(self):
        actual_order = [cable.name for cable in self.cables]
        self.ordered = (actual_order == self.standard)

    def drag(self):
        # Start dragging
        if not self.dragging and input.mouseButtons["left_hold"]:
            for cable in self.cables:
                if cable.rect.collidepoint(input.mousePosition):
                    self.dragging = True
                    self.selectedCable = cable
                    self.selectedCable.shadowActive = False
                    self.mouseOffset = input.mousePosition.y - cable.y
                    break

        # On dragging
        if self.dragging:
            self.selectedCable.y = input.mousePosition.y - self.mouseOffset
            selected_index = self.cables.index(self.selectedCable)
            for cable in self.cables:
                if cable == self.selectedCable:
                    continue
                if cable.rect.collidepoint(input.mousePosition):
                    swap_index = self.cables.index(cable)
                    cable.y = self.cableYPositions[selected_index]
                    self.cables[selected_index], self.cables[swap_index] = \
                        self.cables[swap_index], self.cables[selected_index]

        # End dragging
        if self.dragging and not input.mouseButtons["left_hold"]:
            self.selectedCable.y = self.cableYPositions[self.cables.index(self.selectedCable)]
            self.selectedCable.shadowActive = True
            self.selectedCable = None
            self.dragging = False
            self.check_cable_order()

    def update(self):
        self.update_cursor()
        self.cableSprites.update()
        self.buttonGroup.update()
        self.drag()
        if self.readyButton.clicked():
            scene_manager.swap_scene(self, CrimpCableScene(self.standardName))

        # self.cableCoverBackground.x = input.mousePosition.x
        # self.cableCoverBackground.y = input.mousePosition.y
        #
        # if input.keyboardKeys["SPACE"]:
        #     print(self.cableCoverBackground.x, self.cableCoverBackground.y)

    def render(self):
        self.display.blit(assets.backgrounds["table"], (0, 0))
        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        if self.dragging:
            self.selectedCable.render(self.display)

        if self.ordered and not self.buttonGroup.active:
            self.buttonGroup.active = True
        if not self.ordered and self.buttonGroup.active:
            self.buttonGroup.active = False

        self.cableSprites.render(self.display)
        self.buttonGroup.render(self.display)

        self.instructionsGroup.render(self.display)
