class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def has_the_same_position(self, point):
		return self.x == point.x and self.y == point.y