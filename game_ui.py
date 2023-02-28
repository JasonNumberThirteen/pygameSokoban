import level_counter
import moves_counter
import boxes_counter

class GameUI(object):
	def __init__(self):
		self.level_counter = level_counter.LevelCounter(1)
		self.moves_counter = moves_counter.MovesCounter(0)
		self.boxes_counter = boxes_counter.BoxesCounter(0)

	def draw(self, surface):
		self.level_counter.draw(surface)
		self.moves_counter.draw(surface)
		self.boxes_counter.draw(surface)
	
	def update_moves_counter(self, moves):
		self.moves_counter.update(moves)

	def update_boxes_counter(self, level):
		self.boxes_counter.update(level.inserted_boxes())