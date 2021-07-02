# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class CreatePassanger(unittest.TestCase):
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
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Create_passanger.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.create_passanger()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')     
    
    def test_create_passanger(self):
        self.genlog()
    '''
    def test_create_passanger(self):
        driver = self.driver
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml#")
        #driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector("#j_idt68 > div.nano.layout-tabmenu-nav > ul > li:nth-child(7) > a > div").click()
        driver.find_element_by_id("toolbarform:j_idt76").click()
        driver.find_element_by_id("itemForm:tabView:lastName").click()
        driver.find_element_by_id("itemForm:tabView:lastName").clear()
        driver.find_element_by_id("itemForm:tabView:lastName").send_keys(u"СаблинПасс")
        driver.find_element_by_id("itemForm:tabView:firstName").click()
        driver.find_element_by_id("itemForm:tabView:firstName").clear()
        driver.find_element_by_id("itemForm:tabView:firstName").send_keys(u"Роман")
        driver.find_element_by_id("itemForm:tabView:patronymicName").click()
        driver.find_element_by_id("itemForm:tabView:patronymicName").clear()
        driver.find_element_by_id("itemForm:tabView:patronymicName").send_keys(u"Евгеньевич")
        driver.find_element_by_id("itemForm:tabView:birthDate_input").click()
        driver.find_element_by_id("itemForm:tabView:birthDate_input").clear()
        for date in "08911111":
          driver.find_element_by_id("itemForm:tabView:birthDate_input").send_keys(Keys.HOME, date)
        driver.find_element_by_css_selector("itemForm:tabView:sex:0").click()
        driver.find_element_by_id("itemForm:tabView:flightNumber").click()
        driver.find_element_by_id("itemForm:tabView:flightNumber").clear()
        driver.find_element_by_id("itemForm:tabView:flightNumber").send_keys(u"7845ап")
        driver.find_element_by_id("itemForm:tabView:seat").click()
        driver.find_element_by_id("itemForm:tabView:seat").clear()
        driver.find_element_by_id("itemForm:tabView:seat").send_keys(u"74п")
        driver.find_element_by_id("itemForm:tabView:departureCountry_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:departureCountry_items").click()
        driver.find_element_by_id("itemForm:tabView:departureCountry_1").click()
        driver.find_element_by_id("itemForm:tabView:arrivalCity_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:arrivalCity_items").click()
        driver.find_element_by_id("itemForm:tabView:arrivalCity_1").click()
        driver.find_element_by_id("itemForm:tabView:borderCrossingDate_input").click()
        driver.find_element_by_id("itemForm:tabView:borderCrossingDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:borderCrossingDate_input").send_keys("11.11.2020")
        driver.find_element_by_id("itemForm:tabView:passportSerialNumber").clear()
        driver.find_element_by_id("itemForm:tabView:passportSerialNumber").send_keys("1458")
        driver.find_element_by_id("itemForm:tabView:passportNumber").click()
        driver.find_element_by_id("itemForm:tabView:passportNumber").clear()
        driver.find_element_by_id("itemForm:tabView:passportNumber").send_keys("478965")
        driver.find_element_by_id("itemForm:tabView:passportDateOfIssue_input").click()
        driver.find_element_by_id("itemForm:tabView:passportDateOfIssue_input").clear()
        for date in "51021111":
          driver.find_element_by_id("itemForm:tabView:passportDateOfIssue_input").send_keys(Keys.HOME, date)
        driver.find_element_by_id("itemForm:tabView:phoneNumber").clear()
        driver.find_element_by_id("itemForm:tabView:phoneNumber").send_keys("89654123654")
        driver.find_element_by_id("itemForm:tabView:registerSubjectRf_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:registerSubjectRf_items").click()
        driver.find_element_by_id("itemForm:tabView:registerSubjectRf_1").click()
        driver.find_element_by_id("itemForm:tabView:registerLocality_input").click()
        driver.find_element_by_id("itemForm:tabView:registerLocality_input").clear()
        driver.find_element_by_id("itemForm:tabView:registerLocality_input").send_keys(u"Яро")
        driver.find_element_by_css_selector("li.ui-autocomplete-item.ui-autocomplete-list-item.ui-corner-all.ui-state-highlight").click()
        driver.find_element_by_id("itemForm:tabView:registerCityArea_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:registerCityArea_items").click()
        driver.find_element_by_id("itemForm:tabView:registerCityArea_1").click()
        driver.find_element_by_id("itemForm:tabView:registerStreet_input").click()
        driver.find_element_by_id("itemForm:tabView:registerStreet_input").clear()
        driver.find_element_by_id("itemForm:tabView:registerStreet_input").send_keys(u"Мира")
        driver.find_element_by_id("itemForm:tabView:registerBuilding_input").clear()
        driver.find_element_by_id("itemForm:tabView:registerBuilding_input").send_keys("12")
        driver.find_element_by_id("itemForm:tabView:registerApartment").click()
        driver.find_element_by_id("itemForm:tabView:registerApartment").clear()
        driver.find_element_by_id("itemForm:tabView:registerApartment").send_keys("Barcode_Verification")
        driver.find_element_by_id("itemForm:tabView:factSubjectRf_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:factSubjectRf_items").click()
        time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:factSubjectRf_1").click()
        driver.find_element_by_id("itemForm:tabView:factLocality_input").click()
        driver.find_element_by_id("itemForm:tabView:factLocality_input").clear()
        driver.find_element_by_id("itemForm:tabView:factLocality_input").send_keys(u"Ярослав")
        driver.find_element_by_xpath("//span[@id='itemForm:tabView:factLocality_panel']/ul/li").click()
        driver.find_element_by_id("itemForm:tabView:factCityArea_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:factCityArea_items").click()
        driver.find_element_by_id("itemForm:tabView:factCityArea_1").click()
        driver.find_element_by_id("itemForm:tabView:factStreet_input").click()
        driver.find_element_by_id("itemForm:tabView:factStreet_input").clear()
        driver.find_element_by_id("itemForm:tabView:factStreet_input").send_keys(u"Мира")
        driver.find_element_by_id("itemForm:tabView:factBuilding_input").clear()
        driver.find_element_by_id("itemForm:tabView:factBuilding_input").send_keys("2")
        driver.find_element_by_id("itemForm:tabView:factApartment").click()
        driver.find_element_by_id("itemForm:tabView:factApartment").clear()
        driver.find_element_by_id("itemForm:tabView:factApartment").send_keys("Barcode_Verification")
        driver.find_element_by_xpath("//button[@id='itemForm:tabView:j_id110']/span[2]").click()
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
