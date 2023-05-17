import pygame
import src.game_objects.game_object as game_object

class RectangularObject(game_object.GameObject):
	def __init__(self, x, y, width, height, color, frame_width, border_radius):
		super().__init__(x, y)

		self.width = width
		self.height = height
		self.color = color
		self.frame_width = frame_width
		self.border_radius = border_radius
	
	def draw(self, surface):
		position = self.position_in_tiles()
		rect = pygame.Rect(position[0], position[1], self.width, self.height)
		
		pygame.draw.rect(surface, self.color, rect, self.frame_width, self.border_radius)