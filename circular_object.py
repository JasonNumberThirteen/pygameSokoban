import point
import pygame

from constants import (TILE_WIDTH, TILE_HEIGHT)

class CircularObject(point.Point):
	def __init__(self, x, y, color, border_radius):
		super().__init__(x, y)

		self.color = color
		self.border_radius = border_radius
	
	def draw(self, surface):
		position = (self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y())
		
		pygame.draw.circle(surface, self.color, position, self.border_radius)

	def offset_x(self):
		return 0
	
	def offset_y(self):
		return 0
