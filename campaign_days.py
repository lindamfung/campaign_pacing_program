import sys
from datetime import datetime as dt
from datetime import timedelta as td


def total_flight_days(startdate, enddate):
    '''
    This function calculates the total days between two dates.
    Start date must be before or the same as the end date.
    '''
    
    try:
        # Convert startdate string to date format
        startdate = dt.strptime(startdate, "%m/%d/%Y")
        # Convert enddate string to date format
        enddate = dt.strptime(enddate, "%m/%d/%Y")
    except:
        print("Please enter dates in proper format: mm/dd/yyyy.")
        sys.exit()
        
    # Check if end date is on or after the start date
    if enddate < startdate:
        print("End date must be the same or after the start date.")
        sys.exit()
        
    # Return the total flight days from start up to and including end date
    return (enddate - startdate + td(days = 1)).days


def days_passed(startdate, enddate):
    '''
    This function calculates the number of days that have passed up until
    yesterday.
    If the end date is before yesterday, only calculate the number of days
    up until the end date.
    '''
    
    try:
        # Check if startdate string is in proper date format
        startdate = dt.strptime(startdate, "%m/%d/%Y")
        # Check if enddate string is in proper date format
        enddate = dt.strptime(enddate, "%m/%d/%Y")
    except:
        print("Please enter dates in proper format: mm/dd/yyyy.")
        sys.exit()
        
    # Get yesterday's date
    yesterday = dt.today() - td(days = 1)
    
    if yesterday >= enddate:
        return total_flight_days(dt.strftime(startdate, "%m/%d/%Y"),
                                 dt.strftime(enddate, "%m/%d/%Y"))
    else:
        return total_flight_days(dt.strftime(startdate, "%m/%d/%Y"),
                                 dt.strftime(yesterday, "%m/%d/%Y"))

