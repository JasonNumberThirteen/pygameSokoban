import text

from constants import (GAME_WIDTH, GAME_HEIGHT, UI_TEXT_COLOR, UI_TEXT_FONT_SIZE)

class PressAnyKeyText(text.Text):
	def __init__(self, gm):
		super().__init__("Press any key to continue", 0, 0, UI_TEXT_COLOR, UI_TEXT_FONT_SIZE)

		self.rect = self.render.get_rect(centerx=GAME_WIDTH // 2, bottom=GAME_HEIGHT)
		self.gm = gm
	
	def draw(self, surface):
		if self.gm.completed_level():
			super().draw(surface)