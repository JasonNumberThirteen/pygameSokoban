from src.constants import (PLAYER_UP_MOVEMENT_KEY, PLAYER_DOWN_MOVEMENT_KEY, PLAYER_LEFT_MOVEMENT_KEY, PLAYER_RIGHT_MOVEMENT_KEY, LEVEL_RESTART_KEY)

class PlayerInput():
	def __init__(self, player, gm) -> None:
		self.gm = gm
		self.player = player
		self.callbacks = {PLAYER_UP_MOVEMENT_KEY: self.on_up_press, PLAYER_DOWN_MOVEMENT_KEY: self.on_down_press, PLAYER_LEFT_MOVEMENT_KEY: self.on_left_press, PLAYER_RIGHT_MOVEMENT_KEY: self.on_right_press, LEVEL_RESTART_KEY: self.on_restart_press}
	
	def detect_input(self, event, level, ui):
		for k, v in self.callbacks.items():
			if self.pressed_key(event, k):
				v(level, ui)

	def on_up_press(self, level, ui):
		self.on_move_press(level, ui, 0, -1)
	
	def on_down_press(self, level, ui):
		self.on_move_press(level, ui, 0, 1)
	
	def on_left_press(self, level, ui):
		self.on_move_press(level, ui, -1, 0)
	
	def on_right_press(self, level, ui):
		self.on_move_press(level, ui, 1, 0)
	
	def on_move_press(self, level, ui, offset_x, offset_y):
		if self.player.can_move_to(level, offset_x, offset_y):
			self.player.x += offset_x
			self.player.y += offset_y

			self.player.move_box(level, offset_x, offset_y)
			self.gm.on_player_move(self.player)
			ui.on_player_move()
	
	def on_restart_press(self, level, ui):
		if self.player.moves > 0:
			self.gm.restart_level()
			ui.on_level_start()
	
	def pressed_key(self, event, key):
		return event.key == ord(key)