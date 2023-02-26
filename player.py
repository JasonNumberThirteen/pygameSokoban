import pygame
import constants

class Player(object):
	def __init__(self, gm, x, y):
		self.gm = gm
		self.x = x
		self.y = y
		self.moves = 0
	
	def detect_input(self, event, level):
		if event.type == pygame.KEYDOWN:
			if self.can_move_up(event, level):
				self.y -= 1
				
				self.gm.on_player_move(self)
			elif self.can_move_down(event, level):
				self.y += 1
				
				self.gm.on_player_move(self)
			elif self.can_move_left(event, level):
				self.x -= 1
				
				self.gm.on_player_move(self)
			elif self.can_move_right(event, level):
				self.x += 1
				
				self.gm.on_player_move(self)
			elif self.can_reset_level(event):
				self.gm.restart_level()
	
	def can_move_up(self, event, level):
		return self.can_move_to(level, 0, -1) and self.pressed_key(event, constants.PLAYER_UP_MOVEMENT_KEY)
	
	def can_move_down(self, event, level):
		return self.can_move_to(level, 0, 1) and self.pressed_key(event, constants.PLAYER_DOWN_MOVEMENT_KEY)
	
	def can_move_left(self, event, level):
		return self.can_move_to(level, -1, 0) and self.pressed_key(event, constants.PLAYER_LEFT_MOVEMENT_KEY)
	
	def can_move_right(self, event, level):
		return self.can_move_to(level, 1, 0) and self.pressed_key(event, constants.PLAYER_RIGHT_MOVEMENT_KEY)
	
	def can_move_to(self, level, offset_x, offset_y):
		for t in level.tiles:
			if self.x + offset_x == t.x and self.y + offset_y == t.y:
				for b in level.boxes:
					if self.x + offset_x == b.x and self.y + offset_y == b.y:
						if b.can_be_moved(level, offset_x, offset_y):
							b.move(level, offset_x, offset_y)

							return True
						else:
							return False
				
				return True
		
		return False
	
	def can_reset_level(self, event):
		return self.moves > 0 and self.pressed_key(event, constants.LEVEL_RESTART_KEY)
	
	def pressed_key(self, event, key):
		return event.key == ord(key)
	
	def draw(self, surface):
		x = self.x*constants.TILE_WIDTH + constants.TILE_WIDTH // 2
		y = self.y*constants.TILE_HEIGHT + constants.TILE_HEIGHT // 2
		
		pygame.draw.circle(surface, constants.PLAYER_SHADE_COLOR, (x, y + constants.PLAYER_SHADE_OFFSET), constants.PLAYER_RADIUS)
		pygame.draw.circle(surface, constants.PLAYER_COLOR, (x, y), constants.PLAYER_RADIUS)
