# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 00:26:51 2018

"""

# Functions    
def get_data_using_fun_lib():
    print ("----------->Inside external function lib")
    
def getholiday(date):
    holidaylist = listofholidays()
    for _ in holidaylist:
        if ( _ == date and holidaylist[_] == "Holiday" ):
            print ("Yes Holiday")
            break
        else: 
            print ("No Working Day! Go back to work.")
            break

def listofholidays():
    return {"10":"Holiday","11":"Working Day","12":"Working Day"}

# This import scope is Global
import datetime
def getcurrenttime():
    return datetime.datetime.now()