import pygame
import pygame.gfxdraw
import game_objects.game_object as game_object

from constants import (TILE_WIDTH, TILE_HEIGHT)

class CircularObject(game_object.GameObject):
	def __init__(self, x, y, color, border_radius):
		super().__init__(x, y)

		self.color = color
		self.border_radius = border_radius
	
	def draw(self, surface):
		position = (self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y())
		
		pygame.gfxdraw.aacircle(surface, position[0], position[1], self.border_radius - 1, self.color)
		pygame.gfxdraw.filled_circle(surface, position[0], position[1], self.border_radius - 1, self.color)