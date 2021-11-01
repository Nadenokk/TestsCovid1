# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class ExpressTestStatus(unittest.TestCase):
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
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Express_test_status.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.express_test_status()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    
    
    def test_express_test_status(self):
        self.genlog()
    '''
    def test_express_status(self):
        driver = self.driver
        barcode = "7800560979"
        iss = u"10Х396522" # u - кодировка utf-8
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://rpn19.ru:9880/business/dashboard/dashboard.xhtml")
        #driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("borisova")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector("#j_idt66 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(10) > a > div").click()

        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys(barcode)
        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(10)
        assert driver.find_element_by_id("expressForm:j_idt77").text == iss

        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys("negative")
        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(5)
        #driver.find_element_by_css_selector("#growlForm\:growl_container > div > div > div.ui-growl-message > p")
        assert driver.find_element_by_css_selector("#expressForm\:j_idt90").text == iss
        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys(barcode)
        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(10)
        assert driver.find_element_by_css_selector("#expressForm\:j_idt77").text == iss
        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys("positive")
        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(5)
        #driver.find_element_by_css_selector("#growlForm\:growl_container > div > div > div.ui-growl-message > p")
        assert driver.find_element_by_css_selector("#expressForm\:j_idt82").text == iss
        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys("clear-lists")
        driver.find_element_by_css_selector("#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element_by_css_selector("#growlForm\:growl_container > div > div > div.ui-growl-message > p")
        #assert driver.find_element_by_css_selector("#expressForm:j_idt93").text != iss
        #assert driver.find_element_by_css_selector("#expressForm:j_idt85").text != iss
    
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
