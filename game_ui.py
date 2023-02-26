import text

class GameUI(object):
	def __init__(self, player):
		self.moves_counter = text.Text("Moves: " + str(player.moves), 4, 4, (32, 32, 32))

	def draw(self, surface):
		self.moves_counter.draw(surface)
	
	def update_moves_counter(self, moves):
		self.moves_counter.set_text("Moves: " + str(moves))