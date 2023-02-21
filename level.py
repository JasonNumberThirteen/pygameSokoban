import level_builder

class Level(object):
	def __init__(self, data):
		lb = level_builder.LevelBuilder()
		
		self.tiles = lb.detected_tiles(data)
		self.boxes_slots = lb.detected_boxes_slots(data)
		self.boxes = lb.detected_boxes(data)
		self.player = lb.detected_player(data)
	
	def draw(self, surface):
		for t in self.tiles:
			t.draw(surface)
		
		for bs in self.boxes_slots:
			bs.draw(surface)

		for b in self.boxes:
			b.draw(surface)
		
		self.player.draw(surface)