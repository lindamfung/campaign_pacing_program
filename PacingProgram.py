import sys
from DigitalCampaign import DigitalCampaign
import campaign_days


if __name__ == '__main__':
    '''
    Opens a txt file named 'campaigndata2019', which stores all campaign data,
    and processes it to get the budget pacing of the campaigns.
    User is to update the file with campaign ID, campaign name, start date,
    end date, budget, and spend comma delimited.
    '''
    
    try:
        infile = open("campaigndatafile.txt", "r") # Open campaign data file
    except:
        print("File {} does not exist.".format(infile))
        sys.exit()
        
    # Read the header row and ignore
    line_read = infile.readline().rstrip("\n")
    
    # Read next line of campaign data
    line_read = infile.readline().rstrip("\n")

    while line_read != '':
        # Store campaign details in a list
        campaign_data_list = line_read.split(',')
        
        if len(campaign_data_list) != 6:
            print("Please enter the correct campaign data in the file.")
            sys.exit()
        try:
            # Convert budget and spend to float
            campaign_data_list[4] = float(campaign_data_list[4])
            campaign_data_list[5] = float(campaign_data_list[5])
        except:
            print("Please enter correct budget or spend amounts as floats.")
            sys.exit()
            
        # Calculate total flight days of campaign
        flightDays = campaign_days.total_flight_days(campaign_data_list[2],
                                                     campaign_data_list[3])
        
        # Calculate days passed since campaign started
        daysPassed = campaign_days.days_passed(campaign_data_list[2],
                                               campaign_data_list[3])
        
        # Create a digital campaign object
        digi_c = DigitalCampaign(campaign_data_list[0], 
                                 campaign_data_list[1],
                                 flightDays, daysPassed, 
                                 campaign_data_list[4],
                                 campaign_data_list[5])
        
        # Evaluate digital campaign data and display results
        print(digi_c)
        
        # Read next line of campaign data
        line_read = infile.readline().rstrip("\n")