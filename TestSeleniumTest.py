import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        
        SCROLL_PAUSE_TIME = 0.5
        driver = self.driver
        driver.get("https://nik.bot.nu/brws.html#list/tag:berserk")

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

      
        elems = driver.find_element_by_class_name("image-block")
        print(elems)


    def tearDown(self):
        self.driver.close()

        
unittest.main()
