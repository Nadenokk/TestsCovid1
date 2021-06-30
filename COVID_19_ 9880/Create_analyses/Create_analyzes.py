# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class CreateAnalyzes(unittest.TestCase):
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
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Create_analyzes.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.create_analyzes()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')      
    
    def test_create_analyzes(self):
        self.genlog()
    '''
    def test_create_analyzes(self):
        driver = self.driver
        #driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml#")
        driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector("#j_idt68 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(6) > a > div").click()
        driver.find_element_by_id("toolbarform:j_idt76").click()

        #driver.find_element_by_css_selector("span.ui-button-icon-left ui-icon ui-c fa fa-plus").click()
        driver.find_element_by_id("itemForm:tabView:lastName").click()
        driver.find_element_by_id("itemForm:tabView:lastName").clear()
        driver.find_element_by_id("itemForm:tabView:lastName").send_keys(u"СаблинАн")
        driver.find_element_by_id("itemForm:tabView:firstName").click()
        driver.find_element_by_id("itemForm:tabView:firstName").clear()
        driver.find_element_by_id("itemForm:tabView:firstName").send_keys(u"Роман")
        driver.find_element_by_id("itemForm:tabView:patronymicName").click()
        driver.find_element_by_id("itemForm:tabView:patronymicName").clear()
        driver.find_element_by_id("itemForm:tabView:patronymicName").send_keys(u"Евгеньевич")
        driver.find_element_by_id("itemForm:tabView:passportNumber").click()
        driver.find_element_by_id("itemForm:tabView:passportNumber").clear()
        driver.find_element_by_id("itemForm:tabView:passportNumber").send_keys("478965")
        driver.find_element_by_id("itemForm:tabView:birthDateStr").click()
        driver.find_element_by_id("itemForm:tabView:birthDateStr").clear()
        driver.find_element_by_id("itemForm:tabView:birthDateStr").send_keys("11.11.1980")
        driver.find_element_by_id("itemForm:tabView:phone").click()
        driver.find_element_by_id("itemForm:tabView:phone").click()
        driver.find_element_by_id("itemForm:tabView:phone").clear()
        driver.find_element_by_id("itemForm:tabView:phone").send_keys("+74569851245")
        driver.find_element_by_id("itemForm:tabView:email").click()
        driver.find_element_by_id("itemForm:tabView:email").clear()
        driver.find_element_by_id("itemForm:tabView:email").send_keys("123@321")
        driver.find_element_by_id("itemForm:tabView:otherCountry_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:otherCountry_items").click()
        driver.find_element_by_id("itemForm:tabView:otherCountry_1").click()
        driver.find_element_by_id("itemForm:tabView:otherCountryCity").click()
        driver.find_element_by_id("itemForm:tabView:otherCountryCity").clear()
        driver.find_element_by_id("itemForm:tabView:otherCountryCity").send_keys(u"Ярославль")
        driver.find_element_by_id("itemForm:tabView:otherCountryPeriod").click()
        driver.find_element_by_id("itemForm:tabView:otherCountryPeriod").clear()
        driver.find_element_by_id("itemForm:tabView:otherCountryPeriod").send_keys("11.11.2020")
        driver.find_element_by_css_selector("span.ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element_by_css_selector("span.ui-chkbox-icon.ui-icon.ui-c").click()
        driver.find_element_by_css_selector("div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover > span.ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element_by_css_selector("div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover.ui-state-active > span.ui-chkbox-icon.ui-icon.ui-c").click()
        driver.find_element_by_css_selector("div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover > span.ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element_by_css_selector("div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover.ui-state-active > span.ui-chkbox-icon.ui-icon.ui-c").click()
        driver.find_element_by_id("itemForm:tabView:result").click()
        driver.find_element_by_id("itemForm:tabView:result").clear()
        driver.find_element_by_id("itemForm:tabView:result").send_keys(u"Нет")

        driver.find_element_by_css_selector("body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        driver.find_element_by_id("itemForm:j_id4").click()
        driver.find_element_by_id("toolbarform:j_idt76")

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
