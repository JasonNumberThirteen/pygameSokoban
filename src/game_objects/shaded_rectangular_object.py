import pygame
import src.game_objects.rectangular_object as rectangular_object

class ShadedRectangularObject(rectangular_object.RectangularObject):
	def __init__(self, x, y, width, height, color, frame_width, border_radius, shade_color):
		super().__init__(x, y, width, height, color, frame_width, border_radius)

		self.shade_color = shade_color
	
	def draw(self, surface):
		position = self.position_in_tiles()
		position_y = position[1] + self.shade_offset()
		rect = pygame.Rect(position[0], position_y, self.width, self.height)
		
		pygame.draw.rect(surface, self.shade_color, rect, 0, self.border_radius)
		super().draw(surface)
	
	def shade_offset(self):
		return 0