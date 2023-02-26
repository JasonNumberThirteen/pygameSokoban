import level_builder

class Level(object):
	def __init__(self, gm, data, number):
		self.number = number
		
		self.build(gm, data)
	
	def build(self, gm, data):
		lb = level_builder.LevelBuilder(data)
		
		self.tiles = lb.detected_tiles()
		self.boxes_slots = lb.detected_boxes_slots()
		self.boxes = lb.detected_boxes()
		self.player = lb.detected_player(gm)
	
	def draw(self, surface):
		for t in self.tiles:
			t.draw(surface)
		
		for bs in self.boxes_slots:
			bs.draw(surface)

		for b in self.boxes:
			b.draw(surface)
		
		self.player.draw(surface)
	
	def inserted_boxes(self):
		count = 0

		for b in self.boxes:
			if b.is_in_slot:
				count += 1

		return count