# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

class Barcode1(unittest.TestCase):

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
        driver.find_element(By.CSS_SELECTOR,"span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element(By.CSS_SELECTOR,"#filtersform\:j_idt85_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"filtersform:j_idt87").click()
        time.sleep(30)
        driver.find_elements(By.CSS_SELECTOR,
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(20)
        driver.find_elements(By.CSS_SELECTOR,
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-first.ui-state-default.ui-corner-all")[0].click()
        time.sleep(20)
        #wait = WebDriverWait(driver, 200)
        #element = wait.until(EC.element_to_be_clickable((By.ID, '#tableForm\:main-table\:j_id5_input')))
        driver.find_element(By.CSS_SELECTOR,"#filtersform\:barcode-number").click()
        driver.find_element(By.CSS_SELECTOR,"#filtersform\:barcode-number").clear()
        driver.find_element(By.CSS_SELECTOR,"#filtersform\:barcode-number").send_keys("7800651936")
        driver.find_element(By.CSS_SELECTOR,"#filtersform\:barcode-number").send_keys(Keys.ENTER)
        time.sleep(10)
        driver.find_element(By.ID,"toolbarform:j_idt78").click()
        time.sleep(2)
        driver.find_element(By.ID,"genForm:j_idt106_input").click()
        driver.find_element(By.ID,"genForm:j_idt106_input").clear()
        driver.find_element(By.ID,"genForm:j_idt106_input").send_keys("15")
        time.sleep(2)
        driver.find_element(By.ID,"genForm:j_idt108").click()
        time.sleep(9)
        #driver.find_element(By.CSS_SELECTOR,"#growlForm\:growl_container > div.ui-growl-item-container.ui-state-highlight.ui-corner-all.ui-helper-hidden.ui-shadow.ui-growl-info > div > div.ui-growl-message > p")
        driver.find_element(By.ID,"toolbarform:j_idt78")

if __name__ == '__main__':
    unittest.main()

