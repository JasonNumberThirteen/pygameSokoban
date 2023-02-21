import pygame

TILE_COLOR = (64, 64, 128)
TILE_SHADE_COLOR = (16, 16, 32)
TILE_SHADE_OFFSET = 4
TILE_WIDTH = 32
TILE_HEIGHT = 32
TILE_BORDER_RADIUS = 8
TILE_OFFSET = 1

class Tile(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		x = self.x + TILE_OFFSET
		width = TILE_WIDTH - TILE_OFFSET
		height = TILE_HEIGHT - TILE_OFFSET
		
		pygame.draw.rect(surface, TILE_SHADE_COLOR, pygame.Rect(x, self.y + TILE_SHADE_OFFSET, width, height), 0, TILE_BORDER_RADIUS)
		pygame.draw.rect(surface, TILE_COLOR, pygame.Rect(x, self.y, width, height), 0, TILE_BORDER_RADIUS)
