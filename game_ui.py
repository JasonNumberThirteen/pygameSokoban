import text
import constants

class GameUI(object):
	def __init__(self, moves, level_number):
		self.level_counter = text.Text("LEVEL " + str(level_number), 4, 4, (32, 32, 32))
		self.moves_counter = text.Text("Moves: " + str(moves), 4, 4, (32, 32, 32))

		self.moves_counter.rect.right = constants.GAME_WIDTH - 32

	def draw(self, surface):
		self.level_counter.draw(surface)
		self.moves_counter.draw(surface)
	
	def update_moves_counter(self, moves):
		self.moves_counter.set_text("Moves: " + str(moves))