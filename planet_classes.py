import pytest
import pandas as pd

class planet():
	def __init__(self, name, color = "blue", radius = 1):
		self.color = color
		self.radius = radius
		self.name = name
		self.moon_list = []
class moon():
	def __init__(self, name, color = "white", radius = 1, tidally_locked = False, planet_companion = None):
		self.name = name
		self.color = color
		self.radius = radius
		self.tidally_locked = tidally_locked
		self.planet_companion = planet_companion

	def update_planet(self):
		self.planet_companion.moon_list.append(self)

def print_largest(pl):
	largest = None
	for moon in pl.moon_list:
		if largest is None:
			largest = moon
		else:
			if largest.radius < moon.radius: largest = moon
	if largest is not None:
		print(f"The largest moon of {pl.name} is {largest.name}")

df = pd.read_csv('planet_data.csv', index_col = 'eName')
df = df[['isPlanet', 'meanRadius', 'orbit_type', 'orbits']]



planet_dictionary = dict()
moon_dictionary = dict()

for index, row in df.iterrows():
	if row['isPlanet'] is True:
		planet_dictionary[index] = planet(name = index, radius = row['meanRadius'])


for index, row in df.iterrows():
	if row ['isPlanet'] is False and row['orbit_type'] == 'secondary':
		planet_name = row['orbits']
		if planet_name in planet_dictionary:
			moon_dictionary[index] = moon(name = index, radius = row['meanRadius'], planet_companion = planet_dictionary[planet_name])

for m in moon_dictionary.values():
	m.update_planet()

for key, val in planet_dictionary.items():
	print(key, val.radius)

for key, val in moon_dictionary.items():
	print(key, val.radius, val.planet_companion.name)

for key, val in planet_dictionary.items():
	print_largest(val)
	print(key, [moon.name for moon in val.moon_list])
