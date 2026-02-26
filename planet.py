class planet():
	def __init__(self, radius = 1, color = "blue"):
		self.radius = radius
		self.color = color
		print("Object created.")
	def expand(self, factor):
		self.radius = self.radius*factor
	def reset_color(self):
		self.color = "white"
	def set_color(self, new_color):
		self.color = new_color

mars = planet(2, "red")
print("Mars Radius: " + str(mars.radius))
print("Mars Color: " + str(mars.color))

earth = planet(1, "green")
print("Earth Radius: " + str(earth.radius))
print("Earth Color: " + str(earth.color))

neptune = planet(3)
print("Neptune Radius: " + str(neptune.radius))
print("Neptune Color: " + str(neptune.color))
