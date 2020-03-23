# Importing pandas and bokeh
import pandas
from bokeh.plotting import show
from bokeh.plotting import figure
from bokeh.plotting import output_file

# Reads the excel file
df = pandas.read_excel("verlegenhuken.xlsx")

# Prepare data
x = df["Temperature"]
y = df["Pressure"]

# Prepare output file
output_file("pressure.html")

# Set the resolution
plotting = figure(plot_width=500,
                  plot_height=500,
                  tools='pan')

# Set the custom text and fonts
# Title
plotting.title.text = "Temperature and Air Pressure"
plotting.title.text_color = "Gray"
plotting.title.text_font = "Arial"
plotting.title.text_font_style = "bold"

# Ticks
plotting.xaxis.minor_tick_line_color = None
plotting.yaxis.minor_tick_line_color = None

# Set labels
plotting.xaxis.axis_label = "Temperature (C)"
plotting.yaxis.axis_label = "Pressure (hPa)"

# Create circle plotting in figure object
plotting.circle(x, y, size=0.5)

# Write circle plotting in to figure object
show(plotting)