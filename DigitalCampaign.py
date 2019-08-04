class DigitalCampaign:
    '''
    This class constructs a digital campaign object tied to a campaign ID,
    campaign name, flight days, days passed, budget and spend.
    '''
    
    def __init__(self, cid = '', campaignName = '', flightDays = 0,
                 daysPassed = 0, budget = 0.0, spend = 0.0):
        '''
        Initializer with default values.
        '''
        self.__cid = cid # Campaign ID
        self.__campaignName = campaignName # Name of the campaign
        self.flightDays = flightDays # Number of days campaign is set to run
        self.daysPassed = daysPassed # Number of days that have passed so far
        self.budget = budget # The amount the campaign is allotted to spend
        self.spend = spend # The amount the campaign has spent so far
        
    def getCid(self):
        '''
        Returns the digital campaign ID as a string.
        '''
        return self.__cid

    def getCampaignName(self):
        '''
        Returns the digital campaign name as a string.
        '''
        return self.__campaignName

    def getFlightDays(self):
        '''
        Returns the total number of days the campaign is set to run as
        an integer.
        '''
        return self.flightDays

    def getDaysPassed(self):
        '''
        Returns the total number of days the campaign has run so far since
        the start as an integer.
        '''
        return self.daysPassed

    def getBudget(self):
        '''
        Returns the total budget the campaign has to spend as a float.
        '''
        return self.budget

    def getSpend(self):
        '''
        Returns the total budget that has been spent so far as a float.
        '''
        return self.spend

    def __setCid(self, cid):
        '''
        Takes a string and sets the campaign ID for the digital campaign.
        '''
        self.__cid = cid

    def __setCampaignName(self, campaignName):
        '''
        Takes a string and sets the campaign name for the digital campaign.
        '''
        self.__campaignName = campaignName

    def setFlightDays(self, flightDays):
        '''
        Takes an integer and sets the total flight days for the campaign.
        '''
        self.flightDays = flightDays

    def setDaysPassed(self, daysPassed):
        '''
        Takes an integer and sets the total days that have passed.
        '''
        self.daysPassed = daysPassed

    def setBudget(self, budget):
        '''
        Takes a float and sets the total budget of the campaign.
        '''
        self.budget = budget

    def setSpend(self, spend):
        '''
        Takes a float and sets the total amount the campaign has spent
        so far.
        '''
        self.spend = spend

    def getFlightPace(self):
        '''
        Returns the percentage of the flight that campaign has been running.
        '''
        return self.daysPassed / self.flightDays * 100

    def getBudgetPace(self):
        '''
        Returns the percentage of the budget that has been spent so far.
        '''
        return self.spend / self.budget * 100
    
    def getOverallPace(self):
        '''
        Returns if the campaign is overpacing, underpacing or on pace.
        '''
        overall_pace = (self.getBudgetPace() - self.getFlightPace()) / \
                        self.getFlightPace() * 100
        if overall_pace > 5:
            return "overpacing"
        elif overall_pace < -5:
            return "underpacing"
        else:
            return "on pace"
        
    def getRecommendation(self):
        '''
        Returns budget recommendations for the rest of the campaign.
        '''
        budget_left = self.budget - self.spend
        days_left = self.flightDays - self.daysPassed
        if days_left <= 0:
            return "Campaign has ended. Request an extension."
        elif budget_left <= 0:
            return "Campaign is out of budget. Request more budget."
        else:
            return ("Spend ${:,.2f} per day ".format(budget_left / days_left) +
                    "for the rest of the campaign.")

    def __repr__(self):
        '''
        After evaluating digital campaign pacing, display results and 
        recommendations.
        '''
        return ("[CID {}] - {} is {}.\n".format(self.getCid(),
                self.getCampaignName(), self.getOverallPace()) +
                "Pace should be {:.2f}%. Current pace is {:.2f}%.\n".format(
                self.getFlightPace(), self.getBudgetPace()) +
                "Recommendation: {}\n".format(self.getRecommendation()))