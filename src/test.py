import pygame
import math


def sin_wave(value: int | float, distance: int, speed: int) -> float:
    time = pygame.time.get_ticks() / 2 % 1280
    return value + math.sin(time / speed) * distance


def lerp(a_value: int | float, b_value: int | float, t_value: float) -> float:
    return (1 - t_value) * a_value + b_value * t_value


def inv_lerp(a_value: int | float, b_value: int | float, v_value: float) -> float:
    return (v_value - a_value) / (b_value - a_value)


def remap(i_min: float, i_max: float, o_min: float, o_max: float, v_value: float) -> float:
    ts = inv_lerp(i_min, i_max, v_value) % 1
    tw = lerp(o_min, o_max, ts)
    print(ts)
    print(tw)
    return tw


pygame.init()
pygame.display.set_caption("test")
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
circle_x, circle_y = 250, 250
original_y = 250
oscillation_distance = 250
speed = 50
time_seconds = 2
font = pygame.font.Font("../data/text/monogram.ttf", 32)
dt = 0.2
timer = 0
t = 100
while True:
    screen.fill("red")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEWHEEL:
            # speed += 10 * event.y
            # if speed < 10:
            #     speed = 10
            t += 5 * event.y

            if t > 100:
                t = 100
            if t < 0:
                t = 0

    w = int(remap(20, 50, 0, 255, t))
    # color = (lerp(100, 255, t), lerp(50, 150, t), lerp(0, 255, t))
    print(t, w)
    pygame.draw.circle(screen, (w, w, w), (circle_x, circle_y), 30)

    pygame.display.update()
    dt = clock.tick(60) / 1000
