#!/usr/bin/env python

import gtk
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from matplotlib.backends.backend_gtkagg import FigureCanvasGTKAgg as FigureCanvas

import matplotlib.pyplot as plt
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
	DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo, candlestick,\
	plot_day_summary, candlestick2




class GUI:
	wTree = gtk.Builder()

	def __init__(self):
		#import glade file
		self.builder = gtk.Builder()
		self.builder.add_from_file("GUI.glade")
		
		#define widgets from glade file
		self.windowMain = self.builder.get_object("windowMain")
		self.hbox1 = self.builder.get_object("hbox1")
		
		#a simple matplotlib graph
		f = Figure(figsize=(5,4), dpi=100)
		a = f.add_subplot(111)
		t = arange(0.0,3.0,0.01)
		s = sin(2*pi*t)
		a.plot(t,s)
		
		#convert graph to drawingArea which GTK can use
		graph = FigureCanvas(f)  # a gtk.DrawingArea

		#pack graph into GUI
		self.hbox1.pack_start(graph, True, True, 0)
		
		#connect events and show all widgets in GUI
		self.windowMain.connect("destroy", gtk.main_quit)
		self.windowMain.show_all()



#Main function
if __name__ == "__main__":
	GUI()
	gtk.main()


