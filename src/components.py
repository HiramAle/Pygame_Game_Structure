import pygame


class Renderable:
    def __init__(self):
        self.visible = True
        self.opacity = 255
        self._image: pygame.Surface = pygame.Surface((16, 16))
        self.centered = True
        self.scale = 1
        self.flip = [False, False]


class Position:
    def __init__(self):
        self._position = pygame.math.Vector2(0, 0)

    @property
    def x(self) -> int | float:
        return self._position.x

    @property
    def y(self) -> int | float:
        return self._position.y

    @x.setter
    def x(self, value: int | float):
        self._position.x = value

    @y.setter
    def y(self, value: int | float):
        self._position.y = int(value)

    @property
    def position_as_tuple(self) -> tuple[int | float, int | float]:
        return self.x, self.y

    @property
    def position_as_vector(self) -> pygame.math.Vector2:
        return self._position
