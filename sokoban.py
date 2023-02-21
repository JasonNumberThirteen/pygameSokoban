import pygame

GAME_TITLE = "Sokoban"
BASE_RESOLUTION = (640, 480)
BACKGROUND_COLOR = (224, 224, 224)
TILE_COLOR = (64, 64, 128)
TILE_SHADE_COLOR = (16, 16, 32)
TILE_SHADE_OFFSET = 4
TILE_WIDTH = 32
TILE_HEIGHT = 32
TILE_BORDER_RADIUS = 8

pygame.init()
pygame.display.set_caption(GAME_TITLE)

class Tile(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		pygame.draw.rect(surface, TILE_SHADE_COLOR, pygame.Rect(self.x, self.y + TILE_SHADE_OFFSET, TILE_WIDTH, TILE_HEIGHT), 0, TILE_BORDER_RADIUS)
		pygame.draw.rect(surface, TILE_COLOR, pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_HEIGHT), 0, TILE_BORDER_RADIUS)

canvas = pygame.display.set_mode(BASE_RESOLUTION)
is_running = True
tile = Tile(32, 32)
tileB = Tile(64, 32)

while is_running:
	canvas.fill(BACKGROUND_COLOR)
	tile.draw(canvas)
	tileB.draw(canvas)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			is_running = False

	pygame.display.update()

pygame.quit()
