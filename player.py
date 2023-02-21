import pygame
import tile

PLAYER_COLOR = (128, 192, 128)
PLAYER_SHADE_COLOR = (64, 128, 64)
PLAYER_SHADE_OFFSET = 2
PLAYER_RADIUS = 12

class Player(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		x = self.x + tile.TILE_WIDTH // 2
		y = self.y + tile.TILE_HEIGHT // 2
		
		pygame.draw.circle(surface, PLAYER_SHADE_COLOR, (x, y + PLAYER_SHADE_OFFSET), PLAYER_RADIUS)
		pygame.draw.circle(surface, PLAYER_COLOR, (x, y), PLAYER_RADIUS)
