import pygame
import src.game_objects.point as point
import src.game_objects.player_input as player_input
import src.game_objects.shaded_circular_object as shaded_circular_object

from src.constants import (TILE_WIDTH, TILE_HEIGHT, PLAYER_COLOR, PLAYER_RADIUS, PLAYER_SHADE_COLOR, PLAYER_SHADE_OFFSET)

class Player(shaded_circular_object.ShadedCircularObject):
	def __init__(self, gm, x, y):
		super().__init__(x, y, PLAYER_COLOR, PLAYER_RADIUS, PLAYER_SHADE_COLOR)
		
		self.moves = 0
		self.input = player_input.PlayerInput(self, gm)
	
	def detect_input(self, event, level, ui):
		if event.type == pygame.KEYDOWN:
			self.input.detect_input(event, level, ui)
	
	def can_move_to(self, level, offset_x, offset_y):
		return level.tile_is_walkable(self, point.Point(offset_x, offset_y))
	
	def move_box(self, level, offset_x, offset_y):
		for b in level.boxes:
			if self.has_the_same_position(b):
				b.move(level, offset_x, offset_y)
	
	def offset_x(self):
		return TILE_WIDTH // 2
	
	def offset_y(self):
		return TILE_HEIGHT // 2
	
	def shade_offset(self):
		return PLAYER_SHADE_OFFSET