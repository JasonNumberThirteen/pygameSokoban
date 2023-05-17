import src.game_objects.point as point

from src.constants import (TILE_WIDTH, TILE_HEIGHT)

class GameObject(point.Point):
	def position_in_tiles(self):
		return (self.x*TILE_WIDTH + self.offset_x(), self.y*TILE_HEIGHT + self.offset_y())
	
	def offset_x(self):
		return 0
	
	def offset_y(self):
		return 0