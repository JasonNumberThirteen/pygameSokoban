import pygame
import rectangular_object

from constants import (TILE_WIDTH, TILE_HEIGHT)

class ShadedRectangularObject(rectangular_object.RectangularObject):
	def draw(self, surface):
		rect = pygame.Rect(self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y() + self.shade_offset(), self.width, self.height)
		
		pygame.draw.rect(surface, self.color, rect, 0, self.border_radius)
		super().draw(surface)
	
	def shade_offset(self):
		return 0