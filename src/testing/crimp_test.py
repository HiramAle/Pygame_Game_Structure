import pygame
from src.sprite import Sprite
from src.sprite_group import SpriteGroup
from src.config import *


class Indicator(Sprite):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.image = pygame.Surface((20, 120))
        self._image.set_colorkey((0, 0, 0))
        pygame.draw.rect(self._image, WHITE_MOTION, pygame.Rect(0, 25, 20, 95), border_radius=8)
        pygame.draw.polygon(self._image, WHITE_MOTION, ((0, 0), (20, 0), (10, 20)))


class ColorBar(Sprite):
    def __init__(self, position: tuple):
        super().__init__(position)
        self.image = pygame.Surface((400, 90))
        self._image.fill(RED_MOTION2)
        pygame.draw.rect(self._image, YELLOW_MOTION, pygame.Rect(150, 0, 100, 90))
        pygame.draw.rect(self._image, GREEN_MOTION, pygame.Rect(175, 0, 50, 90))


pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
dt = 0.2
spriteGroup = SpriteGroup()
colorBar = ColorBar((250, 262.5))
indicator = Indicator((50, 250))
spriteGroup.add(colorBar)
spriteGroup.add(indicator)
movement = 400

while True:
    for event in pygame.event.get():
        event: pygame.event.Event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                color = colorBar.image.get_at((int(indicator.x - 50), 0))
                if color == pygame.Color(GREEN_MOTION):
                    print("GREEN")
                elif color == pygame.Color(YELLOW_MOTION):
                    print("YELLOW")
                elif color == pygame.Color(RED_MOTION2):
                    print("RED")

    screen.fill(DARK_BLACK_MOTION)

    indicator.x += dt * movement

    if indicator.x > 450:
        indicator.x = 450
        movement *= -1

    if indicator.x < 50:
        indicator.x = 50
        movement *= -1

    spriteGroup.update()
    spriteGroup.render(screen)

    dt = clock.tick() / 1000
    pygame.display.update()
