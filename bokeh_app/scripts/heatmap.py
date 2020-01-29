from math import pi
import pandas as pd
from bokeh.layouts import widgetbox, column
from bokeh.models import Panel, Tabs
from bokeh.io import show
from bokeh.models import LinearColorMapper, BasicTicker, PrintfTickFormatter, ColorBar
from bokeh.plotting import figure
from bokeh.sampledata.unemployment1948 import data
from bokeh.models.widgets import Slider
from bokeh.models import ColumnDataSource

def heatmap(birth_data):
    
    df_births = birth_data[['Day', 'Month', 'Year']]
    df_births = df_births.dropna()
    df_births = df_births.sort_values(by=['Year'])
    df_births = df_births.reset_index()
    df_births = df_births.drop(columns=['index'])
    df_births['Entry'] = 1
    df_births.Year = df_births.Year.astype(int)
    df_births.Day = df_births.Day.astype(int)
    df_births.Month = df_births.Month.astype(int)

    max_pal = df_births.groupby(['Year', 'Month'])['Entry'].value_counts().to_frame().max()
    min_pal = df_births.groupby(['Year', 'Month'])['Entry'].value_counts().to_frame().min()

    new_df = df_births.groupby(['Year', 'Month']).describe()
    new_df = new_df.Day['count'].to_frame()
    new_df=new_df.reset_index()


    years = list(new_df.Year.unique())
    months = list(new_df.Month.unique())
    years.sort()
    months.sort()
    colors = ["#75968f", "#a5bab7", "#c9d9d3", "#e2e2e2", "#dfccce", "#ddb7b1", "#cc7878", "#933b41", "#550b1d"]
    mapper = LinearColorMapper(palette=colors, low=int(min_pal), high=int(max_pal))
    test = df_births.groupby(['Year', 'Month'])['Entry'].value_counts()
    TOOLS = "hover,save,pan,box_zoom,reset,wheel_zoom"


    def make_plot():

        p = figure(title="Births Frequency per Month ({0} - {1})".format(years[0], years[-1]),
                   x_range=(min(years),max(years)), y_range=(min(months), max(months)),
                   x_axis_location="above", plot_width=1200, plot_height=600,
                   tools=TOOLS, toolbar_location='below',
                   tooltips=[('date', '@Month/@Year'), ('Births', '@count')])

        p.grid.grid_line_color = None
        p.axis.axis_line_color = None
        p.axis.major_tick_line_color = None
        p.axis.major_label_text_font_size = "5pt"
        p.axis.major_label_standoff = 0
        p.xaxis.major_label_orientation = pi / 3

        p.rect(x="Year", y="Month", width=1, height=1,
               source=new_df,
               fill_color={'field': 'count', 'transform': mapper},
               line_color=None)

        color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size="5pt",
                             ticker=BasicTicker(desired_num_ticks=len(colors)),
                             formatter=PrintfTickFormatter(format="%d"),
                             label_standoff=6, border_line_color=None, location=(0, 0))

        p.add_layout(color_bar, 'right')

        return p

    tab = Panel(child=make_plot(), title='Heatmap')
    
    return tab  
