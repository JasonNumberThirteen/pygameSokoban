import src.ui.text as text

from src.constants import LEVEL_TEXT

class LevelCounter(text.Text):
	def __init__(self, level_number):
		super().__init__(self.text_string(level_number), 4, 4)
	
	def update(self, level_number):
		self.set_text(self.text_string(level_number))
	
	def text_string(self, level_number):
		return LEVEL_TEXT + " " + str(level_number)