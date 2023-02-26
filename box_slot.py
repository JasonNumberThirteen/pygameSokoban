import pygame
import constants

class BoxSlot(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		x = self.x*constants.TILE_WIDTH + (constants.TILE_WIDTH - constants.BOX_SLOT_WIDTH) // 2
		y = self.y*constants.TILE_HEIGHT + (constants.TILE_HEIGHT - constants.BOX_SLOT_HEIGHT) // 2
		
		pygame.draw.rect(surface, constants.BOX_SLOT_COLOR, pygame.Rect(x, y, constants.BOX_SLOT_WIDTH, constants.BOX_SLOT_HEIGHT), constants.BOX_SLOT_FRAME_WIDTH, constants.BOX_SLOT_BORDER_RADIUS)