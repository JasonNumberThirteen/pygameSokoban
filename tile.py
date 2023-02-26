import point
import pygame

from constants import (TILE_WIDTH, TILE_HEIGHT, TILE_OFFSET, TILE_COLOR, TILE_BORDER_RADIUS, TILE_SHADE_COLOR, TILE_SHADE_OFFSET)

class Tile(point.Point):
	def draw(self, surface):
		x = self.x*TILE_WIDTH + TILE_OFFSET
		y = self.y*TILE_HEIGHT
		width = TILE_WIDTH - TILE_OFFSET
		height = TILE_HEIGHT - TILE_OFFSET
		
		pygame.draw.rect(surface, TILE_SHADE_COLOR, pygame.Rect(x, y + TILE_SHADE_OFFSET, width, height), 0, TILE_BORDER_RADIUS)
		pygame.draw.rect(surface, TILE_COLOR, pygame.Rect(x, y, width, height), 0, TILE_BORDER_RADIUS)
