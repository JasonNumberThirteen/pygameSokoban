import pygame
import rectangular_object

from constants import (TILE_WIDTH, TILE_HEIGHT, TILE_OFFSET, TILE_COLOR, TILE_BORDER_RADIUS, TILE_SHADE_COLOR, TILE_SHADE_OFFSET)

class Tile(rectangular_object.RectangularObject):
	def __init__(self, x, y):
		super().__init__(x, y, TILE_WIDTH - TILE_OFFSET, TILE_HEIGHT - TILE_OFFSET, TILE_COLOR, 0, TILE_BORDER_RADIUS)
	
	def draw(self, surface):
		rect = pygame.Rect(self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y() + TILE_SHADE_OFFSET, self.width, self.height)
		
		pygame.draw.rect(surface, TILE_SHADE_COLOR, rect, 0, TILE_BORDER_RADIUS)
		super().draw(surface)
	
	def offset_x(self):
		return TILE_OFFSET
