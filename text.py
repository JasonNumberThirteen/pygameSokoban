import pygame

from constants import (UI_TEXT_FONT, UI_TEXT_COLOR, UI_TEXT_FONT_SIZE)

class Text(object):
	def __init__(self, text, x=0, y=0, color=UI_TEXT_COLOR, font_size=UI_TEXT_FONT_SIZE):
		self.font = pygame.font.SysFont(UI_TEXT_FONT, font_size)

		self.set_color(color)
		self.set_text(text)
		self.set_position(x, y)
	
	def set_text(self, text):
		self.render = self.font.render(text, True, self.color)
		self.rect = self.render.get_rect()
	
	def set_position(self, x, y):
		self.rect.x = x
		self.rect.y = y

	def set_color(self, color):
		self.color = color
	
	def draw(self, surface):
		surface.blit(self.render, self.rect)
