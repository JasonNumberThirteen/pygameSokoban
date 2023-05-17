import src.game_objects.box as box
import src.game_objects.tile as tile
import src.game_objects.player as player
import src.game_objects.box_slot as box_slot

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
		return self.detected_objects(box_slot.BoxSlot, 2)
	
	def detected_boxes(self):
		return self.detected_objects(box.Box, 3)

	def detected_player(self, gm):
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if int(self.data[y][x]) == 4:
					return player.Player(gm, x, y)
		
		return None
	
	def detected_objects(self, object, index):
		objects = []
		
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if int(self.data[y][x]) == index:
					objects.append(object(x, y))
		
		return objects
