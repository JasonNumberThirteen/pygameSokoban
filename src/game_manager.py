import src.level as level

from src.constants import (LEVEL_FILES_FOLDER, LEVEL_FILES)

class GameManager(object):
	def __init__(self):
		self.level_number = 1
		self.level = level.Level(self, self.current_level_data())

	def advance_to_next_level(self):
		self.level_number += 1

		self.restart_level()

	def restart_level(self):
		self.level.build(self, self.current_level_data())
	
	def it_is_the_last_level(self):
		return self.level_number == len(LEVEL_FILES)
	
	def completed_level(self):
		return self.level.inserted_boxes() == len(self.level.boxes_slots)
	
	def current_level_data(self):
		return LEVEL_FILES_FOLDER + "/" + LEVEL_FILES[self.level_number - 1]