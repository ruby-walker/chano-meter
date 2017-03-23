import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.embed import file_html
from bokeh.resources import CDN

album = ["10 Day", "Acid Rap", "Coloring Book"]
song = ["Track 1", "Track 2", "Track 3", "Track 4", "Track 5", "Track 6", "Track 7", "Track 8", "Track 9", "Track 10", "Track 11", "Track 12", "Track 13", "Track 14"]
pointname = ["Point 1", "Point 2", "Point 3", "Point 4", "Point 5", "Point 6", "Point 7", "Point 8"]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
radii = [0, .5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0, 1, 1, 0, 0, 2.5, 0, 0, .5, 0, 1.5, .5, 0.0, 0, 0, .5,0,0,0,0,0,0,0,.5,0,.5,0]
colors = ["#033B6B", "#0C4777", "#165384", "#206091", "#296C9D", "#3379AA", "#3D85B7", "#4792C4", "#599ECA", "#6BAAD1", "#7DB6D8", "#8FC2DF", "#A1CEE6", "#B4DAED", "#BF467B", "#B7427B", "#B03E7B", "#A93A7C", "#A2367C", "#9A327D", "#932F7D", "#8C2B7D", "#85277E", "#7D237E", "#761F7F", "#6F1B7F", "#681880", "#FA416C", "#F8476B", "#F74D6A", "#F65369", "#F55A68", "#F46067", "#F36666", "#F26D66", "#F47766", "#F68267", "#F88D67", "#FA9768", "#FCA268", "#FFAD69"]

TOOLS="crosshair, save"

p = figure(tools=TOOLS, title="Occurences of the words 'killed', 'murdered', 'death', 'died', 'shot', and 'shooting' in Chance the Rapper Songs",  y_range=album, x_range=song, plot_width=1000)
p.xgrid.grid_line_color = None

p.scatter(x, y, radius=radii, fill_color=colors, line_color=None, fill_alpha=.9)

output_file("death-final.html", title="color_scatter.py example")

html = file_html(p, CDN, "my plot")

show(p)
