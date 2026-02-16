from planet_classes import *

def test_planet_creation():
	mars = planet("Mars", "Red", 3390)
	earth = planet("Earth", "Green", 6371)
	neptune = planet("Neptune", "Blue", 24622)

	assert mars.name == "Mars"
	assert mars.radius == 3390
	assert mars.moon_list == []

	assert earth.name == "Earth"
	assert earth.radius == 6371
	assert earth.moon_list == []

	assert neptune.name == "Neptune"
	assert neptune.radius == 24622
	assert neptune.moon_list == []

def test_moon_update_planet():
	mars = planet("Mars", radius = 3390)
	phobos = moon(name = "Phobos", color = "Brownish-Red", radius = 11, tidally_locked = True, planet_companion = mars)
	deimos = moon(name = "Deimos", color = "Reddish-Gray", radius = 6, tidally_locked = True, planet_companion = mars)

	phobos.update_planet()
	deimos.update_planet()

	assert phobos in mars.moon_list
	assert phobos.planet_companion == mars

	assert deimos in mars.moon_list
	assert deimos.planet_companion == mars

	assert len(mars.moon_list) == 2
