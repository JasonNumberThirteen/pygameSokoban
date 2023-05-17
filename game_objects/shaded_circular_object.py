import pygame
import pygame.gfxdraw
import game_objects.circular_object as circular_object

from constants import (TILE_WIDTH, TILE_HEIGHT)

class ShadedCircularObject(circular_object.CircularObject):
	def __init__(self, x, y, color, border_radius, shade_color):
		super().__init__(x, y, color, border_radius)

		self.shade_color = shade_color
	
	def draw(self, surface):
		position = (self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y() + self.shade_offset())
		
		pygame.gfxdraw.aacircle(surface, position[0], position[1], self.border_radius - 1, self.shade_color)
		pygame.gfxdraw.filled_circle(surface, position[0], position[1], self.border_radius - 1, self.shade_color)
		super().draw(surface)
	
	def shade_offset(self):
		return 0