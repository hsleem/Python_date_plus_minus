#!/usr/bin/python
#Owner: Houssein Zouhair Sleem
#version: 1
#Date: 20-12-2018

from datetime import datetime, date, timedelta
import sys

""" date_plus_function() accepts 2 arguments. current_date in "%b_%-d_%Y" (example "Dec 1 2018") format and received_no_of_days 
    (example 2. Positive integer). It adds received_no_of_days to current_date and return the result"""

def date_plus_function(current_date, received_no_of_days):
   next_date = current_date + timedelta(days=int(received_no_of_days))
   return next_date

""" date_minus_function() accepts 2 arguments. current_date in "%b_%-d_%Y" (example "Dec 1 2018") format and received_no_of_days 
    (example -2. Negative integer). It adds received_no_of_days to current_date and return the result"""

def date_minus_function(current_date, received_no_of_days):
   previous_date = current_date + timedelta(days=int(received_no_of_days))
   return previous_date



received_date = sys.argv[1] #First command line argument is saved in received_date variable.
received_no_of_days= sys.argv[2] #Second command line argument is saved in received_no_of_days variable.



try:
 str_to_int = int(received_no_of_days) #converting received_no_of_days variable from string to integer.
 str_to_date = datetime.strptime(received_date, "%Y_%b_%d") #converting received_date variable from string to date.

 #if str_to_int is positive, call date_plus_function and save the returned result in result variable
 if str_to_int > 0: 
   result  = date_plus_function(str_to_date, str_to_int)
   print result.strftime("%b_%-d_%Y")
#if str_to_int is negative, call date_minus_function and save the returned result in result variable
 elif str_to_int < 0: 
   result  = date_minus_function(str_to_date, str_to_int) 
   print result.strftime("%b_%-d_%Y")
 elif str_to_int == 0:
   print str_to_date.strftime("%b_%-d_%Y")
except:
 print ("Invalid Arguments' format")

   

