import level

class GameManager(object):
	def __init__(self, ui):
		self.level = level.Level(self, "level1.csv", 1)
		self.ui = ui

		self.on_level_start()

	def on_player_move(self, player):
		player.moves += 1

		self.ui.update_moves_counter(player.moves)
		self.ui.update_boxes_counter(self.level)

	def restart_level(self):
		self.level.build(self, "level1.csv")
		self.on_level_start()
	
	def on_level_start(self):
		self.ui.level_counter.set_text("LEVEL " + str(self.level.number))
		self.ui.update_moves_counter(self.level.player.moves)
		self.ui.update_boxes_counter(self.level)
	
	def completed_level(self):
		return self.level.inserted_boxes() == len(self.level.boxes)