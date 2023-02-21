import pygame

GAME_TITLE = "Sokoban"
BASE_RESOLUTION = (640, 480)

pygame.init()
pygame.display.set_caption(GAME_TITLE)

canvas = pygame.display.set_mode(BASE_RESOLUTION)
is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pygame.display.update()

pygame.quit()
