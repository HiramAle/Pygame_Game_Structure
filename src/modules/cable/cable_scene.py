import pygame
import numpy as np

from src.scenes.scene import Scene, SceneManager
from src.config import Config
from src.modules.cable.cable_objects import Cable
from src.ui_objects import SimpleButton


class CableScene(Scene):
    def __init__(self, manager: SceneManager):
        super().__init__(manager)
        pygame.mouse.set_visible(True)
        self.cables = []
        self.cableYPositions = []
        self.selectedCable = None
        self.dragging = False
        self.mouseOffset = 0
        self.readyButton = SimpleButton((260, 90), "Ready")
        self.cableDone = False
        self.cableSurface = pygame.Surface((320, 180))
        self.cableSurface.set_colorkey((0, 0, 0))
        self.animationDone = False
        self.animationSpeed = 5

        for i, cableName in enumerate(Config.CABLES):
            position = (int(self.display.get_width() / 2), 20 + (i * 20))
            self.cableYPositions.append(position[1])
            color = list(np.random.choice(range(256), size=3))
            self.cables.append(Cable(position, color))

    def update_cursor(self):
        if self.dragging or self.readyButton.clicked(self.input.mousePosition, self.input.mouseButtons["left_hold"]):
            self.set_cursor("grab")
            return

        if not self.cableDone:
            if any([cable.rect.collidepoint(self.input.mousePosition) for cable in self.cables]) or self.readyButton.hover(
                    self.input.mousePosition):
                self.set_cursor("hand")
            else:
                self.set_cursor("arrow")

    def drag(self):
        # Start dragging
        if not self.dragging and self.input.mouseButtons["left_hold"]:
            for cable in self.cables:
                if cable.rect.collidepoint(self.input.mousePosition):
                    self.dragging = True
                    self.selectedCable = cable
                    self.mouseOffset = self.input.mousePosition.y - cable.y
                    break

        # On dragging
        if self.dragging:
            self.selectedCable.y = self.input.mousePosition.y - self.mouseOffset
            selected_index = self.cables.index(self.selectedCable)
            for cable in self.cables:
                if cable == self.selectedCable:
                    continue
                if cable.rect.collidepoint(self.input.mousePosition):
                    swap_index = self.cables.index(cable)
                    cable.y = self.cableYPositions[selected_index]
                    self.cables[selected_index], self.cables[swap_index] = \
                        self.cables[swap_index], self.cables[selected_index]

        # End dragging
        if self.dragging and not self.input.mouseButtons["left_hold"]:
            self.selectedCable.y = self.cableYPositions[self.cables.index(self.selectedCable)]
            self.selectedCable = None
            self.dragging = False

    def update(self, dt: float):
        super().update(dt)
        if not self.cableDone:
            self.drag()
        self.update_cursor()

        if self.readyButton.clicked(self.input.mousePosition, self.input.mouseButtons["left"]):
            print(self.cables)
            self.cableDone = True


        for cable in self.cables:
            cable.update(dt)
        self.readyButton.update(dt)

    def render(self):
        self.display.fill(Config.GREEN_MOTION)
        if not self.cableDone:
            for cable in self.cables:
                cable.render(self.display)

            if self.dragging:
                self.selectedCable.render(self.display)

            self.readyButton.render(self.display)

            pygame.draw.rect(self.display, Config.BLUE_MOTION2, pygame.Rect(0, 5, 120, 170))

        else:
            self.set_cursor("arrow")
            # if not self.animationDone:
            #     self.cableSurface = pygame.transform.scale(self.cableSurface, (
            #     self.cableSurface.get_height() / 0.2, self.cableSurface.get_width() / 0.2))
            #
            #     if self.cableSurface.get_size() == (self.display.get_width() / 2, self.display.get_height() / 2):
            #         self.animationDone = True

            for cable in self.cables:
                cable.render(self.cableSurface)

            if self.dragging:
                self.selectedCable.render(self.cableSurface)
            self.display.blit(pygame.transform.scale_by(self.cableSurface, 0.5), (60, 45))
            pygame.draw.rect(self.display, Config.BLUE_MOTION2, pygame.Rect(0, 47.5, 120, 170/2))
