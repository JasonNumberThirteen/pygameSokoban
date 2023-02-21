import tile
import box
import player
import box_slot

class Level(object):
	def __init__(self):
		self.tiles = [tile.Tile(32, 32), tile.Tile(64, 32), tile.Tile(96, 32)]
		self.boxes_slots = [box_slot.BoxSlot(96, 32)]
		self.boxes = [box.Box(64, 32)]
		self.player = player.Player(32, 32)
	
	def draw(self, surface):
		for t in self.tiles:
			t.draw(surface)
		
		for bs in self.boxes_slots:
			bs.draw(surface)

		for b in self.boxes:
			b.draw(surface)
		
		self.player.draw(surface)