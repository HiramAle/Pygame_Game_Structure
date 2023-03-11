import pygame


class Position:
    def __init__(self, position: tuple[int | float, int | float]):
        self._position = pygame.math.Vector2(position)
        self._layer = 0

    @property
    def x(self) -> int | float:
        return self._position.x

    @property
    def y(self) -> int | float:
        return self._position.y

    @property
    def layer(self) -> int:
        return self._layer

    @property
    def position(self) -> tuple[int | float, int | float]:
        return self.x, self.y

    @property
    def position_vector(self) -> pygame.math.Vector2:
        return self._position

    @x.setter
    def x(self, value: int | float) -> None:
        self._position.x = value

    @y.setter
    def y(self, value: int | float) -> None:
        self._position.y = int(value)

    @layer.setter
    def layer(self, value: int) -> None:
        self._layer = value

    @position.setter
    def position(self, value: tuple[int | float, int | float]) -> None:
        self.x, self.y = value

    @position_vector.setter
    def position_vector(self, value: pygame.math.Vector2) -> None:
        self._position = value


class Renderable:
    def __init__(self, image: pygame.Surface):
        self._source_image = image
        self._image = self._source_image.copy()
        self._visible = True
        self._opacity = 255
        self._centered = True
        self._scale = 1
        self._flip = [False, False]

    def set_centered(self, value: bool):
        self._centered = value

    def set_visible(self, value: bool):
        self._visible = value

    def set_color_key(self, color: tuple | str):
        self._image.set_colorkey(color)

    def set_opacity(self, opacity: int):
        self._opacity = opacity
        self._image.set_alpha(opacity)

    def flip(self, horizontal: bool, vertical: bool):
        self._flip = [horizontal, vertical]
        self._image = pygame.transform.flip(self._image, horizontal, vertical)

    def scale(self, scale: int):
        self._scale = scale
        self._image = pygame.transform.scale_by(self._image, scale)

    def is_visible(self) -> bool:
        return self._visible

    @property
    def image(self) -> pygame.Surface:
        return self._image

    @image.setter
    def image(self, new_image: pygame.Surface):
        self._source_image = new_image
        self._image = self._source_image.copy()


class Text:
    def __init__(self):
        self._text = ""

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str) -> None:
        self._text = value


class Tag:
    def __init__(self):
        self.tags: list[str] = []

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags

    def add_tags(self, *tags: str) -> None:
        for tag in tags:
            if not self.has_tag(tag):
                self.tags.append(tag)

    def remove_tags(self, *tags: str) -> None:
        for tag in tags:
            if self.has_tag(tag):
                self.tags.remove(tag)
