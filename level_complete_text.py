import text

from constants import (GAME_WIDTH, GAME_HEIGHT, UI_TEXT_COLOR, UI_TEXT_FONT_SIZE)

class LevelCompleteText(text.Text):
	def __init__(self):
		super().__init__("LEVEL COMPLETE", 0, 0, UI_TEXT_COLOR, UI_TEXT_FONT_SIZE)

		self.rect = self.render.get_rect(center=(GAME_WIDTH // 2, GAME_HEIGHT // 2))