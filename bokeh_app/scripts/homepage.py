from bokeh.models import Panel, Tabs
from bokeh.models.widgets import PreText

def homepage_tab():

    def make_plot():
        p = PreText(text="""
        We are group 10 in Visualization JBI100.
        
        The group members are:
        
        Kaloyan Videlov
        
        Mohamed Jahouh
        
        Fadi Shallah
        
        Stefan Stoev
        
        Jelle van Hees""",
                      width=500, height=100)

        p1 = PreText(text="""
        Our visualization project is part of the Brabant's Historical Information Center located
        in Den Bosch. The data we use is about people having lived in the Netherlands from at least 200 years, 
        resulting several million people.
        
        In the project we have included timelines, for marriages, births and deaths per year, word clouds for name  
        frequency for every 26 years and a male to female bar charts about people who were born and who died for 
        different time periods.
        
        This project is inspired by the work of Will Koehrsen.""",
                      width=700, height=100)

        # Creating a tab for each visualization
        tab = Panel(child=p, title="About Us")
        tab1 = Panel(child=p1, title="About the project")

        tabs = Tabs(tabs=[tab, tab1])

        return tabs

    tab = Panel(child=make_plot(), title='Home')

    return tab
