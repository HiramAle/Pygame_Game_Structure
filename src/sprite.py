import src.input as input
from src.components import *


class Sprite(Position, Renderable):
    def __init__(self, position: tuple[int, int], image: pygame.Surface = pygame.Surface((16, 16))):
        Position.__init__(self)
        Renderable.__init__(self)
        self.interactive = False
        self.x, self.y = position
        self._image = image

    @property
    def rect(self) -> pygame.Rect:
        if self.centered:
            return self.image.get_rect(center=self.position_as_tuple)
        else:
            return self.image.get_rect(topleft=self.position_as_tuple)

    @property
    def image(self) -> pygame.Surface:
        image = self._image.copy()
        if self.opacity != 255:
            image.set_alpha(self.opacity)
        if self.scale != 1:
            image = pygame.transform.scale_by(image, self.scale)
        return image

    @image.setter
    def image(self, new_image: pygame.Surface):
        self._image = new_image

    @property
    def position(self) -> tuple[int | float, int | float]:
        return self.position_as_tuple

    @position.setter
    def position(self, new_position: tuple[int | float, int | float]):
        self.x, self.y = new_position

    def update(self):
        ...

    def render(self, display: pygame.Surface):
        display.blit(self.image, self.rect)

    def hovered(self) -> bool:
        if self.rect.collidepoint(input.mousePosition):
            if not input.mouseHover:
                input.mouseHover = True
            return True
        return False

    def pressed(self):
        if self.hovered() and input.mouseButtons["left_hold"]:
            return True
        return False

    def clicked(self) -> bool:
        if self.hovered() and input.mouseButtons["left"]:
            return True
        return False

    def released(self):
        if self.hovered() and input.mouseButtons["left_release"]:
            return True
        return False
