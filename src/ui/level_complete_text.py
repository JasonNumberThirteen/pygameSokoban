import src.ui.text as text

from src.constants import (GAME_WIDTH, GAME_HEIGHT)

class LevelCompleteText(text.Text):
	def __init__(self, gm):
		super().__init__()
		
		self.gm = gm
	
	def draw(self, surface):
		if self.gm.completed_level():
			super().draw(surface)
	
	def on_level_complete(self):
		text = "LEVEL COMPLETE"
		
		if self.gm.it_is_the_last_level():
			text = "YOU WIN!!!"
		
		self.set_text(text, center=(GAME_WIDTH // 2, GAME_HEIGHT // 2))