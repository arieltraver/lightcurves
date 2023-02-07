import numpy as np
"""
transit_depth
---parameters: 
	--- star_rad (radius of star), planet_rad (radius of planet)
	--- percent: default true, return val as a percentage (as opposed to decimal)
---output: percentage depth
---possible use: print(transit_depth(100, 2, percent=False))
"""
def transit_depth(star_rad, planet_rad, percent=True):
	pi = 3.14159
	a_star = 4 * pi * star_rad * star_rad
	a_planet = 4 * pi * planet_rad * planet_rad
	ratio = a_planet / a_star
	percentage = ratio * 100
	if percent is True:
		return percentage
	else:
		return ratio

class kepler_III:
	a = None #length of major axis of orbit
	star_mass = None #mass of star
	planet_mass = None #mass of planet
	P = None #orbital period
	knowns = {}

	def __init__(self, a=None, star_mass=None, planet_mass=None, P=None):
		self.knowns = {}
		self.a = a
		if a is not None:
			self.knowns["major axis length"] = a
		self.star_mass = star_mass
		if star_mass is not None:
			self.knowns["star mass"] = star_mass
		self.planet_mass = planet_mass
		if planet_mass is not None:
			self.knowns["planet mass"] = planet_mass
		self.P = P
		if P is not None:
			self.knowns["orbital period"] = P

	def __str__(self):
		return f"given values: {self.knowns}"
		

trial_planet = kepler_III(a=1, star_mass=1, P=1)
print(trial_planet)

