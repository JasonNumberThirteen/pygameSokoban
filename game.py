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
			
			self.level_one.player.detect_input(event)

	def update(self):
		pass

	def draw(self):
		self.canvas.fill(constants.BACKGROUND_COLOR)
		self.level_one.draw(self.canvas)
		self.moves_counter.draw(self.canvas)