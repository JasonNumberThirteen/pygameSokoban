import pygame
import src.game_objects.point as point
import src.game_objects.shaded_circular_object as shaded_circular_object

from src.constants import (PLAYER_UP_MOVEMENT_KEY, PLAYER_DOWN_MOVEMENT_KEY, PLAYER_LEFT_MOVEMENT_KEY, PLAYER_RIGHT_MOVEMENT_KEY, LEVEL_RESTART_KEY, TILE_WIDTH, TILE_HEIGHT, PLAYER_COLOR, PLAYER_RADIUS, PLAYER_SHADE_COLOR, PLAYER_SHADE_OFFSET)

class Player(shaded_circular_object.ShadedCircularObject):
	def __init__(self, gm, x, y):
		super().__init__(x, y, PLAYER_COLOR, PLAYER_RADIUS, PLAYER_SHADE_COLOR)
		
		self.gm = gm
		self.moves = 0
		self.input_callbacks = {PLAYER_UP_MOVEMENT_KEY: self.on_up_press, PLAYER_DOWN_MOVEMENT_KEY: self.on_down_press, PLAYER_LEFT_MOVEMENT_KEY: self.on_left_press, PLAYER_RIGHT_MOVEMENT_KEY: self.on_right_press}
	
	def detect_input(self, event, level, ui):
		if event.type == pygame.KEYDOWN:
			for k, v in self.input_callbacks.items():
				if self.pressed_key(event, k):
					v(level, ui)
	
	def on_up_press(self, level, ui):
		if self.can_move_to(level, 0, -1):
			self.y -= 1

			self.move_box(level, 0, -1)
			self.gm.on_player_move(self)
			ui.on_player_move()
	
	def on_down_press(self, level, ui):
		if self.can_move_to(level, 0, 1):
			self.y += 1

			self.move_box(level, 0, 1)
			self.gm.on_player_move(self)
			ui.on_player_move()
	
	def on_left_press(self, level, ui):
		if self.can_move_to(level, -1, 0):
			self.x -= 1

			self.move_box(level, -1, 0)
			self.gm.on_player_move(self)
			ui.on_player_move()
	
	def on_right_press(self, level, ui):
		if self.can_move_to(level, 1, 0):
			self.x += 1

			self.move_box(level, 1, 0)
			self.gm.on_player_move(self)
			ui.on_player_move()
	
	def can_move_up(self, event, level):
		return self.pressed_key(event, PLAYER_UP_MOVEMENT_KEY) and self.can_move_to(level, 0, -1)
	
	def can_move_down(self, event, level):
		return self.pressed_key(event, PLAYER_DOWN_MOVEMENT_KEY) and self.can_move_to(level, 0, 1)
	
	def can_move_left(self, event, level):
		return self.pressed_key(event, PLAYER_LEFT_MOVEMENT_KEY) and self.can_move_to(level, -1, 0)
	
	def can_move_right(self, event, level):
		return self.pressed_key(event, PLAYER_RIGHT_MOVEMENT_KEY) and self.can_move_to(level, 1, 0)
	
	def can_move_to(self, level, offset_x, offset_y):
		return level.tile_is_walkable(self, point.Point(offset_x, offset_y))
	
	def move_box(self, level, offset_x, offset_y):
		for b in level.boxes:
			if self.has_the_same_position(b):
				b.move(level, offset_x, offset_y)
	
	def can_reset_level(self, event):
		return self.moves > 0 and self.pressed_key(event, LEVEL_RESTART_KEY)
	
	def pressed_key(self, event, key):
		return event.key == ord(key)
	
	def offset_x(self):
		return TILE_WIDTH // 2
	
	def offset_y(self):
		return TILE_HEIGHT // 2
	
	def shade_offset(self):
		return PLAYER_SHADE_OFFSET