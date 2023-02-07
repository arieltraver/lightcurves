
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
    if percent:
        return percentage
    else:
        return ratio



