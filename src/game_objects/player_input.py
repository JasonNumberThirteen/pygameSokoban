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
		if self.player.can_move_to(level, 0, -1):
			self.player.y -= 1

			self.player.move_box(level, 0, -1)
			self.gm.on_player_move(self.player)
			ui.on_player_move()
	
	def on_down_press(self, level, ui):
		if self.player.can_move_to(level, 0, 1):
			self.player.y += 1

			self.player.move_box(level, 0, 1)
			self.gm.on_player_move(self.player)
			ui.on_player_move()
	
	def on_left_press(self, level, ui):
		if self.player.can_move_to(level, -1, 0):
			self.player.x -= 1

			self.player.move_box(level, -1, 0)
			self.gm.on_player_move(self.player)
			ui.on_player_move()
	
	def on_right_press(self, level, ui):
		if self.player.can_move_to(level, 1, 0):
			self.player.x += 1

			self.player.move_box(level, 1, 0)
			self.gm.on_player_move(self.player)
			ui.on_player_move()
	
	def on_restart_press(self, level, ui):
		if self.player.moves > 0:
			self.gm.restart_level()
			ui.on_level_start()
	
	def pressed_key(self, event, key):
		return event.key == ord(key)