import src.ui.level_counter as level_counter
import src.ui.moves_counter as moves_counter
import src.ui.boxes_counter as boxes_counter
import src.ui.press_any_key_text as press_any_key_text
import src.ui.level_complete_text as level_complete_text

class GameUI(object):
	def __init__(self, gm):
		self.gm = gm
		self.level_counter = level_counter.LevelCounter(gm.level_number)
		self.moves_counter = moves_counter.MovesCounter(gm.level.player.moves)
		self.boxes_counter = boxes_counter.BoxesCounter(gm.level)
		self.level_complete_text = level_complete_text.LevelCompleteText(gm)
		self.press_any_key_text = press_any_key_text.PressAnyKeyText(gm)

	def draw(self, surface):
		drawables = (self.level_counter, self.moves_counter, self.boxes_counter, self.level_complete_text, self.press_any_key_text)

		for d in drawables:
			d.draw(surface)
	
	def on_player_move(self):
		self.update()

		if self.gm.completed_level():
			self.on_level_complete()
	
	def update(self):
		self.moves_counter.update(self.gm.level.player.moves)
		self.boxes_counter.update(self.gm.level)
	
	def on_level_start(self):
		self.level_counter.update(self.gm.level_number)
		self.update()
	
	def on_level_complete(self):
		self.level_complete_text.on_level_complete()