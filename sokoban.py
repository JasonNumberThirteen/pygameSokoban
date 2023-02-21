import pygame
import level

GAME_TITLE = "Sokoban"
BASE_RESOLUTION = (640, 480)
BACKGROUND_COLOR = (224, 224, 224)

pygame.init()
pygame.display.set_caption(GAME_TITLE)

canvas = pygame.display.set_mode(BASE_RESOLUTION)
is_running = True
level_data = [[0, 1, 0, 1, 1], [1, 1, 4, 1, 3], [0, 0, 1, 1, 2]]
level = level.Level(level_data)

while is_running:
	canvas.fill(BACKGROUND_COLOR)
	level.draw(canvas)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False
		
		level.player.detect_input(event)

	pygame.display.update()

pygame.quit()
