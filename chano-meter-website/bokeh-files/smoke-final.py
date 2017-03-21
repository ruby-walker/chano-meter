import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool
from bokeh.embed import file_html
from bokeh.resources import CDN

album = ["10 Day", "Acid Rap", "Coloring Book"]
song = ["Track 1", "Track 2", "Track 3", "Track 4", "Track 5", "Track 6", "Track 7", "Track 8", "Track 9", "Track 10", "Track 11", "Track 12", "Track 13", "Track 14"]
pointname = ["Point 1", "Point 2", "Point 3", "Point 4", "Point 5", "Point 6", "Point 7", "Point 8"]
x = [4, 3, 5, 10, 11, 4, 2, 12]
y = [3, 2, 2, 2, 2, 2, 1, 1]
radii = [.1, .2, .1, 3.0, .1, .4, .2, 1.9]
colors = ['#206091', '#761F7F', '#85277E', '#A93A7C', '#B03E7B', '#B7427B', '#F8476B', '#FA9768']

TOOLS="crosshair, save"

p = figure(tools=TOOLS, title="Occurences of the words 'smoke' or 'smoking' in Chance the Rapper Songs",  y_range=album, x_range=song, plot_width=1000)
p.xgrid.grid_line_color = None

p.scatter(x, y, radius=radii, fill_color=colors, line_color=None, fill_alpha=.9)

output_file("smoke.html", title="color_scatter.py example")

html = file_html(p, CDN, "my plot")

show(p)
