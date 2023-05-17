import ui.text as text

from constants import (GAME_WIDTH, BOXES_TEXT)

class BoxesCounter(text.Text):
	def __init__(self, level):
		super().__init__(BOXES_TEXT + ": " + str(level.inserted_boxes()) + "/" + str(len(level.boxes)), 4, 4)
	
	def update(self, level):
		self.set_text(BOXES_TEXT + ": " + str(level.inserted_boxes()) + "/" + str(len(level.boxes)))

		self.rect = self.render.get_rect(centerx=GAME_WIDTH // 2)