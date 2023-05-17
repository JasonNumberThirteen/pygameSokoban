import pygame
import pygame.gfxdraw
import src.game_objects.circular_object as circular_object

class ShadedCircularObject(circular_object.CircularObject):
	def __init__(self, x, y, color, border_radius, shade_color):
		super().__init__(x, y, color, border_radius)

		self.shade_color = shade_color
	
	def draw(self, surface):
		position = self.position_in_tiles()
		
		pygame.gfxdraw.aacircle(surface, position[0], position[1] + self.shade_offset(), self.border_radius - 1, self.shade_color)
		pygame.gfxdraw.filled_circle(surface, position[0], position[1] + self.shade_offset(), self.border_radius - 1, self.shade_color)
		super().draw(surface)
	
	def shade_offset(self):
		return 0