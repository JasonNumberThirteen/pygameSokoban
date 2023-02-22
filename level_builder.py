import box
import tile
import player
import box_slot
import constants

class LevelBuilder(object):
	def __init__(self, data):
		self.set_data(data)
	
	def set_data(self, data):
		self.data = data
	
	def detected_tiles(self):
		tiles = []
		
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if self.data[y][x] > 0:
					tiles.append(tile.Tile(constants.TILE_WIDTH*x, constants.TILE_HEIGHT*y))
		
		return tiles
	
	def detected_boxes_slots(self):
		boxes_slots = []
		
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if self.data[y][x] == 2:
					boxes_slots.append(box_slot.BoxSlot(constants.TILE_WIDTH*x, constants.TILE_HEIGHT*y))
		
		return boxes_slots
	
	def detected_boxes(self):
		boxes = []
		
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if self.data[y][x] == 3:
					boxes.append(box.Box(constants.TILE_WIDTH*x, constants.TILE_HEIGHT*y))
		
		return boxes

	def detected_player(self):
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if self.data[y][x] == 4:
					return player.Player(constants.TILE_WIDTH*x, constants.TILE_HEIGHT*y)
		
		return None
