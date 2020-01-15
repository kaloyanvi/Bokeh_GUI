# Bokeh Python GUI

Interactive Visualizations on the BHIC geneaological dataset. The data is stored in 11 XML files and can be downloaded at 
 https://opendata.picturae.com/organization/bhic
 For easier use the most relevant information has been saved in a CSV files.

Requirements:
* Python version >= 3.6
* bokeh version == 1.4.0
* Tornado version == 6.0.3

The application is in the "bokeh_app" folder. In order to run the application open a command prompt, make the current directory to the folder containing "bokeh_app" and run "bokeh serve --show bokeh_app/". This will run a local server and open the GUI in your browser.