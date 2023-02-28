import level

class GameManager(object):
	def __init__(self):
		self.level = level.Level(self, "level1.csv", 1)
		self.ui = None

	def on_player_move(self, player):
		player.moves += 1

		self.ui.update_moves_counter()
		self.ui.update_boxes_counter()

	def restart_level(self):
		self.level.build(self, "level1.csv")
		self.on_level_start()
	
	def on_level_start(self):
		self.ui.update_moves_counter()
		self.ui.update_boxes_counter()
	
	def completed_level(self):
		return self.level.inserted_boxes() == len(self.level.boxes_slots)