import level

from constants import LEVEL_FILES

class GameManager(object):
	def __init__(self):
		self.level_number = 1
		self.level = level.Level(self, LEVEL_FILES[self.level_number - 1])
		self.ui = None

	def on_player_move(self, player):
		player.moves += 1

		self.ui.update()

		if self.completed_level():
			self.on_level_complete()

	def restart_level(self):
		self.level.build(self, LEVEL_FILES[self.level_number - 1])
		self.on_level_start()
	
	def on_level_start(self):
		self.ui.update_on_start()
	
	def on_level_complete(self):
		self.ui.on_level_complete()
	
	def advance_to_next_level(self):
		self.level_number += 1
		self.restart_level()
	
	def it_is_the_last_level(self):
		return self.level_number == len(LEVEL_FILES)
	
	def completed_level(self):
		return self.level.inserted_boxes() == len(self.level.boxes_slots)