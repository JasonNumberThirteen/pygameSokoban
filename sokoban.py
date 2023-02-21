import pygame

GAME_TITLE = "Sokoban"
BASE_RESOLUTION = (640, 480)
BACKGROUND_COLOR = (224, 224, 224)
TILE_COLOR = (32, 32, 64)
TILE_BORDER_RADIUS = 8

pygame.init()
pygame.display.set_caption(GAME_TITLE)

canvas = pygame.display.set_mode(BASE_RESOLUTION)
is_running = True

while is_running:
	canvas.fill(BACKGROUND_COLOR)
	pygame.draw.rect(canvas, TILE_COLOR, pygame.Rect(32, 32, 32, 32), 0, TILE_BORDER_RADIUS)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

	pygame.display.update()

pygame.quit()
