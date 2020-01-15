# Importing all relevant packages
import pandas as pd

# os methods for manipulating paths
from os.path import dirname, join

# Bokeh basics
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

# Each tab is drawn by one script
from scripts.timeline import timeline_tab
from scripts.homepage import homepage_tab
from scripts.stacked_bars import stacked_bars
# TODO: include all scripts

# Read data into dataframes
birth = pd.read_csv(join(dirname(__file__), 'data', 'Birth.csv'))
death = pd.read_csv(join(dirname(__file__), 'data', 'Death.csv'))
marriage = pd.read_csv(join(dirname(__file__), 'data', 'Marriage.csv'))

# Create each of the tabs
tab = homepage_tab()
tab1 = timeline_tab(birth, marriage, death)
tab2 = stacked_bars(birth, death)
# TODO: fix the tabs with 2 parameters

# Put all the tabs into one application
tabs = Tabs(tabs = [tab, tab1, tab2])

# Put the tabs in the current document for display
curdoc().add_root(tabs)