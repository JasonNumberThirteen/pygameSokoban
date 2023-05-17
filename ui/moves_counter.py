import ui.text as text

from constants import (GAME_WIDTH, MOVES_TEXT)

class MovesCounter(text.Text):
	def __init__(self, moves):
		super().__init__(MOVES_TEXT + ": " + str(moves), 4, 4)
	
	def update(self, value):
		self.set_text(MOVES_TEXT + ": " + str(value))

		self.rect.right = GAME_WIDTH