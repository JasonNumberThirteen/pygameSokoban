import game_objects.rectangular_object as rectangular_object

from constants import (TILE_WIDTH, TILE_HEIGHT, BOX_SLOT_WIDTH, BOX_SLOT_HEIGHT, BOX_SLOT_COLOR, BOX_SLOT_FRAME_WIDTH, BOX_SLOT_BORDER_RADIUS)

class BoxSlot(rectangular_object.RectangularObject):
	def __init__(self, x, y):
		super().__init__(x, y, BOX_SLOT_WIDTH, BOX_SLOT_HEIGHT, BOX_SLOT_COLOR, BOX_SLOT_FRAME_WIDTH, BOX_SLOT_BORDER_RADIUS)

	def offset_x(self):
		return (TILE_WIDTH - BOX_SLOT_WIDTH) // 2

	def offset_y(self):
		return (TILE_HEIGHT - BOX_SLOT_HEIGHT) // 2