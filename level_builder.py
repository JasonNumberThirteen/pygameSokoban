import box
import tile
import player
import box_slot

class LevelBuilder(object):
	def __init__(self, filename):
		self.set_data(filename)
	
	def set_data(self, filename):
		with open(filename) as file:
			content = file.read().split(sep='\n')
			data = []

			for line in content:
				data.append(line.split(sep=','))
			
			self.data = data
	
	def detected_tiles(self):
		tiles = []
		
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if int(self.data[y][x]) > 0:
					tiles.append(tile.Tile(x, y))
		
		return tiles
	
	def detected_boxes_slots(self):
		boxes_slots = []
		
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if int(self.data[y][x]) == 2:
					boxes_slots.append(box_slot.BoxSlot(x, y))
		
		return boxes_slots
	
	def detected_boxes(self):
		boxes = []
		
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if int(self.data[y][x]) == 3:
					boxes.append(box.Box(x, y))
		
		return boxes

	def detected_player(self):
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if int(self.data[y][x]) == 4:
					return player.Player(x, y)
		
		return None
