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
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(10) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Продукты\"] > span").click()
        driver.find_element(By.ID,"j_idt71:j_idt82").click()
        time.sleep(2)
        driver.find_element(By.ID,"productForm:prodName").click()
        driver.find_element(By.ID,"productForm:prodName").clear()
        driver.find_element(By.ID,"productForm:prodName").send_keys("Доставка")
        driver.find_element(By.ID,"productForm:j_idt141").click()
        time.sleep(6)
        driver.find_element(By.CSS_SELECTOR,"#j_idt71\:j_idt78 > div:nth-child(3) > span.ui-icon.ui-icon-triangle-1-s.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt71\:j_idt78_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.ID,"j_idt71:j_idt78").click()
        driver.find_element(By.ID,"j_idt71:j_idt78_1").click()
        driver.find_element(By.ID,"j_idt71:j_idt82").click()
        driver.find_element(By.ID,"productForm:prodName").send_keys("100inH")
        driver.find_element(By.ID,"productForm:j_idt141").click()
        driver.find_element(By.ID,"j_idt71:j_idt78").click()
        driver.find_element(By.ID,"j_idt71:j_idt78_2").click()
        driver.find_element(By.ID,"j_idt71:j_idt82").click()
        driver.find_element(By.ID,"productForm:prodName").send_keys("Вода с минераллами")
        driver.find_element(By.ID,"productForm:prodGroups").send_keys("ма")
        driver.find_element(By.XPATH,"//span[@id]/ul/li/span").click()
        time.sleep(10)





