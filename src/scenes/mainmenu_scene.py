import pygame

import src.input as input
import src.scenes.scene_manager as scene_manager
import src.window as Window
from src.scenes.scene import Scene
from random import randint, choice
# from src.modules.cables.order_cable_scene import OrderCableScene
# from src.scenes.game_selector_scene import GameSelectorScene
from src.commons import sin_wave
from src.ui_objects import *
import src.time as time


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
        self.timer.update()
        if self.timer.done:
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


class Option(Sprite):
    def __init__(self, option: str, position: tuple, *groups: SpriteGroup):
        super().__init__(f"option_{option}", position, pygame.Surface((310, 30)), *groups)
        self.image.fill(BLACK_MOTION)
        self.set_centered(False)
        self.interactive = True
        self.text = GUIText(self.rect.center, option, 32, BLUE_MOTION2, False, 0, *groups)
        self.text.interactive = True
        self.updateAll = False

    def update(self):
        if self.hovered():
            self.image.fill(WHITE_MOTION)
            self.text.set_text_color(BLACK_MOTION)
            if not self.updateAll:
                self.updateAll = True
        elif self.updateAll:
            self.image.fill(BLACK_MOTION)
            self.text.set_text_color(BLUE_MOTION2)

    def disable(self):
        super().disable()
        self.text.disable()

    def enable(self):
        super().enable()
        self.text.enable()

    def render(self, display: pygame.Surface):
        super().render(display)
        if self.isEnabled:
            self.text.render(display)


class ArrowButton(Sprite):
    def __init__(self, position: tuple, direction: str, *groups: SpriteGroup):
        super().__init__(f"arrowButton_{direction}", position, assets.misc["arrow_button"], *groups)
        self.interactive = True
        if direction == "right":
            self.flip(True, False)
        self.normalImage = self.image.copy()
        mask = pygame.mask.from_surface(self.image)
        self.hoveredImage = mask.to_surface(setcolor=BLACK_MOTION, unsetcolor=WHITE_MOTION)

    def update(self):
        if self.hovered():
            self.image = self.hoveredImage
        else:
            self.image = self.normalImage


class MainMenu(Scene):
    def __init__(self):
        super().__init__("MainMenu")
        pygame.mouse.set_visible(True)
        self.stage = "main"
        # Main Menu
        # Groups
        self.mainMenuGroup = self.new_group()
        self.ledsGroup = self.new_group()
        # Logo
        self.logo = GUIImage((147, 93), assets.misc["logo"], self.mainMenuGroup)
        self.logo.scale(4)
        self.logo.set_centered(False)
        self.logo.disable()
        # Computer
        self.computer = assets.backgrounds["main_menu"]
        # Clouds
        self.sky = assets.backgrounds["sky"]
        self.cloudGenerator = CloudGenerator((400, 60))
        # Computer background
        self.computerBackground = pygame.Surface((310, 240))
        self.computerBackground.fill(BLACK_MOTION)
        # Crt Effect
        self.crtEffect = pygame.Surface((310, 240))
        self.crtEffect.blit(assets.effects["crt"], (0, 0))
        # Router leds
        self.routerLed1 = RouterLed((494, 272), self.ledsGroup)
        self.routerLed2 = RouterLed((500, 272), self.ledsGroup)
        self.routerLed3 = RouterLed((506, 272), self.ledsGroup)
        # Options
        self.newGame = Option("- NEW GAME -", (96, 167), self.mainMenuGroup)
        self.continueGame = Option("- CONTINUE -", (96, 197), self.mainMenuGroup)
        self.options = Option("- OPTIONS -", (96, 227), self.mainMenuGroup)
        self.exit = Option("- EXIT -", (96, 257), self.mainMenuGroup)

        self.arrow = ArrowButton((150, 167), "left", self.mainMenuGroup)

        self.newGame.disable()
        self.continueGame.disable()
        self.options.disable()
        self.exit.disable()
        self.optionsIndex = 0
        self.optionsTimer = time.Timer(0.2)
        self.optionsTimer.start()
        self.loaded = False

        # Options Menu
        self.sizes = ["960x540", "1280x720", "1920x1080"]
        self.sizeIndex = 1
        self.optionsMenuGroup = self.new_group()

    def load_main_menu(self):
        if self.loaded:
            return
        if self.optionsTimer.done:
            self.optionsIndex += 1
            self.optionsTimer.start()
        if self.optionsIndex == 1:
            self.exit.enable()
        if self.optionsIndex == 2:
            self.options.enable()
        if self.optionsIndex == 3:
            self.continueGame.enable()
        if self.optionsIndex == 4:
            self.newGame.enable()
        if self.optionsIndex == 5:
            self.logo.enable()
            self.loaded = True

    def update(self):
        self.update_cursor()
        self.mainMenuGroup.update()
        self.ledsGroup.update()
        self.cloudGenerator.update()
        self.logo.y = sin_wave(93, 5, 200)
        self.optionsTimer.update()
        self.load_main_menu()

        if self.exit.released():
            exit()

    def render(self):
        self.display.blit(self.sky, (0, 0))
        self.cloudGenerator.render(self.display)
        self.display.blit(self.computerBackground, (96, 52))
        self.mainMenuGroup.render(self.display)
        self.display.blit(self.crtEffect, (96, 52), special_flags=pygame.BLEND_RGBA_MULT)
        self.display.blit(self.computer, (0, 0))
        self.ledsGroup.render(self.display)
