import level_builder

class Level(object):
	def __init__(self, data, number):
		lb = level_builder.LevelBuilder(data)
		
		self.number = number
		self.tiles = lb.detected_tiles()
		self.boxes_slots = lb.detected_boxes_slots()
		self.boxes = lb.detected_boxes()
		self.player = lb.detected_player()
	
	def draw(self, surface):
		for t in self.tiles:
			t.draw(surface)
		
		for bs in self.boxes_slots:
			bs.draw(surface)

		for b in self.boxes:
			b.draw(surface)
		
		self.player.draw(surface)