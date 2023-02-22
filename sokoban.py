import pygame
import level
import constants

def main():
	pygame.init()
	pygame.display.set_caption(constants.GAME_TITLE)

	canvas = pygame.display.set_mode(constants.BASE_RESOLUTION)
	is_running = True
	level_data = [[0, 1, 0, 1, 1], [1, 1, 4, 1, 3], [0, 0, 1, 1, 2]]
	level_one = level.Level(level_data)

	while is_running:
		canvas.fill(constants.BACKGROUND_COLOR)
		level_one.draw(canvas)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = False
			
			level_one.player.detect_input(event)

		pygame.display.update()

	pygame.quit()

if __name__ == "__main__":
	main()