import pygame
from src.components import *
from src.config import Config
from src.commons import sine

font = pygame.font.Font("data/text/monogram.ttf", 16)


class UIObject(Renderable, Position):
    def __init__(self, position: tuple):
        Renderable.__init__(self)
        Position.__init__(self)
        self.x, self.y = position
        self.rect = self.get_rect(self.position_as_tuple)

    def update(self, dt: float):
        if self.centered:
            self.rect.center = self.position_as_tuple
        else:
            self.rect.topleft = self.position_as_tuple

    def render(self, display: pygame.Surface):
        image = self.image.copy()
        if not self.visible:
            return
        if self.opacity != 255:
            image.set_alpha(self.opacity)
        if self.scale != 1:
            image = pygame.transform.scale_by(image, self.scale)
            self.rect = image.get_rect(center=self.position_as_tuple)
        display.blit(image, self.rect)


class Text(UIObject):
    def __init__(self, position: tuple, text: str, color: str, shadow=True, shadow_color=Config.DARK_BLACK_MOTION):
        super().__init__(position)
        self.text = text
        self.color = color
        self.textImage = font.render(self.text, False, color)
        self.shadowImage = font.render(self.text, False, shadow_color)
        self.image = pygame.Surface((self.textImage.get_width(), self.textImage.get_height() + 1))
        self.image.set_colorkey((0, 0, 0))
        if shadow:
            self.image.blit(self.shadowImage, (0, 1))
        self.image.blit(self.textImage, (0, 0))
        self.rect = self.image.get_rect(center=self.position_as_tuple)


class Image(UIObject):
    def __init__(self, position: tuple, image: pygame.Surface):
        super().__init__(position)
        self.image = image
        self.rect = image.get_rect(center=self.position_as_tuple)


class MenuButton(UIObject):
    def __init__(self, position: tuple, button_type: dict[str, pygame.Surface], text: str):
        self.assets = button_type
        super().__init__(position)
        self.selected = False
        self.pressed = False
        self.set_image(self.pressed, self.selected)
        self.rect = self.get_rect(self.position_as_tuple)
        self.text = Text((self.x, self.y - 2), text, Config.WHITE_MOTION)

    def set_image(self, pressed: bool, selected: bool):
        status = "pressed" if pressed else "plain"
        state = "selected" if selected else ""
        status_name = f"{status}_{state}" if state != "" else status
        self.image = self.assets[status_name]

    def render(self, display: pygame.Surface):
        super().render(display)
        self.text.render(display)

    def update(self, dt: float):
        super().update(dt)
        self.set_image(self.pressed, self.selected)
        self.text.update(dt)
        if self.selected:
            self.text.y = sine(100, 1280, 1, self.y - 1)
        elif self.text.y != self.y - 2:
            self.text.y = self.y - 2


class SimpleButton(UIObject):
    def __init__(self, position: tuple, text: str):
        super().__init__(position)
        self.text = Text((self.x, self.y - 2), text, Config.WHITE_MOTION)
        self.image = pygame.Surface((self.text.rect.width + 3, self.text.rect.height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.get_rect(self.position_as_tuple)

    def render(self, display: pygame.Surface):
        super().render(display)
        pygame.draw.rect(self.image, Config.RED_MOTION2,
                         pygame.Rect(0, 0, self.text.rect.width + 3, self.text.rect.height), border_radius=3)
        self.text.render(display)

    def hover(self, mouse_position: tuple) -> bool:
        if self.rect.collidepoint(mouse_position):
            return True
        else:
            return False

    def clicked(self, mouse_position: tuple, click: bool):
        if not self.rect.collidepoint(mouse_position):
            return False
        if not click:
            return False
        return True

    def update(self, dt: float):
        super().update(dt)
        self.text.x = self.x + 1
        self.text.y = self.y - 2
        self.text.update(dt)
