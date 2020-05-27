# Digital Campaign Pacing Program

## Summary
This program reads a text file of digital campaign data that a user updates. It processes each line to evaulate the pacing and offer recommendations for each campaign. It determines if a campaign is overpacing, underpacing or on pace and suggests how much to spend each day for the rest of the flight. This program is useful for digital campaign managers who run multiple accounts and do not have time to calculate the pacing for each individual campaign as that would be time consuming. With this program, they can just update campaigndatafile.txt and the program will evaluate every campaign and display the pacing with recommendations.

## Overview
This was programmed using Python 3.7.
There is no need to download or install other modules to run this program.
This download includes:
- `DigitalCampaign.py` - Creates a digital campaign object to evaluate campaign pacing and provide recommendations.
- `campaign_days.py` - Contains functions that calculate the total flight days and days passed using the campaign's start and end dates.
- `test_module.py` - Runs tests for the campaign_days functions and some methods in the DigitalCampaign class.
- `campaigndatafile.txt` - A text file of campaign data.
- `PacingProgram.py` - Reads the campaigndatafile.txt and processes each line of campaign data and displays the results of the pacing.
     
## Instructions
>User is to update the text file `campaigndatafile.txt`. First row is a header row and is to be ignored. All proceeding lines should be campaign data (each campaign should be on a new line). The order of the data should follow the header and be separated by commas: Campaign ID, CampaignName, Start Date, End Date, Budget, and Spend.

>Once data is updated, run `PacingProgram.py`. This program will reach line of campaign data and split it into a list of strings. It will convert the Budget and Spend strings into floats as long as they are numeric. The program will call the functions in `campaign_days.py` (total_flight_days and days_passed), which will also convert the Start Date and End Date strings into dates as long as they are in the correct format mm/dd/yyyy. total_flight_days will return the total number of days between the start and end dates. days_passed will return the number of days that have passed since the campaign started. If the campaign has already ended, then it will just return the total flight days.

>After all the conversions are made, using the `DigitalCampaign` class, a digital campaign object will be created with the campaign data. The program will then display for each campaign the CID, name, pace and provide recommendations.

## Author
* Linda Fung - Project for CS 521
