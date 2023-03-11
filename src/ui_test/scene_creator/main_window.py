from __future__ import annotations
import pygame
import ctypes
from abc import abstractmethod
from src.config import WHITE_MOTION, BLUE_MOTION2, GREEN_MOTION, RED_MOTION2, YELLOW_MOTION, DARK_BLACK_MOTION
from src.config import BLACK_MOTION

ctypes.windll.user32.SetProcessDPIAware()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 360

font: pygame.Font = None


def load():
    global font
    font = pygame.Font("../../../data/gui/fonts/monogram.ttf")


class GUIElement:
    def __init__(self, position: tuple, dimensions: tuple, parent: GUIElement):
        self._position = position
        self.dimensions = dimensions
        self.surface = pygame.Surface(dimensions)
        self.parent = parent

    @property
    def x(self) -> int | float:
        return self._position[0]

    @property
    def y(self) -> int | float:
        return self._position[1]

    @property
    def relative_position(self) -> tuple:
        return self._position

    @property
    def width(self) -> int | float:
        return self.dimensions[0]

    @property
    def height(self) -> int | float:
        return self.dimensions[1]

    @property
    def rect(self) -> pygame.Rect:
        return self.surface.get_rect(topleft=self.relative_position)

    @abstractmethod
    def render(self): ...


class Text(GUIElement):
    def __init__(self, position: tuple, text: str, parent: GUIElement):
        super().__init__(position, font.size(text), parent)
        self.text = text
        self.surface = font.render(text, False, WHITE_MOTION)

    def render(self):
        self.parent.surface.blit(self.surface, self.relative_position)


class Panel(GUIElement):
    def __init__(self, position: tuple, dimensions: tuple, parent: pygame.Surface, color=BLACK_MOTION):
        super().__init__(position, dimensions, self)
        self.color = color
        self.surface.set_colorkey((0, 0, 0))
        self._elements: list[GUIElement] = []
        self.parent = parent

    def add(self, *elements: GUIElement):
        for element in elements:
            self._elements.append(element)

    def has_element(self, element: GUIElement) -> bool:
        return element in self._elements

    def remove(self, element: GUIElement):
        if self.has_element(element):
            self._elements.remove(element)

    def render(self):
        self.surface.fill((0, 0, 0))
        pygame.draw.rect(self.surface, self.color, self.surface.get_rect(), 2)

        for element in self._elements:
            element.render()

        self.parent.blit(self.surface, self.relative_position)


class Window:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Scene designer")
        load()
        self.selectedElement: GUIElement = None
        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.canvas = Panel((200, 0), (640, 360), self.screen, BLUE_MOTION2)

        # self.filePanel = pygame.Surface((SCREEN_WIDTH, 50))
        # self.filePanel.fill(GREEN_MOTION)
        # self.objectsPanel = pygame.Surface(((SCREEN_WIDTH - CANVAS_WIDTH) / 2, SCREEN_HEIGHT - 50))
        # self.objectsPanel.fill(RED_MOTION2)
        # self.classesPanel = pygame.Surface((CANVAS_WIDTH, SCREEN_HEIGHT - CANVAS_HEIGHT - 50))
        # self.classesPanel.fill(GREEN_MOTION)
        # self.optionsPanel = pygame.Surface(((SCREEN_WIDTH - CANVAS_WIDTH) / 2, SCREEN_HEIGHT - 50))
        # self.optionsPanel.fill(YELLOW_MOTION)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.canvas.rect.collidepoint((mouse_x, mouse_y)):
                        mouse_x -= self.canvas.x
                        mouse_y -= self.canvas.y
                        if self.selectedElement:
                            self.canvas.add(Text((mouse_x, mouse_y), "Hola", self.canvas))

            self.screen.fill(BLACK_MOTION)

            # self.screen.blit(self.filePanel, (0, 0))
            # self.screen.blit(self.objectsPanel, (0, 50))
            # self.screen.blit(self.canvas, (self.objectsPanel.get_width(), 50))
            # self.screen.blit(self.classesPanel, (self.objectsPanel.get_width(), CANVAS_HEIGHT + 50))
            # self.screen.blit(self.optionsPanel, (SCREEN_WIDTH - self.optionsPanel.get_width(), 50))

            self.canvas.render()

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    Window().run()
