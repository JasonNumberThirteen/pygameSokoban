import src.game_objects.box as box
import src.game_objects.tile as tile
import src.game_objects.player as player
import src.game_objects.box_slot as box_slot

class LevelBuilder(object):
	def __init__(self, filename):
		self.set_data(filename)
	
	def detected_tiles(self):
		return self.detected_objects(tile.Tile, lambda x: x > 0)
	
	def detected_boxes_slots(self):
		return self.detected_objects(box_slot.BoxSlot, lambda x: x == 2)
	
	def detected_boxes(self):
		return self.detected_objects(box.Box, lambda x: x == 3)
	
	def detected_objects(self, object, index_is_correct):
		objects = []
		
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if index_is_correct(int(self.data[y][x])):
					objects.append(object(x, y))
		
		return objects

	def detected_player(self, gm):
		for y in range(0, len(self.data)):
			for x in range(0, len(self.data[y])):
				if int(self.data[y][x]) == 4:
					return player.Player(gm, x, y)
		
		return None
	
	def set_data(self, filename):
		with open(filename) as file:
			content = file.read().split(sep='\n')
			data = []

			for line in content:
				data.append(line.split(sep=','))
			
			self.data = data