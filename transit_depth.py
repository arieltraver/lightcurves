#import numpy as np
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

def kepler_III_a(star_mass, planet_mass, P):
	return None
def kepler_III_star_mass(a, planet_mass, P):
	return None
def kepler_III_planet_mass(a, star_mass, P):
	return None
def kepler_III_P(a, star_mass, planet_mass):
	return None


class transit: #may eventually update to be a transit class, with separate kepler III methods.
	a = None #length of major axis of orbit
	star_mass = None #mass of star
	planet_mass = None #mass of planet
	P = None #orbital period
	knowns = {}
	
	#this is clunky, would be a use case for **kwargs.
	#for now, we are just putting them in by name
	#easier for non-python users probably.
	def __init__(self, a=None, star_mass=None, planet_mass=None, P=None, star_rad=None, planet_rad=None):
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
		self.star_rad = star_rad
		if star_rad is not None:
			self.knowns["star radius"] = star_rad
		self.planet_rad = planet_rad
		if planet_rad is not None:
			self.knowns["planet radius"] = planet_rad

	def __str__(self):
		return f"given values: {self.knowns}"

	def update(self, a=None, star_mass=None, planet_mass=None, P=None, star_rad=None, planet_rad=None):
		if a is not None:
			self.a = a
			self.knowns["major axis length"] = a
		if star_mass is not None:
			self.star_mass = star_mass
			self.knowns["star mass"] = star_mass
		if planet_mass is not None:
			self.planet_mass = planet_mass
			self.knowns["planet mass"] = planet_mass
		if P is not None:
			self.P = P
			self.knowns["orbital period"] = P
		if star_rad is not None:
			self.star_rad = star_rad
			self.knowns["star radius"] = star_rad
		if planet_rad is not None:
			self.planet_rad = planet_rad
			self.knowns["planet radius"] = planet_rad


trial_planet = transit(a=1, star_mass=1, P=1)
print(trial_planet)
trial_planet.update(star_rad = 2)
print(trial_planet)

