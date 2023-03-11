import pygame
import src.input as input
import src.scenes.scene_manager as scene_manager
from src.scenes.scene import Scene
from src.ui_objects import *
from src.ui_objects import Image
import src.time as Time


class CrimpCableScene(Scene):
    def __init__(self, cable_type: str):
        super().__init__("crimpCableScene")
        pygame.mouse.set_visible(False)
        self.cableType = cable_type
        self.crimpGroup = self.new_group()
        self.colorBar = Image((160, 20), assets.misc["colorBar"])
        self.indicator = Image((103, 16), assets.misc["indicator"])
        self.crimpGroup.add(self.colorBar)
        self.crimpGroup.add(self.indicator)
        self.movement = 100
        self.quality = None
        self.cablePopUpGroup = self.new_group()
        self.cableNameText = Text((160, 100), "", WHITE_MOTION)
        self.cableDoneText = Text((160, 115), "done!", WHITE_MOTION)
        self.popUpBackground = Image((160, 90), pygame.transform.scale_by(assets.cables["pop_up_cables"], 2))
        self.cablePopUpGroup.add(self.popUpBackground)
        self.cablePopUpGroup.add(self.cableNameText)
        self.cablePopUpGroup.add(self.cableDoneText)
        self.cablePopUpGroup.active = False
        self.timer = Time.Timer(3)

    def update(self) -> None:
        # ---------- Indicator movement ----------
        if not self.quality:
            self.indicator.x += Time.dt * self.movement

            if self.indicator.x > 215:
                self.indicator.x = 215
                self.movement *= -1

            if self.indicator.x < 104:
                self.indicator.x = 104
                self.movement *= -1

        # ---------- Crimp Input ----------
        if input.keyboardKeys["SPACE"] and not self.quality:
            color = self.colorBar.image.get_at((int(self.indicator.x - 103), 9))
            if color == pygame.Color(GREEN_MOTION):
                self.quality = 3
                self.cablePopUpGroup.add(Image((136 + 48 / 4, 70 + 48 / 4), assets.cables["star"]))
                self.cablePopUpGroup.add(Image((136 + 48 / 4 * 2, 70 + 48 / 4), assets.cables["star"]))
                self.cablePopUpGroup.add(Image((136 + 48 / 4 * 3, 70 + 48 / 4), assets.cables["star"]))
            elif color == pygame.Color(YELLOW_MOTION):
                self.quality = 2
                self.cablePopUpGroup.add(Image((136 + 48 / 3, 70 + 48 / 4), assets.cables["star"]))
                self.cablePopUpGroup.add(Image((136 + 48 / 3 * 2, 70 + 48 / 4), assets.cables["star"]))
            elif color == pygame.Color(RED_MOTION2):
                self.quality = 1
                self.cablePopUpGroup.add(Image((136 + 24, 70 + 48 / 4), assets.cables["star"]))
            self.crimpGroup.active = False
            self.timer.start()

        if self.quality:
            self.cablePopUpGroup.active = True
            self.cableNameText.set_text(f"Cable 568-{self.cableType}")
            self.timer.update()
            if self.timer.done:
                pygame.mouse.set_visible(True)
                scene_manager.exit_scene()

    def render(self) -> None:
        self.display.blit(assets.backgrounds["table"], (0, 0))
        self.display.blit(assets.effects["crt"], (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        self.crimpGroup.render(self.display)
        self.cablePopUpGroup.render(self.display)
