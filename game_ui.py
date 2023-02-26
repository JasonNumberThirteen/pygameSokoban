import text
import constants

class GameUI(object):
	def __init__(self):
		self.level_counter = text.Text("", 4, 4, (32, 32, 32))
		self.moves_counter = text.Text("", 4, 4, (32, 32, 32))
		self.boxes_counter = text.Text("", 4, 4, (32, 32, 32))

	def draw(self, surface):
		self.level_counter.draw(surface)
		self.moves_counter.draw(surface)
		self.boxes_counter.draw(surface)
	
	def update_moves_counter(self, moves):
		self.moves_counter.set_text("Moves: " + str(moves))

		self.moves_counter.rect.right = constants.GAME_WIDTH

	def update_boxes_counter(self, level):
		self.boxes_counter.set_text("Boxes: " + str(level.inserted_boxes()) + "/" + str(len(level.boxes_slots)))

		self.boxes_counter.rect = self.boxes_counter.render.get_rect(centerx=constants.GAME_WIDTH // 2)