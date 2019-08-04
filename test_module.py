import unittest
from DigitalCampaign import DigitalCampaign
import campaign_days


class CampaignPaceTestCase(unittest.TestCase):
    '''
    Tests for campaign_days.py: total_flight_days and days_passed and
    DigitalCampaign: getFlightPace, getBudgetPace, getOverallPace, and
    getRecommendation.
    '''

    def test_flight_days(self):
        '''
        Is total flight days between 03/01/2019 and 03/31/2019 = 31?
        '''
        self.assertEqual(campaign_days.total_flight_days("03/01/2019", 
                                                         "03/31/2019"), 31)
        
    def test_days_passed(self):
        '''
        Is total days passed between 03/01/2019 and yesterday = 9?
        Result passed test as of Sunday March 10, 2019. Testing this at a 
        different day will fail test.
        '''
        self.assertEqual(campaign_days.days_passed("03/01/2019",
                                                   "03/31/2019"), 9)
        # If campaign has already ended, days_passed should return
        # total flight days
        self.assertEqual(campaign_days.days_passed("2/1/2019", 
                                                   "2/28/2019"), 28)
        
    def test_flight_pace(self):
        '''
        Test the getFlightPace method in DigitalCampaign class.
        '''
        digi_c = DigitalCampaign("10101", "Test_Campaign", 31, 15, 200000.00, 
                                 100000.00)
        self.assertAlmostEqual(digi_c.getFlightPace(), 48.3870968)
        
    def test_budget_pace(self):
        '''
        Test the getBudgetPace method in DigitalCampaign class.
        '''
        digi_c = DigitalCampaign("10101", "Test_Campaign", 31, 15, 200000.00, 
                                 100000.00)
        self.assertEqual(digi_c.getBudgetPace(), 50.0)
        
    def test_overall_pace(self):
        '''
        Test the getOverallPace method in DigitalCampaign class.
        '''
        digi_c = DigitalCampaign("10101", "Test_Campaign", 31, 15, 200000.00, 
                                 100000.00)   
        self.assertEqual(digi_c.getOverallPace(), "on pace")
        
    def test_recommendation(self):
        '''
        Test the getRecommendation method in DigitalCampaign class.
        '''
        digi_c = DigitalCampaign("10101", "Test_Campaign", 31, 15, 200000.00, 
                                 100000.00) 
        self.assertEqual(digi_c.getRecommendation(), "Spend $6,250.00 per day "
                         + "for the rest of the campaign.")


if __name__ == '__main__':
    unittest.main()