# imports for importing files
from google.colab import files
import io
# imports for reading in data files and plotting
# note in Colab can't use interactive plots with matplotlib so plotly instead
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

"""
transit_depth
---parameters: 
	--- star_rad (radius of star), planet_rad (radius of planet)
	--- percent: default true, return val as a percentage (as opposed to decimal)
---output: percentage depth
---possible use: print(transit_depth(100, 2, percent=False))
"""

'''author: Kim  McLeod'''
# Make a push button for uploading files
# Run the cell then push the button
uploaded = files.upload()
# Take your favorite uploaded file and read it into a pandas data frame
# USER: put in the name of your file here
df = pd.read_csv(io.BytesIO(uploaded['lightcurves.csv']),)

# This will show you what the frame looks like
# Check to see that the columns look like you think they should!
#     Note: NaN means not a number
df.drop(" Corrected Flux", inplace=True, axis=1)
df
# This will make a nice interactive plot
# From the plot you can zoom, pan, and save as a png
#
# Note that the label for the second column starts with a space in this case
# because the .csv column first line was BJD - 2454833, Corrected Flux,
# with a space after the first comma
fig = px.scatter(data_frame=df, x=df.index, y="BJD - 2454833", width=1000, height=800)
fig.show()

# If you want to try the features below, remove the two """
# Nice option for changing labels and titles

fig.update_layout(
    title="Plot Title",
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",
    legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)


# add some text and arrows
fig.add_annotation(x=3440, y=1.025,
            text="Text annotation with arrow",
            showarrow=True,
            arrowhead=1)
fig.add_annotation(x=3450, y=0.99,
            text="Text annotation without arrow",
            showarrow=False,
            yshift=10)



# a way to add points and lines to an existing plot
fig.add_trace(go.Scatter(
    x=[3440,3440],    # x position of first and second point
    y=[1,1.008],      # y position of first and second point 
    name="transit 2"
))


#the plan:
#transit class contains all possible values about a transit related to our equations
#it stores a list of lists
#each list contains the variables needed in an equation
#every time you give a transit object a new value, it checks each equation to see if it can find more new values
#it does this recursively until it's done finding new values, and updates them for you
###perhaps make the auto-updating optional ("new value for {value} found from equation {name}, update?")
###small problem: removing a value may be difficult, as it would have to backtrack somehow.


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