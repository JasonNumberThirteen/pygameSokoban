import pygame
import game_ui
import game_manager

from constants import BACKGROUND_COLOR

class Game(object):
	def __init__(self, width, height, title="Game Window"):
		pygame.init()
		pygame.display.set_caption(title)

		self.canvas = pygame.display.set_mode((width, height))
		self.is_running = True
		self.gm = game_manager.GameManager()
		self.ui = game_ui.GameUI(self.gm)

		self.gm.ui = self.ui
		game_icon = pygame.image.load("gameIcon.png")

		pygame.display.set_icon(game_icon)
		self.gm.on_level_start()
		self.loop()
		pygame.quit()

	def loop(self):
		while self.is_running:
			self.detect_input()
			self.update()
			self.draw()
			pygame.display.update()

	def detect_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.is_running = False

			if not self.gm.completed_level():
				self.gm.level.player.detect_input(event, self.gm.level)
			elif not self.gm.it_is_the_last_level() and event.type == pygame.KEYDOWN:
				self.gm.advance_to_next_level()

	def update(self):
		pass

	def draw(self):
		self.canvas.fill(BACKGROUND_COLOR)
		self.gm.level.draw(self.canvas)
		self.ui.draw(self.canvas)