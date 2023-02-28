import pygame
import game_object

from constants import (TILE_WIDTH, TILE_HEIGHT)

class RectangularObject(game_object.GameObject):
	def __init__(self, x, y, width, height, color, frame_width, border_radius):
		super().__init__(x, y)

		self.width = width
		self.height = height
		self.color = color
		self.frame_width = frame_width
		self.border_radius = border_radius
	
	def draw(self, surface):
		rect = pygame.Rect(self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y(), self.width, self.height)
		
		pygame.draw.rect(surface, self.color, rect, self.frame_width, self.border_radius)
