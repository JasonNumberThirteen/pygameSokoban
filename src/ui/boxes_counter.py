import src.ui.text as text

from src.constants import (GAME_WIDTH, BOXES_TEXT)

class BoxesCounter(text.Text):
	def __init__(self, level):
		super().__init__(self.text_string(level), 4, 4)
	
	def update(self, level):
		self.set_text(self.text_string(level), centerx=GAME_WIDTH // 2)
	
	def text_string(self, level):
		inserted_boxes = str(level.inserted_boxes())
		all_boxes = str(len(level.boxes))
		
		return BOXES_TEXT + ": " + inserted_boxes + "/" + all_boxes