import pygame
import rectangular_object

from constants import (TILE_WIDTH, TILE_HEIGHT, BOX_WIDTH, BOX_HEIGHT, BOX_COLOR, BOX_BORDER_RADIUS, BOX_SHADE_COLOR, BOX_SHADE_OFFSET)

class Box(rectangular_object.RectangularObject):
	def __init__(self, x, y):
		super().__init__(x, y, BOX_WIDTH, BOX_HEIGHT, BOX_COLOR, 0, BOX_BORDER_RADIUS)
		
		self.is_in_slot = False
	
	def draw(self, surface):
		rect = pygame.Rect(self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y() + BOX_SHADE_OFFSET, self.width, self.height)
		
		pygame.draw.rect(surface, BOX_SHADE_COLOR, rect, 0, BOX_BORDER_RADIUS)
		super().draw(surface)

	def offset_x(self):
		return (TILE_WIDTH - BOX_WIDTH) // 2

	def offset_y(self):
		return (TILE_HEIGHT - BOX_WIDTH) // 2
	
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
