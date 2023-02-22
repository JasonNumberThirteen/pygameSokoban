import text

class GameUI(object):
	def __init__(self, moves):
		self.moves_counter = text.Text("Moves: " + str(moves), 4, 4, (32, 32, 32))

	def draw(self, surface):
		self.moves_counter.draw(surface)