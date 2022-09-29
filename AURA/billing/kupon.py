# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException, NoSuchWindowException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver import ActionChains
import logging, os
import sys
import random
import string
from glob import glob
import os.path
from selenium.common.exceptions import WebDriverException

class Kupon(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    '''    
    def genlog(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not os.path.exists("Logs"):
            os.mkdir("Logs")
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Barcode.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.barcode()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    

    def test_barcode(self):
        self.genlog()
    '''

    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))
        return rand_string

    def test_kupon(self):
        driver = self.driver
        driver.get("http://auraep.ru:8180/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("tuilp")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("tuilp")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(8) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Купоны\"] > span").click()
        driver.find_element(By.ID,"tableForm:j_idt73").click()
        driver.find_element(By.ID,"itemForm:tabView:name").send_keys(self.generate_random_string())
        driver.find_element(By.CSS_SELECTOR,"span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element(By.XPATH,"//table[@id = 'itemForm:tabView:discountType']//span").click()
        driver.find_element(By.ID,"itemForm:tabView:discountValue").send_keys("50")
        driver.find_element(By.ID,"itemForm:tabView:startDate_input").send_keys("01.12.2020")
        driver.find_element(By.ID,"itemForm:tabView:finishDate_input").send_keys("01.12.2030")
        driver.find_element(By.ID,"itemForm:j_idt280").click()
        time.sleep(2)

        table_id = driver.find_element(By.ID,"tableForm:main-table_data")
        rows = table_id.find_elements(By.TAG_NAME, "tr")  # get all of the rows in the table
        for row in rows[1:]:
        # Get the columns (all the column 2)
            col = row.find_elements(By.TAG_NAME, "td")[0]  # note: index start from 0, 1 is col 2
            assert (driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").text != col.text)