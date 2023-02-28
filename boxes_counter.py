import text

from constants import (GAME_WIDTH, BOXES_TEXT)

class BoxesCounter(text.Text):
	def __init__(self, boxes):
		super().__init__(BOXES_TEXT + ": " + str(boxes), 4, 4)
	
	def update(self, value):
		self.set_text(BOXES_TEXT + ": " + str(value))

		self.rect = self.render.get_rect(centerx=GAME_WIDTH // 2)