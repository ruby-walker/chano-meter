import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool
from bokeh.embed import file_html
from bokeh.resources import CDN

album = ["10 Day", "Acid Rap", "Coloring Book"]
song = ["Track 1", "Track 2", "Track 3", "Track 4", "Track 5", "Track 6", "Track 7", "Track 8", "Track 9", "Track 10", "Track 11", "Track 12", "Track 13", "Track 14"]
pointname = ["Point 1", "Point 2", "Point 3", "Point 4", "Point 5", "Point 6", "Point 7", "Point 8"]
x = [2, 3, 6, 12, 13, 14, 1, 2, 3, 4, 5, 6, 8, 11, 12, 1, 2, 3, 5, 11, 13, 14]
y = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
radii = [.1, .4, .1, .1, .2, .1, .1, .1, .3, .6, .1, .1, .1, .1, .3, .3, .1, .2, .1, .3, 2.0, .3, .2]
#radii = [.05, .2, .05, .05, .1, .05, .05, .05, .15, .3, .05, .05, .05, .05, .15, .15, .05, .1, .05, .15, 1.0, .15, .1]

colors = ['#0C4777', '#165384', '#3379AA', '#8FC2DF', '#A1CEE6', '#B4DAED', '#681880', '#6F1B7F', '#761F7F', '#7D237E', '#85277E', '#8C2B7D', '#9A327D', '#B03E7B', '#B7427B', '#FA416C', '#F8476B', '#F74D6A', '#F55A68', '#F88D67', '#FCA268', '#FFAD69']

TOOLS="crosshair, save"

p = figure(tools=TOOLS, title="Occurences of the words 'God', 'Lord', or 'Jesus' in Chance the Rapper Songs",  y_range=album, x_range=song, plot_width=1000)
p.xgrid.grid_line_color = None

p.scatter(x, y, radius=radii, fill_color=colors, line_color=None, fill_alpha=.9)

output_file("god2.html", title="color_scatter.py example")

output_file("color_scatter.html", title="color_scatter.py example")

html = file_html(p, CDN, "my plot")

show(p)
