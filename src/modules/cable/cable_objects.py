from src.sprite import Sprite
from src.config import *


class Cable(Sprite):
    def __init__(self, position: tuple, color: str, name: str):
        super().__init__(position)
        self.x, self.y = position
        self.name = name
        self.color = color
        self.image = pygame.Surface((100, 16))
        self._image.fill(color)
        self.interactive = True

    def __repr__(self):
        return str(self.name)
