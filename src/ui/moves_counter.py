import src.ui.text as text

from src.constants import (GAME_WIDTH, MOVES_TEXT)

class MovesCounter(text.Text):
	def __init__(self, moves):
		super().__init__(self.text_string(moves), 4, 4)
	
	def update(self, moves):
		self.set_text(self.text_string(moves))
		
		self.rect.right = GAME_WIDTH
	
	def text_string(self, moves):
		return MOVES_TEXT + ": " + str(moves)