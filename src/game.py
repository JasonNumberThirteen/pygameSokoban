import pygame
import src.game_ui as game_ui
import src.game_manager as game_manager

from src.constants import BACKGROUND_COLOR

class Game(object):
	def __init__(self, width, height, title="Game Window"):
		pygame.init()
		pygame.display.set_caption(title)

		self.canvas = pygame.display.set_mode((width, height))
		self.is_running = True
		self.gm = game_manager.GameManager()
		self.ui = game_ui.GameUI(self.gm)
		
		self.set_icon()
		self.loop()
		pygame.quit()
	
	def set_icon(self):
		game_icon = pygame.image.load("gameIcon.png")

		pygame.display.set_icon(game_icon)

	def loop(self):
		while self.is_running:
			self.detect_input()
			self.draw()
			pygame.display.update()

	def detect_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.is_running = False
			
			self.detect_input_during_game(event)
	
	def detect_input_during_game(self, event):
		gm = self.gm
		
		if not gm.completed_level():
			gm.level.player.detect_input(event, gm.level, self.ui)
		elif not gm.it_is_the_last_level() and event.type == pygame.KEYDOWN:
			gm.advance_to_next_level()
			self.ui.on_level_start()

	def draw(self):
		self.canvas.fill(BACKGROUND_COLOR)
		self.gm.level.draw(self.canvas)
		self.ui.draw(self.canvas)