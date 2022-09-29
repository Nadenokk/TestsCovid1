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
        #driver.get("http://auraep.ru:11080/documents/")
        driver.get("http://sau.rpn19.ru:11080/documents")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("supervisor")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("zgA8SlfS")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(5) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Сформировать экстренное извещение\"] > span").click()
        driver.find_element(By.ID,"searchForm:lastName").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:firstName").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:patronymicName").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:dateFrom_input").click()
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
        driver.find_element(By.ID,"j_idt73:j_idt92:inn").click()
        driver.find_element(By.ID,"j_idt73:j_idt92:inn").clear()
        driver.find_element(By.ID,"j_idt73:j_idt92:inn").send_keys("123")
        driver.find_element(By.ID,"j_idt73:j_idt92:snils").click()
        driver.find_element(By.ID,"j_idt73:j_idt92:snils").clear()
        driver.find_element(By.ID,"j_idt73:j_idt92:snils").send_keys("78945212399")
        driver.find_element(By.ID,"j_idt73:j_idt92:citizenship_label").click()
        driver.find_element(By.CSS_SELECTOR,"#j_idt73\:j_idt92\:citizenship_panel").click()
        driver.find_element(By.CSS_SELECTOR,"#j_idt73\:j_idt92\:citizenship_129").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"j_idt73:j_idt92:contractor_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id14").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id14").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id14").send_keys(u"хеликс")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(7)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element(By.ID,"j_idt73:j_idt92:tf_addressesList_add").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableFieldItemForm:addressType_label").click()
        #time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:addressType_panel").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:addressType_1").click()

        #driver.find_element(By.ID,"tableFieldItemForm:country_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:country_panel").click()
        #driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:country_129").click()
        #driver.find_element(By.ID,"tableFieldItemForm:region_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:region_panel").click()
        #time.sleep(1)
        #driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:region_1").click()
        #time.sleep(1)
        #driver.find_element(By.ID,"tableFieldItemForm:tableFieldPanel").click()
        driver.find_element(By.ID,"tableFieldItemForm:city_input").click()
        driver.find_element(By.ID,"tableFieldItemForm:city_input").clear()
        driver.find_element(By.ID,"tableFieldItemForm:city_input").send_keys("Санкт")
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[@id='tableFieldItemForm:city_panel']/ul/li/span").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:cityArea_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:cityArea_items").click()
        driver.find_element(By.ID,"tableFieldItemForm:cityArea_1").click()
        driver.find_element(By.ID,"tableFieldItemForm:street_input").send_keys(u"Граф")
        driver.find_element(By.XPATH,"//span[@id='tableFieldItemForm:street_panel']/ul/li/span").click()
        driver.find_element(By.ID,"tableFieldItemForm:house_input").click()
        driver.find_element(By.ID,"tableFieldItemForm:house_input").clear()
        driver.find_element(By.ID,"tableFieldItemForm:house_input").send_keys("1")
        driver.find_element(By.ID,"tableFieldItemForm:flat").click()
        driver.find_element(By.ID,"tableFieldItemForm:flat").clear()
        driver.find_element(By.ID,"tableFieldItemForm:flat").send_keys("1")
        driver.find_element(By.ID,"tableFieldItemForm:comment").click()
        driver.find_element(By.ID,"tableFieldItemForm:comment").clear()
        driver.find_element(By.ID,"tableFieldItemForm:comment").send_keys("Динозаврики")
        driver.find_element(By.ID,"tableFieldItemForm:saveTableButton").click()
        time.sleep(2)
        #Контактные данные
        driver.find_element(By.ID,"j_idt73:j_idt92:tf_contactDataList_add").click()
        driver.find_element(By.ID,"tableFieldItemForm:contactType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:contactType_panel").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:contactType_1").click()
        driver.find_element(By.ID,"tableFieldItemForm:data").click()
        driver.find_element(By.ID,"tableFieldItemForm:data").clear()
        driver.find_element(By.ID,"tableFieldItemForm:data").send_keys("Динозаврики@mail.ru")
        driver.find_element(By.ID,"tableFieldItemForm:j_idt194").click()
        driver.find_element(By.ID,"tableFieldItemForm:saveTableButton").click()
        time.sleep(2)
        #Документ, удостоверяющий личность
        driver.find_element(By.ID,"j_idt73:j_idt92:tf_identityDocuments_add").click()
        driver.find_element(By.ID,"tableFieldItemForm:identityDocumentsType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:identityDocumentsType_panel").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:identityDocumentsType_2").click()
        driver.find_element(By.ID,"tableFieldItemForm:series").click()
        driver.find_element(By.ID,"tableFieldItemForm:series").clear()
        driver.find_element(By.ID,"tableFieldItemForm:series").send_keys("4477")
        driver.find_element(By.ID,"tableFieldItemForm:identityDocumentsNumber").click()
        driver.find_element(By.ID,"tableFieldItemForm:identityDocumentsNumber").clear()
        driver.find_element(By.ID,"tableFieldItemForm:identityDocumentsNumber").send_keys("1234567")
        driver.find_element(By.ID,"tableFieldItemForm:issuedBy").click()
        driver.find_element(By.ID,"tableFieldItemForm:issuedBy").clear()
        driver.find_element(By.ID,"tableFieldItemForm:issuedBy").send_keys("УФМС ДИНОЗАВРИКИ")
        driver.find_element(By.ID,"tableFieldItemForm:issuedDate_input").click()
        driver.find_element(By.ID,"tableFieldItemForm:issuedDate_input").clear()
        driver.find_element(By.ID,"tableFieldItemForm:issuedDate_input").send_keys("12.12.2000")
        driver.find_element(By.ID,"tableFieldItemForm:issuedCode").click()
        driver.find_element(By.ID,"tableFieldItemForm:issuedCode").clear()
        driver.find_element(By.ID,"tableFieldItemForm:issuedCode").send_keys("123456")
        driver.find_element(By.ID,"tableFieldItemForm:validity_input").click()
        driver.find_element(By.ID,"tableFieldItemForm:validity_input").clear()
        driver.find_element(By.ID,"tableFieldItemForm:validity_input").send_keys("12.12.2222")
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
        driver.find_element(By.ID,"tableFieldItemForm2:saveTableButton2").click()

        #заполнение диагноза
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='3']").click()
        driver.find_element(By.ID,"j_idt73:j_idt92:tf_diagnoses_add").click()
        driver.find_element(By.ID,"tableFieldItemForm2:diagnose_input").send_keys("головокружение")
        driver.find_element(By.ID,"tableFieldItemForm2:diagnose_panel").click()
        driver.find_element(By.ID,"tableFieldItemForm2:diagnose_input").clear()
        time.sleep(2)
        driver.find_element(By.ID,"tableFieldItemForm2:codeMkb10_input").clear()
        driver.find_element(By.ID,"tableFieldItemForm2:codeMkb10_input").send_keys("J05.1")
        driver.find_element(By.ID,"tableFieldItemForm2:codeMkb10_panel").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableFieldItemForm2:saveTableButton2").click()

        driver.find_element(By.ID,"j_idt73:j_idt76").click()
        time.sleep(10)
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

