import point
import pygame

from constants import (TILE_WIDTH, TILE_HEIGHT, BOX_WIDTH, BOX_HEIGHT, BOX_COLOR, BOX_BORDER_RADIUS, BOX_SHADE_COLOR, BOX_SHADE_OFFSET)

class Box(point.Point):
	def __init__(self, x, y):
		super().__init__(x, y)
		
		self.is_in_slot = False
	
	def draw(self, surface):
		x = self.x*TILE_WIDTH + (TILE_WIDTH - BOX_WIDTH) // 2
		y = self.y*TILE_HEIGHT + (TILE_HEIGHT - BOX_HEIGHT) // 2
		
		pygame.draw.rect(surface, BOX_SHADE_COLOR, pygame.Rect(x, y + BOX_SHADE_OFFSET, BOX_WIDTH, BOX_HEIGHT), 0, BOX_BORDER_RADIUS)
		pygame.draw.rect(surface, BOX_COLOR, pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT), 0, BOX_BORDER_RADIUS)
	
	def can_be_moved(self, level, offset_x, offset_y):
		for t in level.tiles:
			if self.x + offset_x == t.x and self.y + offset_y == t.y:
				return True
		
		return False

	def move(self, level, offset_x, offset_y):
		self.x += offset_x
		self.y += offset_y

		self.check_if_it_is_in_slot(level)
	
	def check_if_it_is_in_slot(self, level):
		for bs in level.boxes_slots:
			if self.x == bs.x and self.y == bs.y and not self.is_in_slot:
				self.is_in_slot = True

				break
			elif self.is_in_slot:
				self.is_in_slot = False

				break
