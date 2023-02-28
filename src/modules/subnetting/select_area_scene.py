import pygame

import src.assets as Assets
import src.input as input
from src.scenes.scene import Scene
from src.config import *
from src.ui_objects import *
from src.modules.subnetting.subnetting_objects import *


class SelectAreaScene(Scene):
    def __init__(self):
        super().__init__("SelectAreaScene")
        # Groups
        self.zonesGroup = self.new_group()
        self.dragAndDropGroup = self.new_group()
        self.dragAndDropGroup.active = False
        # Zones
        self.zone1 = Image((110, 40), assets.subnetting["house"])
        self.zone1.scale = 2
        self.zone1.interactive = True

        self.zone2 = Image((160, 40), assets.subnetting["house"])
        self.zone2.scale = 2
        self.zone2.interactive = True

        self.zone3 = Image((210, 40), assets.subnetting["house"])
        self.zone3.scale = 2
        self.zone3.interactive = True

        self.instruction = Text((160, 20), "Select the area for subnet", WHITE_MOTION)

        # Drag and Drop
        self.subnets = Text((10 + 200 / 3, 90), "Subnets", WHITE_MOTION)

        self.hosts = Text((10 + 200 / 3 * 2, 90), "Hosts", WHITE_MOTION)

        self.network = Text((20, 110), "Network", WHITE_MOTION)
        self.network.centered = False
        self.networkIp = Text((100, 110), "192.160.0.", WHITE_MOTION)
        self.networkIp.centered = False
        self.networkBlank = Blank((180, 118), "network")

        self.broadcast = Text((20, 125), "Broadcast", WHITE_MOTION)
        self.broadcast.centered = False
        self.broadcastIp = Text((100, 125), "192.160.0.", WHITE_MOTION)
        self.broadcastIp.centered = False
        self.broadcastBlank = Blank((180, 133), "broadcast")

        self.gateAway = Text((20, 140), "Gateaway", WHITE_MOTION)
        self.gateAway.centered = False
        self.gateAwayIp = Text((100, 140), "192.160.0.", WHITE_MOTION)
        self.gateAwayIp.centered = False
        self.gateAwayBlank = Blank((180, 148), "Gateaway")

        self.blankGroup = self.new_group()
        self.blankGroup.add(self.networkBlank)
        self.blankGroup.add(self.broadcastBlank)
        self.blankGroup.add(self.gateAwayBlank)

        self.optionsGroup = self.new_group()
        self.option = Option((230, 90), 192)
        self.option2 = Option((230, 110), 1)

        self.zonesGroup.add(self.zone1)
        self.zonesGroup.add(self.zone2)
        self.zonesGroup.add(self.zone3)
        self.zonesGroup.add(self.instruction)
        self.zonesGroup.add(self.network)
        self.zonesGroup.add(self.broadcast)
        self.zonesGroup.add(self.gateAway)
        self.zonesGroup.add(self.subnets)
        self.zonesGroup.add(self.hosts)
        self.zonesGroup.add(self.networkIp)
        self.zonesGroup.add(self.broadcastIp)
        self.zonesGroup.add(self.gateAwayIp)

        self.optionsGroup.add(self.option)
        self.optionsGroup.add(self.option2)

        self.dragging = False
        self.mouseOffsetX = 0
        self.mouseOffsetY = 0
        self.selectedOption = None
        self.selectedBlank = None
        self.oldPosition = 0, 0

    def update(self) -> None:
        self.update_cursor()
        self.zonesGroup.update()
        self.optionsGroup.update()
        self.blankGroup.update()

        self.drag()

        if self.zone1.clicked():
            self.subnets.set_text(f"Subnets: {2}")
            self.hosts.set_text(f"Hosts: {4}")

        # self.networkBlank.x = input.mousePosition.x
        # self.networkBlank.y = input.mousePosition.y
        #
        # if input.keyboardKeys["SPACE"]:
        #     print(self.networkBlank.x, self.networkBlank.y)

    def render(self) -> None:
        self.display.fill(BLUE_MOTION2)
        pygame.draw.rect(self.display, GRAY_MOTION, pygame.Rect(10, 80, 200, 90), border_radius=3)
        pygame.draw.rect(self.display, GRAY_MOTION, pygame.Rect(220, 80, 90, 90), border_radius=3)
        self.zonesGroup.render(self.display)
        self.blankGroup.render(self.display)
        self.optionsGroup.render(self.display)

    def drag(self):
        # Start dragging
        if not self.dragging and input.mouseButtons["left_hold"]:
            for option in self.optionsGroup.sprites:
                if option.rect.collidepoint(input.mousePosition):
                    self.dragging = True
                    self.selectedOption = option
                    self.selectedOption.shadowActive = False
                    self.mouseOffsetX = input.mousePosition.x - option.x
                    self.mouseOffsetY = input.mousePosition.y - option.y
                    self.oldPosition = option.x, option.y
                    break

        # On dragging
        if self.dragging:
            self.selectedOption.x = input.mousePosition.x - self.mouseOffsetX
            self.selectedOption.y = input.mousePosition.y - self.mouseOffsetY

            for blank in self.blankGroup.sprites:
                if blank.rect.collidepoint(input.mousePosition):
                    self.selectedBlank = blank
                    break
                self.selectedBlank = None

        # selected_index = self.cables.index(self.selectedOption)
        # for cable in self.cables:
        #     if cable == self.selectedOption:
        #         continue
        #     if cable.rect.collidepoint(input.mousePosition):
        #         swap_index = self.cables.index(cable)
        #         cable.y = self.cableYPositions[selected_index]
        #         self.cables[selected_index], self.cables[swap_index] = \
        #             self.cables[swap_index], self.cables[selected_index]

        # End dragging
        if self.dragging and not input.mouseButtons["left_hold"]:
            # self.selectedOption.y = self.cableYPositions[self.cables.index(self.selectedOption)]
            if self.selectedBlank and self.selectedBlank.empty:
                self.selectedBlank.empty = False
                self.selectedOption.x, self.selectedOption.y = self.selectedBlank.x, self.selectedBlank.y
            else:
                self.selectedOption.x, self.selectedOption.y = self.oldPosition

            self.selectedOption.shadowActive = True
            self.selectedOption = None
            self.dragging = False
            # self.check_cable_order()
