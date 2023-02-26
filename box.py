import pygame
import constants

class Box(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.is_in_slot = False
	
	def draw(self, surface):
		x = self.x*constants.TILE_WIDTH + (constants.TILE_WIDTH - constants.BOX_WIDTH) // 2
		y = self.y*constants.TILE_HEIGHT + (constants.TILE_HEIGHT - constants.BOX_HEIGHT) // 2
		
		pygame.draw.rect(surface, constants.BOX_SHADE_COLOR, pygame.Rect(x, y + constants.BOX_SHADE_OFFSET, constants.BOX_WIDTH, constants.BOX_HEIGHT), 0, constants.BOX_BORDER_RADIUS)
		pygame.draw.rect(surface, constants.BOX_COLOR, pygame.Rect(x, y, constants.BOX_WIDTH, constants.BOX_HEIGHT), 0, constants.BOX_BORDER_RADIUS)
	
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
				self.is_in_correct_place = False

				break
