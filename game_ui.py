import level_counter
import moves_counter
import boxes_counter
import press_any_key_text
import level_complete_text

class GameUI(object):
	def __init__(self, gm):
		self.gm = gm
		self.level_counter = level_counter.LevelCounter(gm.level_number)
		self.moves_counter = moves_counter.MovesCounter(gm.level.player.moves)
		self.boxes_counter = boxes_counter.BoxesCounter(gm.level)
		self.level_complete_text = level_complete_text.LevelCompleteText(gm)
		self.press_any_key_text = press_any_key_text.PressAnyKeyText(gm)

	def draw(self, surface):
		self.level_counter.draw(surface)
		self.moves_counter.draw(surface)
		self.boxes_counter.draw(surface)
		self.level_complete_text.draw(surface)
		self.press_any_key_text.draw(surface)
	
	def update_on_start(self):
		self.level_counter.update(self.gm.level_number)
		self.update()
	
	def update(self):
		self.moves_counter.update(self.gm.level.player.moves)
		self.boxes_counter.update(self.gm.level)