# -*- coding: utf-8 -*-
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
import unittest, time, re
import logging, os

from selenium.webdriver.support.wait import WebDriverWait


class CreatePublic(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")	
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
        driver.get("http://auraep.ru:9880")
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
        driver.find_element_by_id("date-mask").send_keys("11111980")
        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("0").click()
        driver.find_element_by_id("Email").click()
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("2332@3221")
        driver.find_element_by_id("Telefon").click()
        driver.find_element_by_id("Telefon").clear()
        driver.find_element_by_id("Telefon").send_keys("89456321782")
        select=Select(driver.find_element_by_name("Strana"))
        select.select_by_visible_text(u"Россия")

        select = Select(driver.find_element_by_name("Region"))
        select.select_by_visible_text(u"Ярославская область")
        time.sleep(2)


        #Не понимаю почему selector не отрабатывает город и улицу
        #driver.find_element_by_id("city").click()
        #driver.find_element_by_id("city").clear()
        driver.find_element_by_id("city").send_keys(u"Ярославль"+Keys.TAB)
        time.sleep(2)
        #select = Select(driver.find_element_by_id("city"))
        #select.select_by_index(1)
        #select.select_by_visible_text(u"Ярославль")
        #time.sleep(5)
        driver.find_element_by_id("street").click()
        driver.find_element_by_id("street").clear()
        driver.find_element_by_id("street").send_keys(u"Мира"+Keys.TAB)
        #select = Select(driver.find_element_by_name("street"))
        #select.select_by_visible_text(u"Мира")


        #driver.find_element_by_id("building").click()
       # driver.find_element_by_id("building").click()
        driver.find_element_by_id("building").clear()
        driver.find_element_by_id("building").send_keys("1")
        time.sleep(2)
       # driver.find_element_by_id("Kvartira").click()
        driver.find_element_by_id("Kvartira").clear()
        driver.find_element_by_id("Kvartira").send_keys("1231")
        time.sleep(2)

        driver.find_element_by_id("Naimenovanie_organizatsii_Company_name").click()
        driver.find_element_by_id("Naimenovanie_organizatsii_Company_name").clear()
        driver.find_element_by_id("Naimenovanie_organizatsii_Company_name").send_keys(u"Институт")
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
