import pygame

from constants import (TILE_WIDTH, TILE_HEIGHT, BOX_SLOT_WIDTH, BOX_SLOT_HEIGHT, BOX_SLOT_COLOR, BOX_SLOT_FRAME_WIDTH, BOX_SLOT_BORDER_RADIUS)

class BoxSlot(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		x = self.x*TILE_WIDTH + (TILE_WIDTH - BOX_SLOT_WIDTH) // 2
		y = self.y*TILE_HEIGHT + (TILE_HEIGHT - BOX_SLOT_HEIGHT) // 2
		
		pygame.draw.rect(surface, BOX_SLOT_COLOR, pygame.Rect(x, y, BOX_SLOT_WIDTH, BOX_SLOT_HEIGHT), BOX_SLOT_FRAME_WIDTH, BOX_SLOT_BORDER_RADIUS)