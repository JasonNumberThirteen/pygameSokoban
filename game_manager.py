import level

class GameManager(object):
	def __init__(self):
		self.level = level.Level("level1.csv", 1)
	
	def completed_level(self):
		return self.level.inserted_boxes() == len(self.level.boxes)