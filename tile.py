import pygame
import constants

class Tile(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		x = self.x*constants.TILE_WIDTH + constants.TILE_OFFSET
		y = self.y*constants.TILE_HEIGHT
		width = constants.TILE_WIDTH - constants.TILE_OFFSET
		height = constants.TILE_HEIGHT - constants.TILE_OFFSET
		
		pygame.draw.rect(surface, constants.TILE_SHADE_COLOR, pygame.Rect(x, y + constants.TILE_SHADE_OFFSET, width, height), 0, constants.TILE_BORDER_RADIUS)
		pygame.draw.rect(surface, constants.TILE_COLOR, pygame.Rect(x, y, width, height), 0, constants.TILE_BORDER_RADIUS)
