import pygame
from dataclasses import dataclass


@dataclass
class Point:
    coord: tuple[int, int] = (0, 0)
    color: tuple[int, int, int, int] = (0, 0, 0, 0)


pygame.init()
screen = pygame.display.set_mode((1270, 720))

image = pygame.image.load("../../data/images/misc/logo.png")
points = [[Point for x in range(image.get_width())] for y in range(image.get_height())]

for y_coord in range(image.get_height()):
    for x_coord in range(image.get_width()):
        points[y_coord][x_coord].coord = x_coord, y_coord
        points[y_coord][x_coord].color = image.get_at((x_coord, y_coord))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            print(event.key)

    for y_coord in range(image.get_height()):
        for x_coord in range(image.get_width()):
            pygame.draw.circle(screen, image.get_at((x_coord, y_coord)), (20 + x_coord * 10, 20 + y_coord * 10), 3)

    pygame.display.update()
