# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver import ActionChains
import logging, os
import sys
import random
import string

class CreateOrder(unittest.TestCase):

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

    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))
        return rand_string

    def test_create_order(self):
        driver = self.driver
        driver.get("http://auraep.ru:11080/documents/")
        #driver.get("http://46.61.193.136:8383/documents/projects-list#")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("supervisor")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("supervisor")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(5) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Сформировать экстренное извещение\"] > span").click()
        driver.find_element(By.ID,"searchForm:lastName").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:firstName").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:patronymicName").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:dateFrom_input").click()
        driver.find_element(By.ID,"searchForm:dateFrom_input").clear()
        time.sleep(2)
        driver.find_element(By.ID,"searchForm:dateFrom_input").send_keys("11")
        time.sleep(1)
        driver.find_element(By.ID,"searchForm:dateFrom_input").send_keys("11")
        time.sleep(1)
        driver.find_element(By.ID,"searchForm:dateFrom_input").send_keys("1111")
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//span[@class='ui-button-icon-left ui-icon ui-c fa fa-search']").click()
        driver.find_element(By.XPATH,
            "//span[@class='ui-button-icon-left ui-icon ui-c fa fa-stethoscope']").click()
        #заполнение карточки
        driver.find_element(By.XPATH,
            "//label[@for='j_idt73:j_idt92:sex:0']").click()
        driver.find_element(By.ID,"j_idt73:j_idt92:tf_addressesList_add").click()

        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:cityArea_label").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:cityArea_items").click()
        driver.find_element(By.ID,"tableFieldItemForm:cityArea_1").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableFieldItemForm:saveTableButton").click()
        time.sleep(2)
        #заполнение место работы
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='2']").click()
        driver.find_element(By.ID,"j_idt73:j_idt92:tf_jobs_add").click()
        time.sleep(2)

        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"tableFieldItemForm2:orgName_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id5").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id5").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id5").send_keys(u"сбер")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable.ui-state-hover").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        assert driver.find_element(By.XPATH,
            "//label[@class='ui-selectonemenu-label ui-inputfield ui-corner-all' and @id='tableFieldItemForm2:cityArea_label']").text=="Кировский"
        time.sleep(2)
        '''
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm2\:cityArea_label").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm2\:cityArea_items").click()
        driver.find_element(By.ID,"tableFieldItemForm2:cityArea_1").click()
        '''
        driver.find_element(By.ID,"tableFieldItemForm2:saveTableButton2").click()


        #заполнение диагноза
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='3']").click()
        driver.find_element(By.ID,"j_idt73:j_idt92:tf_diagnoses_add").click()
        driver.find_element(By.ID,"tableFieldItemForm2:diagnose_input").send_keys("головокружение")
        driver.find_element(By.ID,"tableFieldItemForm2:diagnose_panel").click()
        driver.find_element(By.ID,"tableFieldItemForm2:saveTableButton2").click()

        driver.find_element(By.ID,"j_idt73:j_idt76").click()
        time.sleep(4)
        assert driver.find_element(By.XPATH,
                "//span[@class='ui-dialog-title' and @id='dialogForm:j_idt186_title']").text=="Внимание"
        time.sleep(3)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()