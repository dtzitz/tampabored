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




if __name__ == '__main__':  
    unittest.main(warnings='ignore')