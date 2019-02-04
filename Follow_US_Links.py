import unittest
from selenium.webdriver.common.by import By
import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class MyTestCase_Follow_Link(unittest.TestCase):

    def setUp(self):
        # TO INITIATE HEADLESS BROWSER
        #options = Options()
        #options.add_argument("--headless")
        #self.driver = webdriver.Chrome(options=options)
        # TO INITIATE HEADLESS BROWSER

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(35)
        self.driver.maximize_window()
        print("--------------------------------")
        print("Test Environment Created")
        print("Run began at :" + str(datetime.datetime.now()))


    def test_links_access(self):

        self.driver.get("http://automationpractice.com/index.php")
        self.assertEqual("My Store", self.driver.title)

        facebook_link = self.driver.find_element_by_css_selector("#social_block > ul > li.facebook > a").click()
        sleep(3)
        self.assertTrue("Selenium Framework Public group | Facebook", self.driver.title)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        window_before = self.driver.window_handles[0]
        self.driver.switch_to.window(window_before)
        sleep(3)
        twitter_link = self.driver.find_element_by_css_selector("#social_block > ul > li.twitter > a").click()
        sleep(3)
        self.assertTrue("Selenium Framework(@seleniumfrmwrk) | Facebook", self.driver.title)
        self.driver.back()


    def tearDown(self):

        if self.driver != None:
           print("--------------------------------")
           print("Test Environment Destroyed")
           print("Run completed at :" + str(datetime.datetime.now()))
           self.driver.close()


if __name__ == '__main__':
    unittest.main()
