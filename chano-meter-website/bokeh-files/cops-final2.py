import numpy as np

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool
from bokeh.embed import file_html
from bokeh.resources import CDN

album = ["10 Day", "Acid Rap", "Coloring Book"]
song = ["Track 1", "Track 2", "Track 3", "Track 4", "Track 5", "Track 6", "Track 7", "Track 8", "Track 9", "Track 10", "Track 11", "Track 12", "Track 13", "Track 14"]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
y = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
radii = [0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1.0, 0, 1, 0 ,0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0.0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0]
colors = ["#033B6B", "#0C4777", "#165384", "#206091", "#296C9D", "#3379AA", "#3D85B7", "#4792C4", "#599ECA", "#6BAAD1", "#7DB6D8", "#8FC2DF", "#A1CEE6", "#B4DAED", "#BF467B", "#B7427B", "#B03E7B", "#A93A7C", "#A2367C", "#9A327D", "#932F7D", "#8C2B7D", "#85277E", "#7D237E", "#761F7F", "#6F1B7F", "#681880", #FFAD69", "#FDA368", "#FB9A68", "#F99167", "#F78867", "#F57F66", "#F37666", "#F26D66", "#F36567", "#F45E68", "#F65769", "#F74F6A", "#F8486B", "#FA416C"]

TOOLS="crosshair, save"

p = figure(tools=TOOLS, title="Occurences of the words 'smoke' or 'smoking' in Chance the Rapper Songs",  y_range=album, x_range=song, plot_width=1000)
p.xgrid.grid_line_color = None

p.scatter(x, y, radius=radii, fill_color=colors, line_color=None, fill_alpha=.9)

output_file("smoke.html", title="color_scatter.py example")

html = file_html(p, CDN, "my plot")

show(p)
