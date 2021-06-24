# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class CreatePlanshet(unittest.TestCase):
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
        handler = logging.FileHandler(str('logs/' + (time.strftime('''%d.%m.%Y_%H.%M_''', (time.localtime())))  + 'Create_planshet_by_barcode_and_batch.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.planshet()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')

    def test_create_planshet(self):            
        self.genlog()
    
    def planshet(self):
        driver = self.driver
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml#")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        
        # Копируем номер штрихкода
        driver.find_element_by_css_selector("#j_idt60 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(11) > a > div").click()
        driver.find_element_by_css_selector(u"a[title=\"Штрих-коды\"] > span").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element_by_xpath("/html/body/div[9]/div[2]/ul/li[2]/div/div[2]/span").click()
        time.sleep(50)
        driver.find_elements_by_css_selector("#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(25)
        barcode = driver.find_elements_by_css_selector("#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(1)")[0].text
        iss = driver.find_elements_by_css_selector("#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(3)")[0].text
        
        #Идем к планшетам по штрихкоду        
        driver.find_element_by_link_text(u"Планшеты").click()
        driver.find_element_by_css_selector("#toolbarform\:j_idt90").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#barcodeForm\:j_idt327").click()
        driver.find_element_by_css_selector("#barcodeForm\:j_idt327").clear()
        driver.find_element_by_css_selector("#barcodeForm\:j_idt327").send_keys(barcode)
        driver.find_element_by_css_selector("#barcodeForm\:j_idt327").send_keys(Keys.ENTER)
        time.sleep(15)
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:patientCategories_panel").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:patientCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:patientCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body.main-body").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_css_selector("span.ui-button-icon-left.ui-icon.ui-c.fa.fa-ellipsis-h").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:main-table_data > tr:nth-child(3)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector("#toolbarform\:j_idt68")
        driver.find_element_by_css_selector("#toolbarform\:j_idt90")
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id2").click()
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id2").clear()
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id2").send_keys(iss)
        time.sleep(35)
        driver.find_element_by_css_selector("#tableForm\:main-table_data > tr:nth-child(1)").click()
        driver.find_element_by_css_selector("#toolbarform\:j_idt70").click()
        time.sleep(30)
        driver.find_element_by_css_selector("#itemForm\:tablets-doAction-Отправленвхранилище").click()
        driver.find_element_by_css_selector("#itemForm\:j_id16").click()
        driver.find_element_by_css_selector("#itemForm\:tablets-doAction-Вхранилище").click()
        driver.find_element_by_css_selector("#itemForm\:j_id21").click()
        driver.find_element_by_css_selector("div > div > div.ui-growl-message > p")
        time.sleep(50)
    
        #Формируем партию планшетов
        driver.find_element_by_link_text(u"Планшеты").click()
        driver.find_element_by_css_selector("#toolbarform\:j_idt91").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#buildForm\:j_idt70").click()
        driver.find_element_by_css_selector("#barcodeForm\:j_idt86").click()
        driver.find_element_by_css_selector("#barcodeForm\:j_idt86").clear()
        driver.find_element_by_css_selector("#barcodeForm\:j_idt86").send_keys(barcode)
        time.sleep(2)
        driver.find_element_by_css_selector("#barcodeForm\:j_idt86").send_keys(Keys.ENTER)
        assert driver.find_element_by_css_selector("#dataForm\:tablets_data > tr > td:nth-child(1)").text == iss
        time.sleep(3)
        driver.find_element_by_link_text(u"Планшеты").click()
        driver.find_element_by_css_selector("#toolbarform\:j_idt91").click()
        driver.find_element_by_css_selector("#buildForm\:searchTablet_input").click()
        driver.find_element_by_css_selector("#buildForm\:searchTablet_input").clear()
        driver.find_element_by_css_selector("#buildForm\:searchTablet_input").send_keys(iss)
        time.sleep(2)
        driver.find_element_by_css_selector("body").click()
        time.sleep(3)
        assert driver.find_element_by_css_selector("#dataForm\:tablets_data > tr > td:nth-child(1)").text == iss
        driver.find_element_by_css_selector("#buildForm\:sendToLaboratory").click()
        driver.find_element_by_css_selector("#growlForm\:growl_container > div > div > div.ui-growl-message > p")
        driver.find_element_by_css_selector("#buildForm\:laboratory_label").click()
        time.sleep(1)
        driver.find_element_by_css_selector("#buildForm\:laboratory_2").click()
        driver.find_element_by_css_selector("#buildForm\:sendToLaboratory").click()
        driver.find_element_by_css_selector("#growlForm\:growl_container > div > div > div.ui-growl-message > p")
        driver.find_element_by_css_selector("#buildForm\:sendToLaboratory")
        
        
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
