import src.level_builder as level_builder

class Level(object):
	def __init__(self, gm, data):
		self.build(gm, data)
	
	def build(self, gm, data):
		lb = level_builder.LevelBuilder(data)
		
		self.tiles = lb.detected_tiles()
		self.boxes_slots = lb.detected_boxes_slots()
		self.boxes = lb.detected_boxes()
		self.player = lb.detected_player(gm)
	
	def draw(self, surface):
		self.draw_objects(surface, self.tiles)
		self.draw_objects(surface, self.boxes_slots)
		self.draw_objects(surface, self.boxes)
		self.player.draw(surface)
	
	def draw_objects(self, surface, objects):
		for o in objects:
			o.draw(surface)
	
	def inserted_boxes(self):
		count = 0

		for b in self.boxes:
			if b.is_in_slot:
				count += 1

		return count