import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define some constants for the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Network Puzzle")

# Set up the font
font = pygame.font.SysFont('Calibri', 25, True, False)

# Define some variables for the network
subnets = [
    {"name": "Subnet 1", "color": RED, "x": 100, "y": 100},
    {"name": "Subnet 2", "color": GREEN, "x": 500, "y": 100},
    {"name": "Subnet 3", "color": BLUE, "x": 300, "y": 400}
]

subnets = [
    {"network": "192.168.1.0/24", "x": 100, "y": 100, "radius": 50, "color": BLUE, "name":"Subnet 1"},
    {"network": "192.168.2.0/24", "x": 300, "y": 100, "radius": 50, "color": GREEN, "name":"Subnet 2"},
    {"network": "192.168.3.0/24", "x": 200, "y": 300, "radius": 50, "color": RED, "name":"Subnet 3"}
]
routers = [
    {"name": "Router 1", "color": BLACK, "x": 300, "y": 100, "routes": []},
    {"name": "Router 2", "color": BLACK, "x": 300, "y": 300, "routes": []},
    {"name": "Router 3", "color": BLACK, "x": 300, "y": 500, "routes": []}
]

# Define some variables for the game state
selected_subnet = None
selected_router = None

# Define a function to draw the network
def draw_network():
    for subnet in subnets:
        pygame.draw.rect(screen, subnet["color"], [subnet["x"], subnet["y"], 100, 100])
        text = font.render(subnet["name"], True, WHITE)
        screen.blit(text, [subnet["x"] + 10, subnet["y"] + 10])
    for router in routers:
        pygame.draw.circle(screen, router["color"], [router["x"], router["y"]], 50)
        text = font.render(router["name"], True, WHITE)
        screen.blit(text, [router["x"] - 35, router["y"] - 15])
        for route in router["routes"]:
            pygame.draw.line(screen, route["color"], [router["x"], router["y"]], [route["x"], route["y"]], 5)

# Define a function to update the router routes
def update_router_routes():
    for router in routers:
        router["routes"] = {}
        for subnet in subnets:
            if subnet != selected_subnet:
                distance = ((router["x"] - subnet["x"])**2 + (router["y"] - subnet["y"])**2)**0.5
                if distance <= subnet["radius"]:
                    router["routes"][subnet["network"]] = distance
        if selected_subnet:
            if selected_subnet["network"] not in router["routes"]:
                router["routes"][selected_subnet["network"]] = float('inf')

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for subnet in subnets:
                if subnet["x"] < pos[0] < subnet["x"] + 100 and subnet["y"] < pos[1] < subnet["y"] + 100:
                    selected_subnet = subnet
                    selected_router = None
                    update_router_routes()
            for router in routers:
                if (router["x"] - pos[0]) ** 2 + (router["y"] - pos[1]) ** 2 < 50 ** 2:
                    selected_router = router
                    selected_subnet = None

    # Update the game state
    if selected_router:
        selected_router["x"], selected_router["y"] = pygame.mouse.get_pos()
        update_router_routes()

    # Draw the network
    screen.fill(WHITE)
    draw_network()
    pygame.display.flip()

pygame.quit()