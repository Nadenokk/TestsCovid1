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
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml")
        #driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector("#j_idt68 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(11) > a > div").click()
        driver.find_element_by_css_selector(u"a[title=\"Штрих-коды\"] > span").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id9_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        time.sleep(50)
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id5_input").click()
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id5_input").clear()
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id5_input").send_keys("04.03.2021")
        driver.find_element_by_css_selector("body").click()
        time.sleep(7)
        driver.find_elements_by_css_selector("#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(7)
        driver.find_elements_by_css_selector("#tableForm\:main-table_paginator_bottom > a.ui-paginator-first.ui-state-default.ui-corner-all")[0].click()
        time.sleep(7)
        driver.find_element_by_id("toolbarform:j_idt79").click()
        time.sleep(2)
        driver.find_element_by_id("genForm:j_idt90_input").click()
        driver.find_element_by_id("genForm:j_idt90_input").clear()
        driver.find_element_by_id("genForm:j_idt90_input").send_keys("15")
        time.sleep(2)
        driver.find_element_by_id("genForm:j_idt92").click()
        time.sleep(7)
        #driver.find_element_by_css_selector("#growlForm\:growl_container > div.ui-growl-item-container.ui-state-highlight.ui-corner-all.ui-helper-hidden.ui-shadow.ui-growl-info > div > div.ui-growl-message > p")
        driver.find_element_by_id("toolbarform:j_idt79")
    
              
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)



if __name__ == '__main__':
    unittest.main()

