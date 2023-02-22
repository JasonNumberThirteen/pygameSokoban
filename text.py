import pygame

class Text(object):
	def __init__(self, text, x=0, y=0, color=(255, 255, 255), font_size=32):
		self.font = pygame.font.SysFont("arial.ttf", font_size)
		self.render = self.font.render(text, True, color)
		self.rect = self.render.get_rect()
		self.color = color

		self.set_position(x, y)
	
	def set_text(self, text):
		self.render = self.font.render(text, True, self.color)
	
	def set_position(self, x, y):
		self.rect.x = x
		self.rect.y = y
	
	def draw(self, surface):
		surface.blit(self.render, self.rect)
