import pygame
import src.input as input
from src.scenes.scene import Scene
from src.config import *
from src.ui_objects import SimpleButton
from src.modules.cable.cable_objects import Cable


class CableScene(Scene):
    def __init__(self):
        super().__init__("CableScene")
        pygame.mouse.set_visible(True)
        self.cables = []
        self.cableYPositions = []
        self.selectedCable = None
        self.dragging = False
        self.mouseOffset = 0
        self.readyButton = SimpleButton((260, 90), "Ready")
        self.add_sprites(self.readyButton)
        self.stage = "ordering"
        self.cableSurface = pygame.Surface((320, 180))
        self.cableSurface.set_colorkey((0, 0, 0))
        self.animationDone = False
        self.animationSpeed = 5

        for i, cableName in enumerate(CABLES):
            position = (int(self.display.get_width() / 2), 20 + (i * 20))
            self.cableYPositions.append(position[1])
            color = cableName.split("_")[1]
            cable = Cable(position, color, cableName)
            self.cables.append(cable)
            self.add_sprites(cable)

    def drag(self):
        # Start dragging
        if not self.dragging and input.mouseButtons["left_hold"]:
            for cable in self.cables:
                if cable.rect.collidepoint(input.mousePosition):
                    self.dragging = True
                    self.selectedCable = cable
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
            self.selectedCable = None
            self.dragging = False

    def update(self, dt: float):
        super().update(dt)
        match self.stage:
            case "ordering":
                self.drag()
                if self.readyButton.clicked():
                    self.stage = "active_reload"
            case "active_reload":
                ...
        self.update_sprites(dt)

    def render(self):
        self.display.fill(GREEN_MOTION)
        self.render_sprites()
        match self.stage:
            case "ordering":
                if self.dragging:
                    self.selectedCable.render(self.display)
                pygame.draw.rect(self.display, BLUE_MOTION2, pygame.Rect(0, 5, 120, 170))

