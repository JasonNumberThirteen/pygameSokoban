import pygame
import pygame.gfxdraw
import src.game_objects.game_object as game_object

from src.constants import (TILE_WIDTH, TILE_HEIGHT)

class CircularObject(game_object.GameObject):
	def __init__(self, x, y, color, border_radius):
		super().__init__(x, y)

		self.color = color
		self.border_radius = border_radius
	
	def draw(self, surface):
		position = (self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y())
		border_radius = self.border_radius - 1
		
		pygame.gfxdraw.aacircle(surface, position[0], position[1], border_radius, self.color)
		pygame.gfxdraw.filled_circle(surface, position[0], position[1], border_radius, self.color)