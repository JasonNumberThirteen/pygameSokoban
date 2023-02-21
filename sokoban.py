import pygame
import tile

GAME_TITLE = "Sokoban"
BASE_RESOLUTION = (640, 480)
BACKGROUND_COLOR = (224, 224, 224)

pygame.init()
pygame.display.set_caption(GAME_TITLE)

canvas = pygame.display.set_mode(BASE_RESOLUTION)
is_running = True
tileA = tile.Tile(32, 32)
tileB = tile.Tile(64, 32)

while is_running:
	canvas.fill(BACKGROUND_COLOR)
	tileA.draw(canvas)
	tileB.draw(canvas)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

	pygame.display.update()

pygame.quit()
