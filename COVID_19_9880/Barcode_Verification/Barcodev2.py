# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class Barcode2(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")	
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.verificationErrors = []
        self.accept_next_alert = True
    '''    
    def genlog(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        path = "\Logs"
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Barcode.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.barcode()
        except Exception as e:
            logger.info('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    
        
    def test_barcode(self):
        self.genlog()
    '''
    def test_barcode(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        #driver.get("http://127.0.0.1:48080/business/dashboard/dashboard.xhtml")
        #driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,"#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(8) > a > div").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Поиск штрих-кодов\"] > span").click()
        #print (driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_paginator_bottom > span.ui-paginator-current").text)
        driver.find_element(By.ID,"filtersform:j_idt87").click()
        time.sleep(25)
        print (driver.find_element(By.XPATH,"//span[@class='ui-paginator-current']").text)
        
if __name__ == "__main__":
    unittest.main()