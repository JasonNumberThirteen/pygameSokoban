import shaded_rectangular_object

from constants import (TILE_WIDTH, TILE_HEIGHT, TILE_OFFSET, TILE_COLOR, TILE_BORDER_RADIUS, TILE_SHADE_COLOR, TILE_SHADE_OFFSET)

class Tile(shaded_rectangular_object.ShadedRectangularObject):
	def __init__(self, x, y):
		super().__init__(x, y, TILE_WIDTH - TILE_OFFSET, TILE_HEIGHT - TILE_OFFSET, TILE_COLOR, 0, TILE_BORDER_RADIUS, TILE_SHADE_COLOR)
	
	def offset_x(self):
		return TILE_OFFSET

	def shade_offset(self):
		return TILE_SHADE_OFFSET
