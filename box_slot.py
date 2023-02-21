import pygame
import tile 

BOX_SLOT_COLOR = (192, 0, 0)
BOX_SLOT_WIDTH = 16
BOX_SLOT_HEIGHT = 16
BOX_SLOT_BORDER_RADIUS = 2
BOX_SLOT_FRAME_WIDTH = 2

class BoxSlot(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		x = self.x + (tile.TILE_WIDTH - BOX_SLOT_WIDTH) // 2
		y = self.y + (tile.TILE_HEIGHT - BOX_SLOT_HEIGHT) // 2
		
		pygame.draw.rect(surface, BOX_SLOT_COLOR, pygame.Rect(x, y, BOX_SLOT_WIDTH, BOX_SLOT_HEIGHT), BOX_SLOT_FRAME_WIDTH, BOX_SLOT_BORDER_RADIUS)