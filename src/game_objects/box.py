import src.game_objects.point as point
import src.game_objects.shaded_rectangular_object as shaded_rectangular_object

from src.constants import (TILE_WIDTH, TILE_HEIGHT, BOX_WIDTH, BOX_HEIGHT, BOX_COLOR, BOX_BORDER_RADIUS, BOX_SHADE_COLOR, BOX_SHADE_OFFSET)

class Box(shaded_rectangular_object.ShadedRectangularObject):
	def __init__(self, x, y):
		super().__init__(x, y, BOX_WIDTH, BOX_HEIGHT, BOX_COLOR, 0, BOX_BORDER_RADIUS, BOX_SHADE_COLOR)
		
		self.is_in_slot = False
	
	def offset_x(self):
		return (TILE_WIDTH - BOX_WIDTH) // 2

	def offset_y(self):
		return (TILE_HEIGHT - BOX_WIDTH) // 2
	
	def shade_offset(self):
		return BOX_SHADE_OFFSET
	
	def can_be_moved(self, level, offset_x, offset_y):
		return level.tile_is_free_for_box(self, point.Point(offset_x, offset_y))

	def move(self, level, offset_x, offset_y):
		self.x += offset_x
		self.y += offset_y

		self.check_if_it_is_in_slot(level)
	
	def check_if_it_is_in_slot(self, level):
		for bs in level.boxes_slots:
			if self.has_the_same_position(bs) and not self.is_in_slot:
				self.is_in_slot = True

				break
			elif self.is_in_slot:
				self.is_in_slot = False

				break
