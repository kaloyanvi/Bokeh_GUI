"""Importing all relevant packages."""
from bokeh.models import Panel, Tabs
from bokeh.plotting import figure
from bokeh.models.widgets import Slider
from bokeh.layouts import widgetbox, column
from bokeh.models import Slider, ColumnDataSource
from bokeh.plotting import figure, curdoc
from bokeh.core.properties import value
from bokeh.models.ranges import FactorRange
from bokeh.models import Panel, Tabs
import pandas as pd

"""Preprocessing the death data and adjusting the dataframe. Since, there are a few years in the beginning 
which have very little count, I consider them as outliers and that is why I have removed them. """

def timeline_tab(births, marriages, deaths):

    # Preprocessing the birth data
    df_year = births[["Year"]]
    df_births = df_year.dropna()
    year_freq = df_births.Year.value_counts().to_frame()  # new dataframe for births per year
    year_freq = year_freq.rename(columns={"Year": "Count"})
    year_freq["Year"] = year_freq.index
    year_freq.sort_values(by=['Year'], inplace=True)  # sorting the years in ascending order
    year_freq = year_freq.reset_index()
    year_freq = year_freq.drop(["index"], axis=1)
    year_freq["Year"] = year_freq["Year"].astype(int)
    year_freq = year_freq[year_freq["Count"]>50]  # removing years with less than 50 deaths
    year_freq = year_freq.reset_index()
    year_freq = year_freq.drop(["index"], axis=1)

    # Preprocessing the marriage data
    df_marriage = marriages[["Person id", "Connection", "Event Year"]]  # keeping only relevant variables
    df_marriage["Year"] = df_marriage["Event Year"]
    marriage_freq = df_marriage.Year.value_counts().to_frame()  # new dataframe for marriages per year
    marriage_freq = marriage_freq.rename(columns={"Year": "Count"})
    marriage_freq["Year"] = marriage_freq.index
    marriage_freq.sort_values(by=['Year'], inplace=True)  # sorting the years in ascending order
    marriage_freq = marriage_freq.reset_index()
    marriage_freq = marriage_freq.drop(["index"], axis=1)
    marriage_freq["Year"] = marriage_freq["Year"].astype(int)
    marriage_freq = marriage_freq[marriage_freq["Count"]>50]  # removing years with less than 50 marriages
    marriage_freq = marriage_freq.reset_index()
    marriage_freq = marriage_freq.drop(["index"], axis=1)

    # Preprocessing the death data
    df_death = deaths[["Year"]]
    df_death = df_death.dropna()  # removing all missing values
    death_freq = df_death.Year.value_counts().to_frame()  # new dataframe for deaths per year
    death_freq = death_freq.rename(columns={"Year": "Count"})
    death_freq["Year"] = death_freq.index
    death_freq.sort_values(by=['Year'], inplace=True)  # sorting the years in ascending order
    death_freq = death_freq.reset_index()
    death_freq = death_freq.drop(["index"], axis=1)
    death_freq["Year"] = death_freq["Year"].astype(int)
    death_freq = death_freq[death_freq["Count"]>50]  # removing years with less than 50 marriages
    death_freq = death_freq.reset_index()
    death_freq = death_freq.drop(["index"], axis=1)

    # Putting the dataframes into lists
    years = year_freq["Year"].tolist()
    year_counts = year_freq["Count"].tolist()
    marriages = marriage_freq["Year"].tolist()
    marriage_counts = marriage_freq["Count"].tolist()
    deaths = death_freq["Year"].tolist()
    death_counts = death_freq["Count"].tolist()

    def make_plot():

        colors = ["#669acc", "#cc8f66", '#66cc72', '#ccc669', '#b266cc']

        # Plot for births per year
        data1 = {'years':years,
                'year_counts':year_counts,
                'color': ["#669acc" for i in range(len(years))]}

        source1 = ColumnDataSource(data=data1)


        TOOLTIPS1 = [
            ("year", "@years"),
            ("count", "@year_counts"),
        ]
        p = figure(title="Timeline of births every year", toolbar_location=None, tools=["hover", 'tap'], tooltips=TOOLTIPS1,
                   plot_height=700, plot_width=1200, y_axis_label = "Number of people", x_axis_label = "Year")
        p.vbar(x='years', top='year_counts', width=0.7, source=source1, color='color')
        p.xgrid.grid_line_color = None
        p.y_range.start = 0

        data2 = {'marriages': marriages,
                 'marriage_counts': marriage_counts,
                 'color': ["#669acc" for i in range(len(marriages))]}

        source2 = ColumnDataSource(data=data2)

        TOOLTIPS2 = [
            ("year", "@marriages"),
            ("count", "@marriage_counts"),
        ]
        # Plot for marriages per year
        p1 = figure(title="Timeline of marriages every year",
                   toolbar_location=None, tools=["hover", 'tap'], tooltips=TOOLTIPS2, plot_height=700, plot_width=1200,
                   y_axis_label = "Number of people", x_axis_label = "Year")
        p1.vbar(x='marriages', top='marriage_counts', width=0.7, source=source2, color='color')
        p1.xgrid.grid_line_color = None
        p1.y_range.start = 0

        # Plot for deaths per year
        data3 = {'deaths': deaths,
                 'death_counts': death_counts,
                 'color': ["#669acc" for i in range(len(deaths))]}

        source3 = ColumnDataSource(data=data3)

        TOOLTIPS3 = [
            ("year", "@deaths"),
            ("count", "@death_counts"),
        ]
        p2 = figure(title="Timeline of deaths every year",
                   toolbar_location=None, tools=["hover", 'tap'], tooltips=TOOLTIPS3, plot_height=700, plot_width=1200,
                   y_axis_label = "Number of people", x_axis_label = "Year")
        p2.vbar(x='deaths', top='death_counts', width=0.7, source=source3, color='color')
        p2.xgrid.grid_line_color = None
        p2.y_range.start = 0

        slider = Slider(start=0, end=len(colors)-1, value=0, step=1, title="Color")

        #function to update axis range
        def update_axis(attrname, old, new):
            a=slider.value
            new_data = {'years':years,
                'year_counts':year_counts,
                'color': [colors[a] for i in range(108)]}
            source1.data = new_data

        #Adding fucntion to on_change
        slider.on_change('value', update_axis)

        layout1 = column(p, widgetbox(slider))

        # Creating a tab for each visualization
        tab = Panel(child=layout1, title="Births per year")
        tab1= Panel(child=p1, title="Marriages per year")
        tab2= Panel(child=p2, title="Deaths per year")

        tabs = Tabs(tabs=[tab,tab1,tab2])

        return tabs

    tab = Panel(child=make_plot(), title='Timelines')

    return tab
