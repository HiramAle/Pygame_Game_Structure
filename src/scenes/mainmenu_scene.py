import pygame

import src.input as input
import src.scenes.scene_manager as scene_manager
import src.window as Window
from src.scenes.scene import Scene, StagedScene
from src.scenes.main_menu_stage import MainStage
from random import randint, choice
# from src.modules.cables.order_cable_scene import OrderCableScene
# from src.scenes.game_selector_scene import GameSelectorScene
from src.commons import sin_wave
from src.ui_objects import *
import src.time as time
import src.window as window


class Cloud(Sprite):
    def __init__(self, position: tuple, *groups):
        super().__init__("cloud", position, assets.misc["cloud"], *groups)
        self.speed = randint(10, 15)

    def update(self):
        self.x += self.speed * time.dt
        if self.x > 700:
            self.kill()


class CloudGenerator(Position):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.cloudGroup = SpriteGroup()
        self.timer = time.Timer(4)
        self.timer.start()

    def update(self):
        self.cloudGroup.update()
        if self.timer.update():
            self.timer.start()
            self.cloudGroup.add(Cloud((self.x, randint(0, 140)), self.cloudGroup))

    def render(self, display: pygame.Surface):
        self.cloudGroup.render(display)


class RouterLed(Sprite):
    def __init__(self, position: tuple, *groups: SpriteGroup):
        super().__init__("routerLed", position, pygame.Surface((4, 4)), *groups)
        self.colorOn = "#7eb55d"
        self.colorOff = "#474b75"
        self.image.fill(choice([self.colorOn, self.colorOff]))
        self.timer = time.Timer(randint(1, 2))
        self.timer.start()
        self.set_centered(False)

    def update(self):
        self.timer.update()
        if self.timer.done:
            self.timer = time.Timer(randint(1, 2))
            self.timer.start()
            self.image.fill(choice([self.colorOn, self.colorOff]))


class MainMenu(StagedScene):
    def __init__(self):
        super().__init__("MainMenu")
        pygame.mouse.set_visible(True)
        # ---------- Main Menu ----------
        self.screenPadding = 96
        self.screenWidth = 310
        # Groups
        self.ledsGroup = self.new_group()
        # Computer
        self.computerForeground = GUIImage((0, 0), assets.backgrounds["main_menu"])
        self.computerForeground.set_centered(False)
        # Clouds
        self.sky = GUIImage((0, 0), assets.backgrounds["sky"])
        self.sky.set_centered(False)
        self.cloudGenerator = CloudGenerator((400, 60))
        # Computer background
        computer_bg = pygame.Surface((310, 240))
        computer_bg.fill(BLACK_MOTION)
        self.computerBackground = GUIImage((96, 52), computer_bg)
        self.computerBackground.set_centered(False)
        # Crt Effect
        crt_image = pygame.Surface((310, 240))
        crt_image.blit(assets.effects["crt"], (0, 0))
        self.crtEffect = GUIImage((96, 52), crt_image)
        self.crtEffect.set_centered(False)
        # Router leds
        self.routerLed1 = RouterLed((494, 272), self.ledsGroup)
        self.routerLed2 = RouterLed((500, 272), self.ledsGroup)
        self.routerLed3 = RouterLed((506, 272), self.ledsGroup)
        # ---------- Options Menu ----------

        self.set_stage(MainStage(self))

    def update(self):
        self.update_cursor()
        self.cloudGenerator.update()
        self.ledsGroup.update()
        self.update_stage()

    def render(self):
        self.sky.render(self.display)
        self.cloudGenerator.render(self.display)
        self.computerBackground.render(self.display)
        self.render_stage()
        self.crtEffect.render(self.display, blend=pygame.BLEND_RGBA_MULT)
        self.computerForeground.render(self.display)
        self.ledsGroup.render(self.display)
