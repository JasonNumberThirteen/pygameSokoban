import pygame
import constants

class Player(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.moves = 0
	
	def detect_input(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == ord("w"):
				self.y -= constants.TILE_HEIGHT
				self.moves += 1
			elif event.key == ord("s"):
				self.y += constants.TILE_HEIGHT
				self.moves += 1
			elif event.key == ord("a"):
				self.x -= constants.TILE_WIDTH
				self.moves += 1
			elif event.key == ord("d"):
				self.x += constants.TILE_WIDTH
				self.moves += 1
	
	def draw(self, surface):
		x = self.x + constants.TILE_WIDTH // 2
		y = self.y + constants.TILE_HEIGHT // 2
		
		pygame.draw.circle(surface, constants.PLAYER_SHADE_COLOR, (x, y + constants.PLAYER_SHADE_OFFSET), constants.PLAYER_RADIUS)
		pygame.draw.circle(surface, constants.PLAYER_COLOR, (x, y), constants.PLAYER_RADIUS)
