import pygame

import src.assets as Assets
import src.input as input
from src.scenes.scene import Scene
from src.config import *
from src.ui_objects import *
from random import randint
from src.modules.subnetting.subnetting_objects import *


class SelectAreaScene(Scene):
    def __init__(self):
        super().__init__("SelectAreaScene")
        # Groups
        self.zonesGroup = self.new_group()
        self.draggableGroup = self.new_group()
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

        self.mask = Text((20, 110), "Mask", WHITE_MOTION)
        self.mask.centered = False
        self.maskIP = Text((100, 110), "255.255.255.", WHITE_MOTION)
        self.maskIP.centered = False
        self.maskBlank = Blank((180, 118), "mask")

        self.network = Text((20, 110), "Network", WHITE_MOTION)
        self.network.centered = False
        self.networkIp = Text((100, 110), "192.160.1.", WHITE_MOTION)
        self.networkIp.centered = False
        self.networkBlank = Blank((180, 118), "network")

        self.broadcast = Text((20, 125), "Broadcast", WHITE_MOTION)
        self.broadcast.centered = False
        self.broadcastIp = Text((100, 125), "192.160.2.", WHITE_MOTION)
        self.broadcastIp.centered = False
        self.broadcastBlank = Blank((180, 133), "broadcast")

        self.gateAway = Text((20, 140), "Gateaway", WHITE_MOTION)
        self.gateAway.centered = False
        self.gateAwayIp = Text((100, 140), "192.160.3.", WHITE_MOTION)
        self.gateAwayIp.centered = False
        self.gateAwayBlank = Blank((180, 148), "Gateaway")

        self.emptyBlank1 = Blank((220 - 5 + 90 / 4, 100), "empty1", True)
        self.emptyBlank2 = Blank((220 - 5 + 90 / 4, 115), "empty2", True)
        self.emptyBlank3 = Blank((220 - 5 + 90 / 4, 130), "empty3", True)
        self.emptyBlank4 = Blank((220 + 90 / 4 * 2, 100), "empty4", True)
        self.emptyBlank5 = Blank((220 + 90 / 4 * 2, 115), "empty5", True)
        self.emptyBlank6 = Blank((220 + 90 / 4 * 2, 130), "empty6", True)
        self.emptyBlank7 = Blank((220 + 6 + 90 / 4 * 3, 100), "empty7", True)
        self.emptyBlank8 = Blank((220 + 6 + 90 / 4 * 3, 115), "empty8", True)
        self.emptyBlank9 = Blank((220 + 6 + 90 / 4 * 3, 130), "empty9", True)

        self.blankGroup = self.new_group()
        self.blankGroup.add(self.networkBlank)
        self.blankGroup.add(self.broadcastBlank)
        self.blankGroup.add(self.gateAwayBlank)
        self.blankGroup.add(self.emptyBlank1)
        self.blankGroup.add(self.emptyBlank2)
        self.blankGroup.add(self.emptyBlank3)
        self.blankGroup.add(self.emptyBlank4)
        self.blankGroup.add(self.emptyBlank5)
        self.blankGroup.add(self.emptyBlank6)
        self.blankGroup.add(self.emptyBlank7)
        self.blankGroup.add(self.emptyBlank8)
        self.blankGroup.add(self.emptyBlank9)

        self.optionsGroup = self.new_group()
        self.option1 = Option(192, self.emptyBlank1)
        self.option2 = Option(1, self.emptyBlank2)
        self.option3 = Option(0, self.emptyBlank3)
        self.optionsGroup.add(self.option1)
        self.optionsGroup.add(self.option2)
        self.optionsGroup.add(self.option3)

        default_blanks = [blank for blank in self.blankGroup.sprites if blank.default]
        used_blanks = [option.blank for option in self.optionsGroup.sprites]
        self.emptyBlanks = [blank for blank in default_blanks if blank not in used_blanks]

        for i in range(len(self.emptyBlanks)):
            number = randint(0, 255)
            while str(number) in [option.number for option in self.optionsGroup.sprites]:
                number = randint(0, 255)

            self.optionsGroup.add(Option(number, self.emptyBlanks[i]))

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
        self.zonesGroup.add(self.mask)
        self.zonesGroup.add(self.maskIP)

        self.draggableGroup.add(self.network)
        self.draggableGroup.add(self.networkIp)
        self.draggableGroup.add(self.mask)
        self.draggableGroup.add(self.maskIP)
        self.draggableGroup.add(self.broadcast)
        self.draggableGroup.add(self.broadcastIp)
        self.draggableGroup.add(self.gateAway)
        self.draggableGroup.add(self.gateAwayIp)
        self.draggableGroup.add(self.hosts)
        self.draggableGroup.add(self.subnets)
        self.itemDragging = None
        self.draggingPosition = ""
        self.positionText = Text((35, 5), self.draggingPosition, WHITE_MOTION)
        self.zonesGroup.add(self.positionText)

        self.dragging = False
        self.ordering = False
        self.mouseOffsetX = 0
        self.mouseOffsetY = 0
        self.selectedOption: Option = None
        self.selectedBlank: Blank = None
        self.oldPosition = 0, 0

    def update(self) -> None:
        self.update_cursor()
        self.zonesGroup.update()
        self.optionsGroup.update()
        self.blankGroup.update()

        self.reorder()

        self.drag()

        if self.zone1.clicked():
            self.subnets.set_text(f"Subnets: {2}")
            self.hosts.set_text(f"Hosts: {4}")

        if input.keyboardKeys["SPACE"]:
            # for blank in self.blankGroup.sprites:
            #     blank: Blank
            #     if not blank.empty and not blank.default:
            #         option = next((option for option in self.optionsGroup.sprites if option.blank == blank))
            #         print(option.blank.name, option.number)
            for sprite in self.draggableGroup.sprites:
                if hasattr(sprite, "name"):
                    print(sprite.name, sprite.position)
                else:
                    print(sprite.text, sprite.position)

    def render(self) -> None:
        self.display.fill(BLUE_MOTION2)
        pygame.draw.rect(self.display, GRAY_MOTION, pygame.Rect(10, 80, 200, 90), border_radius=3)
        pygame.draw.rect(self.display, GRAY_MOTION, pygame.Rect(220, 80, 90, 90), border_radius=3)
        self.zonesGroup.render(self.display)
        self.blankGroup.render(self.display)
        self.optionsGroup.render(self.display)
        if self.selectedOption:
            self.selectedOption.render(self.display)

    def reorder(self):
        # Start dragging
        if not self.ordering and input.mouseButtons["left_hold"]:
            for sprite in self.draggableGroup.sprites:
                if sprite.rect.collidepoint(input.mousePosition):
                    self.ordering = True
                    self.itemDragging = sprite
                    self.mouseOffsetX = input.mousePosition.x - sprite.x
                    self.mouseOffsetY = input.mousePosition.y - sprite.y
                    break

        # On dragging
        if self.ordering:
            self.itemDragging.x = input.mousePosition.x - self.mouseOffsetX
            self.itemDragging.y = input.mousePosition.y - self.mouseOffsetY
            self.positionText.set_text(f'({str("%.1f" % self.itemDragging.x)}, {str("%.1f" % self.itemDragging.y)})')

        # End dragging
        if self.ordering and not input.mouseButtons["left_hold"]:
            self.selectedOption = None
            self.ordering = False
            self.positionText.set_text("")

    def drag(self):
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
                    break

        # On dragging
        if self.dragging:
            self.selectedOption.x = input.mousePosition.x - self.mouseOffsetX
            self.selectedOption.y = input.mousePosition.y - self.mouseOffsetY

            for blank in self.blankGroup.sprites:
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
            self.selectedOption = None
            self.dragging = False
