import unittest
from selenium.webdriver.common.by import By
import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class MyTestCase_search_function(unittest.TestCase):

    def setUp(self):
        # TO INITIATE HEADLESS BROWSER
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        # TO INITIATE HEADLESS BROWSER

        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.set_page_load_timeout(25)
        self.driver.maximize_window()
        print("--------------------------------")
        print("Test Environment Created")
        print("Run began at :" + str(datetime.datetime.now()))

    def test_search_dress(self):

        self.driver.get("http://automationpractice.com/index.php")

        search_text_field = self.driver.find_element_by_xpath("//*[@id='search_query_top']")
        search_text_field.send_keys("Dress")
        search_button = self.driver.find_element_by_css_selector("#searchbox > button").click()
        current_page_source = self.driver.page_source

        if "Dress" in current_page_source:
            print("Dress search appears when searched using the search function")
        else:
            print("Dress search doesn't appears when searched using the search function")

        sleep(5)

        self.driver.back()

    def test_search_shirt(self):

        self.driver.get("http://automationpractice.com/index.php")


        search_text_field = self.driver.find_element_by_xpath("//*[@id='search_query_top']")
        search_text_field.send_keys("Shirt")
        search_button = self.driver.find_element_by_css_selector("#searchbox > button").click()
        sleep(3)
        current_page_source = self.driver.page_source

        if "Shirt" in current_page_source:
            print("Shirt search appears when searched using the search function")
        else:
            print("Shirt search doesn't appears when searched using the search function")

    def tearDown(self):

        if self.driver != None:
           print("--------------------------------")
           print("Test Environment Destroyed")
           print("Run completed at :" + str(datetime.datetime.now()))
           self.driver.close()




if __name__ == '__main__':
    unittest.main()
