#test the live site

from selenium import webdriver
import unittest


#homepage
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_homepage_has_browser_title(self):
        self.browser.get('https://pacific-everglades-16759.herokuapp.com/')
        self.assertIn('TampaBored', self.browser.title)
        self.tearDown()

#should contain cards with event info
#should contain list of events
#events should be organized by type
#events should be in order of start date
#events that have ended should not appear
#should contain at least one article


if __name__ == '__main__':  
    unittest.main(warnings='ignore')