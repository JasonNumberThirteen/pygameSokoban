import level
import pygame
import game_ui
import constants

class Game(object):
	def __init__(self, width, height, title="Game Window"):
		pygame.init()
		pygame.display.set_caption(title)

		self.canvas = pygame.display.set_mode((width, height))
		self.is_running = True
		self.level = level.Level("level1.csv")
		self.ui = game_ui.GameUI(self.level.player.moves)

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
			
			self.level.player.detect_input(event)

	def update(self):
		pass

	def draw(self):
		self.canvas.fill(constants.BACKGROUND_COLOR)
		self.level.draw(self.canvas)
		self.ui.draw(self.canvas)