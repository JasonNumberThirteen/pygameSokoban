import pygame
import constants

class Player(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.moves = 0
	
	def detect_input(self, event):
		if event.type == pygame.KEYDOWN:
			if self.can_move_up(event):
				self.y -= constants.TILE_HEIGHT
				self.moves += 1
			elif self.can_move_down(event):
				self.y += constants.TILE_HEIGHT
				self.moves += 1
			elif self.can_move_left(event):
				self.x -= constants.TILE_WIDTH
				self.moves += 1
			elif self.can_move_right(event):
				self.x += constants.TILE_WIDTH
				self.moves += 1
	
	def can_move_up(self, event):
		return event.key == ord("w")
	
	def can_move_down(self, event):
		return event.key == ord("s")
	
	def can_move_left(self, event):
		return event.key == ord("a")
	
	def can_move_right(self, event):
		return event.key == ord("d")
	
	def draw(self, surface):
		x = self.x + constants.TILE_WIDTH // 2
		y = self.y + constants.TILE_HEIGHT // 2
		
		pygame.draw.circle(surface, constants.PLAYER_SHADE_COLOR, (x, y + constants.PLAYER_SHADE_OFFSET), constants.PLAYER_RADIUS)
		pygame.draw.circle(surface, constants.PLAYER_COLOR, (x, y), constants.PLAYER_RADIUS)
