import pygame
import constants

class Box(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		x = self.x*constants.TILE_WIDTH + (constants.TILE_WIDTH - constants.BOX_WIDTH) // 2
		y = self.y*constants.TILE_HEIGHT + (constants.TILE_HEIGHT - constants.BOX_HEIGHT) // 2
		
		pygame.draw.rect(surface, constants.BOX_SHADE_COLOR, pygame.Rect(x, y + constants.BOX_SHADE_OFFSET, constants.BOX_WIDTH, constants.BOX_HEIGHT), 0, constants.BOX_BORDER_RADIUS)
		pygame.draw.rect(surface, constants.BOX_COLOR, pygame.Rect(x, y, constants.BOX_WIDTH, constants.BOX_HEIGHT), 0, constants.BOX_BORDER_RADIUS)
