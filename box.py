import pygame
import tile

BOX_COLOR = (192, 96, 0)
BOX_SHADE_COLOR = (128, 32, 0)
BOX_SHADE_OFFSET = 2
BOX_WIDTH = 16
BOX_HEIGHT = 16
BOX_BORDER_RADIUS = 4

class Box(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		x = self.x + (tile.TILE_WIDTH - BOX_WIDTH) // 2
		y = self.y + (tile.TILE_HEIGHT - BOX_HEIGHT) // 2
		
		pygame.draw.rect(surface, BOX_SHADE_COLOR, pygame.Rect(x, y + BOX_SHADE_OFFSET, BOX_WIDTH, BOX_HEIGHT), 0, BOX_BORDER_RADIUS)
		pygame.draw.rect(surface, BOX_COLOR, pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT), 0, BOX_BORDER_RADIUS)
