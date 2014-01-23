#!/usr/bin/env python

#to use in GUI:
#import dataFeed
#dataFeed.dataFeed(ticker, start_date, end_date)
#see this file's main class for how to write parameters

import datetime
import matplotlib.finance as mplf



class dataFeed:
	def __init__(self, ticker, start_date, end_date):
		
		#query yahoo finance
		aList = mplf.quotes_historical_yahoo(ticker, start_date, end_date) 
		
		#print data
		for x in aList:
			#formats date
			print "Date:", datetime.datetime.fromordinal(int(x[0])) 
			print "Open:", x[1]
			print "Close:", x[2]
			print "High:", x[3]
			print "Low:", x[4]
			print "Volume:", x[5]
			print " "
	
	
	
#Main function
if __name__ == "__main__":
	#ticker is the string used to identiy a Company 'AAPL' is apple 
	ticker = 'AAPL'
	#dates to pull data from
	start_date = datetime.datetime(2014, 1, 10) #year, month, day
	end_date = datetime.datetime(2014, 1, 21)   #year, month, day
	dataFeed(ticker, start_date, end_date)
