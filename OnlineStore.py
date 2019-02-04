import unittest
from selenium.webdriver.common.by import By
import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options





class MyTestCase_HomePage(unittest.TestCase):

    def setUp(self):
        # TO INITIATE HEADLESS BROWSER
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        # TO INITIATE HEADLESS BROWSER

        #self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(35)
        self.driver.maximize_window()
        print("--------------------------------")
        print("Test Environment Created")
        print("Run began at :" + str(datetime.datetime.now()))

    #TESTING MAJOR LINKS ON THE HOMEPAGE

    def test_Homepage_mainmenu(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.assertEqual("My Store", self.driver.title)

        Menu_Women = self.driver.find_element_by_css_selector("#block_top_menu > ul > li:nth-child(1) > a")
        ActionChains(self.driver).move_to_element(Menu_Women).perform()
        sleep(2)

        Menu_Dreses = self.driver.find_element_by_css_selector("#block_top_menu > ul > li:nth-child(2) > a")
        ActionChains(self.driver).move_to_element(Menu_Dreses).perform()
        sleep(2)

        Menu_T_Shirts = self.driver.find_element_by_css_selector("#block_top_menu > ul > li:nth-child(3) > a").click()
        sleep(1)
        self.driver.back()

        Contact_Us = self.driver.find_element_by_css_selector("#contact-link > a").click()
        self.assertEqual("Contact us - My Store", self.driver.title)
        current_page_source = self.driver.page_source
        #print(current_page_source)

        if "send a message" in current_page_source:
            print("SEND A MESSAGE Is Present")
        else:
            print("SEND A MESSAGE Is Not Present")

        sleep(2)

    def test_Sign_In(self):
        self.driver.get("http://automationpractice.com/index.php")
        sign_in = self.driver.find_element_by_css_selector("#header > div.nav > div > div > nav > div.header_user_info > a").click()
        self.assertEqual("Login - My Store", self.driver.title)
        self.driver.back()
        sleep(2)

    def test_Cart_button(self):
        self.driver.get("http://automationpractice.com/index.php")

        cart_button = self.driver.find_element_by_css_selector("#header > div:nth-child(3) > div > div > div:nth-child(3) > div > a").click()
        self.assertEqual("Order - My Store", self.driver.title)
        self.driver.back()

    #FOOTER LINKS

    def test_bottom_navigation_menu(self):
        self.driver.get("http://automationpractice.com/index.php")

        categories = self.driver.find_element_by_xpath("//*[@id='footer']/div/section[2]/div/div/ul/li/a").click()
        self.assertEqual("Women - My Store", self.driver.title)
        self.driver.back()

        specials = self.driver.find_element_by_xpath("//*[@id='block_various_links_footer']/ul/li[1]/a").click()
        self.assertEqual("Prices drop - My Store", self.driver.title)
        self.driver.back()

        new_products = self.driver.find_element_by_css_selector("#block_various_links_footer > ul > li:nth-child(2) > a").click()
        self.assertEqual("New products - My Store", self.driver.title)
        self.driver.back()

        best_sellers = self.driver.find_element_by_css_selector("#block_various_links_footer > ul > li:nth-child(3) > a").click()
        self.assertEqual("Best sales - My Store", self.driver.title)
        self.driver.back()

        our_stores = self.driver.find_element_by_css_selector("#block_various_links_footer > ul > li:nth-child(4) > a").click()
        self.assertEqual("Stores - My Store", self.driver.title)
        self.driver.back()

        contact_Us = self.driver.find_element_by_css_selector("#block_various_links_footer > ul > li:nth-child(5) > a").click()
        self.assertEqual("Contact us - My Store", self.driver.title)
        self.driver.back()

        terms = self.driver.find_element_by_css_selector("#block_various_links_footer > ul > li:nth-child(6) > a").click()
        self.assertEqual("Terms and conditions of use - My Store", self.driver.title)
        self.driver.back()

        about_us = self.driver.find_element_by_css_selector("#block_various_links_footer > ul > li:nth-child(7) > a").click()
        self.assertEqual("About us - My Store", self.driver.title)
        self.driver.back()

        sitemap = self.driver.find_element_by_css_selector("#block_various_links_footer > ul > li:nth-child(8) > a").click()
        self.assertEqual("Sitemap - My Store", self.driver.title)
        self.driver.back()

        my_orders = self.driver.find_element_by_css_selector("#footer > div > section:nth-child(7) > div > ul > li:nth-child(1) > a").click()
        self.assertEqual("Login - My Store", self.driver.title)
        self.driver.back()

        credit_slip = self.driver.find_element_by_xpath("//*[@id='footer']/div/section[5]/div/ul/li[2]/a").click()
        self.assertEqual("Login - My Store", self.driver.title)
        self.driver.back()

        address = self.driver.find_element_by_css_selector("#footer > div > section:nth-child(7) > div > ul > li:nth-child(3) > a").click()
        self.assertEqual("Login - My Store", self.driver.title)
        self.driver.back()

        personal_info = self.driver.find_element_by_css_selector("#footer > div > section:nth-child(7) > div > ul > li:nth-child(4) > a").click()
        self.assertEqual("Login - My Store", self.driver.title)




    def tearDown(self):

        if self.driver != None:
           print("--------------------------------")
           print("Test Environment Destroyed")
           print("Run completed at :" + str(datetime.datetime.now()))
           self.driver.close()






if __name__ == '__main__':
    unittest.main()
