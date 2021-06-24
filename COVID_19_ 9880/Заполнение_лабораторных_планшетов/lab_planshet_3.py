# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class LabPlanshet(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")	
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def genlog(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not os.path.exists("Logs"):
            os.mkdir("Logs")
        handler = logging.FileHandler(str('logs/' + (time.strftime('''%d.%m.%Y_%H.%M_''', (time.localtime())))  + 'lab_planshet_3.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.lab_planshet()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')     
    
    def test_lab_planshet(self):
        self.genlog()
        
    def lab_planshet(self):
        driver = self.driver
        barcode1 = "7800560977"
        barcode2 = "7800560978"
        barcode3 = "7800560979"
        iss1 = u"321Х24"
        iss2 = u"321Х25"
        iss3 = u"321Х26"
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml#")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector("a.submenu-marker > div.layout-tabmenu-tooltip > div.layout-tabmenu-tooltip-text").click()
        driver.find_element_by_css_selector("#j_id2\:DynamicMenuItem-138 > a").click()
        driver.find_element_by_id("barcodeForm:j_idt86").click()
        driver.find_element_by_id("barcodeForm:j_idt86").click()
        driver.find_element_by_css_selector("td").click()
        driver.find_element_by_id("barcodeForm:j_idt86").clear()
        driver.find_element_by_id("barcodeForm:j_idt86").send_keys(barcode1)
        driver.find_element_by_id("barcodeForm:j_idt86").send_keys(Keys.ENTER)
        time.sleep(6)
        assert driver.find_element_by_css_selector("#tabletForm\:tube_1_content > span.content-value").text == iss1
        driver.find_element_by_id("barcodeForm:j_idt86").clear()
        driver.find_element_by_id("barcodeForm:j_idt86").send_keys(barcode2)
        driver.find_element_by_id("barcodeForm:j_idt86").send_keys(Keys.ENTER)
        time.sleep(6)
        assert driver.find_element_by_css_selector("#tabletForm\:tube_2_content > span.content-value").text == iss2
        driver.find_element_by_id("barcodeForm:j_idt86").clear()
        driver.find_element_by_id("barcodeForm:j_idt86").send_keys(barcode3)
        driver.find_element_by_id("barcodeForm:j_idt86").send_keys(Keys.ENTER)
        time.sleep(6)
        assert driver.find_element_by_css_selector("#tabletForm\:tube_3_content > span.content-value").text == iss3
        driver.find_element_by_css_selector("#buttonsForm\:j_idt78")
        driver.find_element_by_css_selector("#buttonsForm\:j_idt79")
               
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

if __name__ == "__main__":
    unittest.main()
