import pygame
import circular_object

from constants import (TILE_WIDTH, TILE_HEIGHT)

class ShadedCircularObject(circular_object.CircularObject):
	def __init__(self, x, y, width, height, color, border_radius, shade_color):
		super().__init__(x, y, width, height, color, border_radius)

		self.shade_color = shade_color
	
	def draw(self, surface):
		position = (self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y() + self.shade_offset())
		
		pygame.draw.circle(surface, self.color, position, self.border_radius)
		super().draw(surface)
	
	def shade_offset(self):
		return 0