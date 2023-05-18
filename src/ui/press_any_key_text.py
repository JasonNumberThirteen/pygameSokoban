import src.ui.text as text

from src.constants import (GAME_WIDTH, GAME_HEIGHT)

class PressAnyKeyText(text.Text):
	def __init__(self, gm):
		super().__init__()
		self.set_text("Press any key to continue", centerx=GAME_WIDTH // 2, bottom=GAME_HEIGHT)
		
		self.gm = gm
	
	def draw(self, surface):
		if self.gm.completed_level() and not self.gm.it_is_the_last_level():
			super().draw(surface)