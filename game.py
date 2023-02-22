import text
import level
import pygame
import constants

class Game(object):
	def __init__(self, width, height, title="Game Window"):
		pygame.init()
		pygame.display.set_caption(title)

		self.canvas = pygame.display.set_mode((width, height))
		self.is_running = True
		self.level_data = [[0, 1, 0, 1, 1], [1, 1, 4, 1, 3], [0, 0, 1, 1, 2]]
		self.level_one = level.Level(self.level_data)
		self.moves_counter = text.Text("Moves: " + str(self.level_one.player.moves), 4, 4, (32, 32, 32))

		while self.is_running:
			self.canvas.fill(constants.BACKGROUND_COLOR)
			self.level_one.draw(self.canvas)
			self.moves_counter.draw(self.canvas)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.is_running = False
				
				self.level_one.player.detect_input(event)

			pygame.display.update()

		pygame.quit()

	def loop(self):
		pass

	def detect_input(self):
		pass

	def update(self):
		pass

	def draw(self):
		pass