# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import unittest, time, re
import logging, os

class CreatePublic(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")	
        #self.driver = webdriver.Chrome(chrome_options=options)
        self.driver = webdriver.Chrome(executable_path = "E:/bin/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def genlog(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not os.path.exists("Logs"):
            os.mkdir("Logs")
        handler = logging.FileHandler(str('logs/' + (time.strftime('''%d.%m.%Y_%H.%M_''', (time.localtime())))  + 'Create_public.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.create_public()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    
    
    def test_create_public(self):
        self.genlog()
        
    def create_public(self):
        driver = self.driver
        #driver.get("http://auraep.ru:9880")
        driver.get("https://pub.rpn19.ru/forms/33")
        driver.refresh()
        driver.find_element_by_id("Familiya_").click()
        driver.find_element_by_id("Familiya_").clear()
        driver.find_element_by_id("Familiya_").send_keys(u"СаблинПабл")
        driver.find_element_by_id("Imya").click()
        driver.find_element_by_id("Imya").clear()
        driver.find_element_by_id("Imya").send_keys(u"Роман")
        driver.find_element_by_id("Otchestvo_Middle_name").click()
        driver.find_element_by_id("Otchestvo_Middle_name").clear()
        driver.find_element_by_id("Otchestvo_Middle_name").send_keys(u"Евгеньевич")
        driver.find_element_by_id("date-mask").click()
        driver.find_element_by_id("date-mask").clear()
        driver.find_element_by_id("date-mask").send_keys("11.11.1980")
        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("0").click()
        #driver.find_element_by_css_selector("#itemForm\:tabView\:sex > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("Email").click()
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("2332@3221")
        driver.find_element_by_id("Telefon").click()
        driver.find_element_by_id("Telefon").clear()
        driver.find_element_by_id("Telefon").send_keys("89456321782")
        #driver.find_element_by_id("itemForm:tabView:country_label").click()
        driver.find_element_by_name("Strana").c

        driver.find_element_by_xpath("//form[@id='feedBack']//div[@class='mb-3'][10]//select[@name='Strana_Country' and @class='form-select']").click()

        #driver.find_element_by_link_text(u"Брянск").click()

        driver.find_element_by_css_selector("#itemForm\:tabView\:country_panel").click()
        driver.find_element_by_id("itemForm:tabView:country_1").click()
        driver.find_element_by_id("itemForm:tabView:region_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:region_panel").click()
        driver.find_element_by_id("itemForm:tabView:region_1").click()
        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("itemForm:tabView:city_input").click()
        driver.find_element_by_id("itemForm:tabView:city_input").clear()
        driver.find_element_by_id("itemForm:tabView:city_input").send_keys(u"Ярос")
        driver.find_element_by_css_selector("#itemForm\:tabView\:city_panel > ul > li:nth-child(1)").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressStreet_input").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressStreet_input").clear()
        driver.find_element_by_id("itemForm:tabView:homeAddressStreet_input").send_keys(u"Мир")
        driver.find_element_by_css_selector("#itemForm\:tabView\:homeAddressStreet_panel").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressBuilding_input").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressBuilding_input").clear()
        driver.find_element_by_id("itemForm:tabView:homeAddressBuilding_input").send_keys("1")
        driver.find_element_by_id("itemForm:tabView:homeAddressFlat").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressFlat").clear()
        driver.find_element_by_id("itemForm:tabView:homeAddressFlat").send_keys("1231")
        driver.find_element_by_id("itemForm:tabView:orgName").click()
        driver.find_element_by_id("itemForm:tabView:orgName").clear()
        driver.find_element_by_id("itemForm:tabView:orgName").send_keys(u"Институт")
        driver.find_element_by_id("itemForm:tabView:workPositionStringValue").click()
        driver.find_element_by_id("itemForm:tabView:workPositionStringValue").clear()
        driver.find_element_by_id("itemForm:tabView:workPositionStringValue").send_keys(u"Студент")
        driver.find_element_by_id("itemForm:tabView:workPhone").click()
        driver.find_element_by_id("itemForm:tabView:workPhone").clear()
        driver.find_element_by_id("itemForm:tabView:workPhone").send_keys("84965213647")
        driver.find_element_by_id("itemForm:tabView:workAddressCountry_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:workAddressCountry_panel").click()
        driver.find_element_by_id("itemForm:tabView:workAddressCountry_1").click()
        driver.find_element_by_id("itemForm:tabView:workAddressRegion_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:workAddressRegion_panel").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:workAddressRegion_1").click()
        driver.find_element_by_id("itemForm:tabView:workAddressCity_input").click()
        driver.find_element_by_id("itemForm:tabView:workAddressCity_input").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressCity_input").send_keys(u"г Ярос")
        driver.find_element_by_css_selector("#itemForm\:tabView\:workAddressCity_panel > ul > li.ui-autocomplete-item.ui-autocomplete-list-item.ui-corner-all.ui-state-highlight").click()
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").click()
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").send_keys(u"Мир")
        driver.find_element_by_css_selector("#itemForm\:tabView\:workAddressStreet_panel > ul > li.ui-autocomplete-item.ui-autocomplete-list-item.ui-corner-all.ui-state-highlight").click()
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").click()
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").send_keys("7")
        driver.find_element_by_id("itemForm:tabView:workAddressFlat").click()
        driver.find_element_by_id("itemForm:tabView:workAddressFlat").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressFlat").send_keys("745")
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").click()
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").send_keys("11.03.2021")
        driver.find_element_by_id("itemForm:tabView:departureCountry_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:departureCountry_items").click()
        driver.find_element_by_id("itemForm:tabView:departureCountry_2").click()
        driver.find_element_by_id("itemForm:tabView:flightNumber").click()
        driver.find_element_by_id("itemForm:tabView:flightNumber").clear()
        driver.find_element_by_id("itemForm:tabView:flightNumber").send_keys(u"7854пв")
        driver.find_element_by_css_selector("span.ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element_by_css_selector("body").send_keys(Keys.CONTROL + Keys.END)
        driver.find_element_by_css_selector("#itemForm\:j_idt19").click()
        driver.find_element_by_css_selector("#itemForm\:j_idt12")
        driver.find_element_by_css_selector("#itemForm\:j_idt12 > h3:nth-child(1)")
        driver.find_element_by_css_selector("#itemForm\:j_idt12 > img")
        driver.find_element_by_css_selector("#itemForm\:j_idt12 > h3:nth-child(6) > a")
                   
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
