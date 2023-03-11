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


class CubicBezier:
    def __init__(self, *points):
        points = list(points)
        if len(points) not in [2, 4]:
            raise Exception('InvalidArgumentCountError')
        if len(points) == 2:
            points = [[0, 0]] + points + [[1, 1]]
        self.points = points

    def calculate(self, t):
        x = (1 - t) ** 3 * self.points[0][0] + 3 * t * (1 - t) ** 2 * self.points[1][0] + 3 * t ** 2 * (1 - t) * \
            self.points[2][0] + t ** 3 * self.points[3][0]
        y = (1 - t) ** 3 * self.points[0][1] + 3 * t * (1 - t) ** 2 * self.points[1][1] + 3 * t ** 2 * (1 - t) * \
            self.points[2][1] + t ** 3 * self.points[3][1]
        return [x, y]

    def calculate_x(self, t):
        return self.calculate(t)[0]


pygame.init()
pygame.display.set_caption("test")
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
circle_x, circle_y = 250, 250
original_y = 250
oscillation_distance = 250
speed = 50
time_seconds = 2
font = pygame.font.Font("../data/gui/fonts/monogram.ttf", 32)
dt = 0.2
timer = 0
t = 100
BEZIER_TYPES = {
    'bounce_out': [[2.4, 0.01], [1.25, 2.65]],
    'slow_in': [[0.91, 0.29], [0.98, -0.33]],
}
bezier = CubicBezier([2.4, 0.01], [1.25, 2.65])
while True:
    screen.fill("red")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        print(bezier.calculate_x(pygame.time.get_ticks()))
        if event.type == pygame.MOUSEWHEEL:
            # speed += 10 * event.y
            # if speed < 10:
            #     speed = 10
            t += 5 * event.y

            if t > 100:
                t = 100
            if t < 0:
                t = 0

    # w = int(remap(20, 50, 0, 255, t))
    # color = (lerp(100, 255, t), lerp(50, 150, t), lerp(0, 255, t))
    # print(t, w)
    # pygame.draw.circle(screen, (w, w, w), (circle_x, circle_y), 30)

    pygame.display.update()
    dt = clock.tick(60) / 1000
