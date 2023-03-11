import pygame

pygame.init()

font = pygame.Font(None, 60)
screen = pygame.display.set_mode((500, 500))

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill("dodgerblue")
    txt = font.render("Hi u/shy_dinosaur. Consider this a demo.\nHave a good day!", True, "lightgrey", None, 400)
    screen.blit(txt, (20, 20))
    pygame.display.flip()

pygame.quit()
