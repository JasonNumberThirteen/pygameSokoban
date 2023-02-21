import pygame

TILE_COLOR = (64, 64, 128)
TILE_SHADE_COLOR = (16, 16, 32)
TILE_SHADE_OFFSET = 4
TILE_WIDTH = 32
TILE_HEIGHT = 32
TILE_BORDER_RADIUS = 8

class Tile(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		pygame.draw.rect(surface, TILE_SHADE_COLOR, pygame.Rect(self.x, self.y + TILE_SHADE_OFFSET, TILE_WIDTH, TILE_HEIGHT), 0, TILE_BORDER_RADIUS)
		pygame.draw.rect(surface, TILE_COLOR, pygame.Rect(self.x, self.y, TILE_WIDTH, TILE_HEIGHT), 0, TILE_BORDER_RADIUS)
