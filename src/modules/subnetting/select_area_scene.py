import pygame
from random import shuffle
import src.assets as Assets
import src.input as input
from src.scenes.scene import Scene
from src.config import *
from src.ui_objects import *
from random import randint
from src.modules.subnetting.subnetting_objects import *
from src.load import load_json
from src.scenes.scene_manager import *


class SelectAreaScene(Scene):
    def __init__(self):
        super().__init__("SelectAreaScene")
        self.data = load_json("data/scenes/subnetting/1.json")
        # ---------- Groups ----------
        self.zonesGroup = self.new_group()
        self.draggableGroup = self.new_group()
        self.blankGroup = self.new_group()
        self.optionsGroup = self.new_group()
        self.buttonsGroup = self.new_group()
        self.completeGroup = self.new_group()
        self.dataGroup = self.new_group()
        # ---------- Instructions ----------
        self.instruction = Text((160, 10), "Select the area to subnet", WHITE_MOTION)
        self.dataGroup.add(self.instruction)
        # ---------- Load zones from json ----------
        number_of_zones = len(self.data.keys())
        zone_x_initial = 320 / (number_of_zones + 1)
        for index, zone in enumerate(self.data.keys()):
            zone_position = zone_x_initial * (index + 1), 40
            zone_sprite = Zone(zone_position, assets.subnetting["house"], zone)
            self.zonesGroup.add(zone_sprite)
        # ---------- Problem data ----------
        # Subnets
        self.subnets = Text((18, 110), "Subnets: __", WHITE_MOTION)
        self.subnets._centered = False
        self.dataGroup.add(self.subnets)
        # Hosts
        self.hosts = Text((100, 110), "Hosts: __", WHITE_MOTION)
        self.hosts._centered = False
        self.dataGroup.add(self.hosts)
        # Mask
        self.mask = Text((18, 95), "Mask", WHITE_MOTION)
        self.mask._centered = False
        self.maskIp = Text((88, 95), "___.___.___.", WHITE_MOTION)
        self.maskIp._centered = False
        self.dataGroup.add(self.mask)
        self.dataGroup.add(self.maskIp)
        # Network
        self.network = Text((18, 125), "Network", WHITE_MOTION)
        self.network._centered = False
        self.networkIp = Text((100, 125), "___.___.___.", WHITE_MOTION)
        self.networkIp._centered = False
        self.dataGroup.add(self.network)
        self.dataGroup.add(self.networkIp)
        # Broadcast
        self.broadcast = Text((18, 140), "Broadcast", WHITE_MOTION)
        self.broadcast._centered = False
        self.broadcastIp = Text((100, 140), "___.___.___.", WHITE_MOTION)
        self.broadcastIp._centered = False
        self.dataGroup.add(self.broadcast)
        self.dataGroup.add(self.broadcastIp)
        # Gateaway
        self.gateAway = Text((18, 155), "Gateaway", WHITE_MOTION)
        self.gateAway._centered = False
        self.gateAwayIp = Text((100, 155), "___.___.___.", WHITE_MOTION)
        self.gateAwayIp._centered = False
        self.dataGroup.add(self.gateAway)
        self.dataGroup.add(self.gateAwayIp)
        # ---------- Options Blanks ----------
        # Options blanks
        blanks_column_positions = [220 - 5 + 90 / 4, 220 + 90 / 4 * 2, 220 + 6 + 90 / 4 * 3]
        blanks_row_positions = [115, 130, 145, 160]
        counter = 1
        for y in range(4):
            for x in range(3):
                position = blanks_column_positions[x], blanks_row_positions[y]
                print(f"blank_{counter}", position)
                self.blankGroup.add(Blank(position, f"blank_{counter}", True))
                counter += 1
        # Answers blanks
        self.maskBlank = Blank((180, self.mask.rect.centery), "mask")
        self.networkBlank = Blank((180, self.network.rect.centery), "network")
        self.broadcastBlank = Blank((180, self.broadcast.rect.centery), "broadcast")
        self.gateAwayBlank = Blank((180, self.gateAway.rect.centery), "Gateaway")
        self.answerBlanks = [self.maskBlank, self.networkBlank, self.broadcastBlank, self.gateAwayBlank]

        self.blankGroup.add(self.maskBlank)
        self.blankGroup.add(self.networkBlank)
        self.blankGroup.add(self.broadcastBlank)
        self.blankGroup.add(self.gateAwayBlank)
        # ---------- Buttons ----------
        self.back = SquareButton((15, 15), "back")
        self.complete = SquareButton((300, 15), "check")

        self.buttonsGroup.add(self.back)
        self.completeGroup.add(self.complete)
        self.completeGroup.active = False
        # ---------- Dragging data ----------
        self.dragging = False
        self.mouseOffsetX = 0
        self.mouseOffsetY = 0
        self.selectedOption: Option = None
        self.selectedBlank: Blank = None
        self.oldPosition = 0, 0
        # ---------- Zone selecting ----------
        self.activeZone: Zone = None
        # ---------- Answer review ----------
        self.correctAnswers = []
        self.userAnswers = []

    def set_options(self):
        self.optionsGroup.sprites = []
        options = self.correctAnswers.copy()

        for index in range(8):
            number = randint(0, 255)
            while number in options:
                number = randint(0, 155)
            options.append(number)

        shuffle(options)

        for index, option in enumerate(options):
            blanks = [blank for blank in self.blankGroup.sprites if blank.default]
            self.optionsGroup.add(Option(int(option), blanks[index]))

    def set_zone_data(self, zone_name: str):
        zone_data = self.data[zone_name]
        mask_ip = zone_data["mask"]
        network_ip = zone_data["network"]
        broadcast_ip = zone_data["broadcast"]
        gate_away_ip = zone_data["router"]
        subnets = zone_data["subnets"]
        hosts = zone_data["hosts"]

        mask = mask_ip[:mask_ip.rfind(".") + 1]
        network = network_ip[:network_ip.rfind(".") + 1]
        broadcast = broadcast_ip[:broadcast_ip.rfind(".") + 1]
        gate_away = gate_away_ip[:gate_away_ip.rfind(".") + 1]

        self.correctAnswers = [mask_ip[mask_ip.rfind(".") + 1:], network_ip[network_ip.rfind(".") + 1:],
                               broadcast_ip[broadcast_ip.rfind(".") + 1:], gate_away_ip[gate_away_ip.rfind(".") + 1:]]

        self.subnets.set_text(self.subnets._text[:-2] + str(subnets))
        self.hosts.set_text(self.hosts._text[:-2] + str(hosts))
        self.maskIp.set_text(mask)
        self.networkIp.set_text(network)
        self.broadcastIp.set_text(broadcast)
        self.gateAwayIp.set_text(gate_away)

    def set_zone(self):
        for zone in self.zonesGroup.sprites:
            zone: Zone
            if zone.clicked():
                if self.activeZone:
                    self.activeZone.selected = False
                self.activeZone = zone
                self.activeZone.selected = True
                self.set_zone_data(self.activeZone.name)
                self.set_options()
                break

    def get_user_answers(self):
        if self.all_blanks_filled():
            self.completeGroup.active = True
            self.userAnswers = [next(option.number for option in self.optionsGroup.sprites if option.blank == blank)
                                for blank in self.answerBlanks]

    def compare_answers(self):
        if self.userAnswers == self.correctAnswers:
            print("Correct")
        else:
            print("Incorrect")

    def all_blanks_filled(self) -> bool:
        if not any(blank.empty for blank in self.answerBlanks):
            if not self.completeGroup.active:
                self.completeGroup.active = True
            return True
        if self.completeGroup.active:
            self.completeGroup.active = False
        return False

    def update(self) -> None:
        self.update_cursor()
        self.zonesGroup.update()
        self.optionsGroup.update()
        self.blankGroup.update()
        self.buttonsGroup.update()
        self.dataGroup.update()
        self.completeGroup.update()
        self.drag()
        self.set_zone()

        self.get_user_answers()

        if self.back.released():
            exit_scene()

        if self.complete.released():
            self.get_user_answers()
            self.compare_answers()

        # if input.keyboardKeys["SPACE"]:
        #     for blank in self.blankGroup.sprites:
        #         blank: Blank
        #         if not blank.empty and not blank.default:
        #             option = next((option for option in self.optionsGroup.sprites if option.blank == blank))
        #             print(option.blank.name, option.number)

    def render(self) -> None:
        self.display.fill(BLUE_MOTION2)
        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        pygame.draw.rect(self.display, YELLOW_MOTION, pygame.Rect(10, 95, 200, 75), border_radius=3)
        pygame.draw.rect(self.display, YELLOW_MOTION, pygame.Rect(220, 105, 90, 65), border_radius=3)
        self.zonesGroup.render(self.display)
        self.blankGroup.render(self.display)
        self.optionsGroup.render(self.display)
        self.completeGroup.render(self.display)
        if self.selectedOption:
            self.selectedOption.render(self.display)
        self.buttonsGroup.render(self.display)
        self.dataGroup.render(self.display)

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
            self.selectedOption.dragging = False
            self.selectedOption = None
            self.dragging = False
