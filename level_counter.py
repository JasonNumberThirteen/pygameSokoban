import text

from constants import LEVEL_TEXT

class LevelCounter(text.Text):
	def __init__(self, level_number):
		super().__init__(LEVEL_TEXT + " " + str(level_number), 4, 4)
	
	def update(self, value):
		self.set_text(LEVEL_TEXT + " " + str(value))