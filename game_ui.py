import text
import constants

class GameUI(object):
	def __init__(self, moves, level):
		self.level_counter = text.Text("LEVEL " + str(level.number), 4, 4, (32, 32, 32))
		self.moves_counter = text.Text("Moves: " + str(moves), 4, 4, (32, 32, 32))
		self.boxes_counter = text.Text("", 4, 4, (32, 32, 32))

		self.moves_counter.rect.right = constants.GAME_WIDTH - 32
		self.boxes_counter.rect.right = constants.GAME_WIDTH // 2 - 32

		self.update_boxes_counter(level)

	def draw(self, surface):
		self.level_counter.draw(surface)
		self.moves_counter.draw(surface)
		self.boxes_counter.draw(surface)
	
	def update_moves_counter(self, moves):
		self.moves_counter.set_text("Moves: " + str(moves))

	def update_boxes_counter(self, level):
		self.boxes_counter.set_text("Boxes: " + str(level.inserted_boxes()) + "/" + str(len(level.boxes)))