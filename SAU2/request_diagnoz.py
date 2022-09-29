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
        driver.get("http://sau.rpn19.ru:11080/documents")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova@webdom.net")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("cudEJkKl")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(5) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Сформировать экстренное извещение\"] > span").click()
        driver.find_element(By.ID,"searchForm:j_idt82_input").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:j_idt85_input").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:j_idt88_input").send_keys(self.generate_random_string())
        driver.find_element(By.ID,"searchForm:dateFrom_input").click()
        time.sleep(2)
        driver.find_element(By.ID,"searchForm:dateFrom_input").send_keys("11")
        time.sleep(1)
        driver.find_element(By.ID,"searchForm:dateFrom_input").send_keys("05")
        time.sleep(1)
        driver.find_element(By.ID,"searchForm:dateFrom_input").send_keys("1999")
        time.sleep(2)
        driver.find_element(By.ID,"searchForm:j_idt93").click()
        time.sleep(2)
        driver.find_element(By.ID,"patientsForm:j_idt111").click()
        #заполнение карточки
        driver.find_element(By.XPATH,
            "//label[@for='j_idt78:j_idt97:sex:0']").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:inn").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:inn").send_keys(u"l4598")
        driver.find_element(By.ID,"j_idt78:j_idt97:snils").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:snils").send_keys(u"111-111-111 11")
        #адрес
        driver.find_element(By.ID,"j_idt78:j_idt97:tf_addressesTableList_add").click()
        driver.find_element(By.ID,"tableFieldItemForm:city_input").click()
        driver.find_element(By.ID,"tableFieldItemForm:city_input").send_keys(u"г. Санкт-Петербург"+Keys.TAB)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:cityArea_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:cityArea_items").click()
        driver.find_element(By.ID,"tableFieldItemForm:cityArea_1").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableFieldItemForm:street_input").send_keys(u"Учительская" + Keys.TAB)
        driver.find_element(By.ID,"tableFieldItemForm:house_input").send_keys(u"18" + Keys.TAB)
        driver.find_element(By.ID,"tableFieldItemForm:flat").click()
        driver.find_element(By.ID,"tableFieldItemForm:flat").send_keys(u"115")
        driver.find_element(By.ID,"tableFieldItemForm:comment").click()
        driver.find_element(By.ID,"tableFieldItemForm:comment").send_keys(u"Динозаврик")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"tableFieldItemForm:contractor_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id13").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id13").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id13").send_keys(u"ФБУЗ Центр гигиены и эпидемиологии (Эпидбюро)"+Keys.ENTER)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.ID,"tableFieldItemForm:j_idt205").click()
        time.sleep(2)
        #Контактные данные
        driver.find_element(By.ID,"j_idt78:j_idt97:tf_contactTableList_add").click()
        driver.find_element(By.ID,"tableFieldItemForm:data").click()
        driver.find_element(By.ID,"tableFieldItemForm:data").send_keys("+79997652322")
        driver.find_element(By.ID,"tableFieldItemForm:comments").click()
        driver.find_element(By.ID,"tableFieldItemForm:comments").send_keys("Номер телефона Динозаврика")
        driver.find_element(By.ID,"tableFieldItemForm:j_idt205").click()
        #Документ, удостоверяющий личность
        driver.find_element(By.ID,"j_idt78:j_idt97:tf_identityDocumentsTableList_add").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:identityDocumentsType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm\:identityDocumentsType_items").click()
        driver.find_element(By.ID,"tableFieldItemForm:identityDocumentsType_2").click()
        driver.find_element(By.ID,"tableFieldItemForm:series").click()
        driver.find_element(By.ID,"tableFieldItemForm:series").clear()
        driver.find_element(By.ID,"tableFieldItemForm:series").send_keys("4598")
        driver.find_element(By.ID,"tableFieldItemForm:identityDocumentsNumber").click()
        driver.find_element(By.ID,"tableFieldItemForm:identityDocumentsNumber").clear()
        driver.find_element(By.ID,"tableFieldItemForm:identityDocumentsNumber").send_keys("789456")
        driver.find_element(By.ID,"tableFieldItemForm:issuedBy").click()
        driver.find_element(By.ID,"tableFieldItemForm:issuedBy").clear()
        driver.find_element(By.ID,"tableFieldItemForm:issuedBy").send_keys(u"ОУФМС")
        driver.find_element(By.ID,"tableFieldItemForm:issuedDate_input").click()
        driver.find_element(By.ID,"tableFieldItemForm:issuedDate_input").clear()
        driver.find_element(By.ID,"tableFieldItemForm:issuedDate_input").send_keys("11.11.2015")
        driver.find_element(By.ID,"tableFieldItemForm:issuedCode").click()
        driver.find_element(By.ID,"tableFieldItemForm:issuedCode").clear()
        driver.find_element(By.ID,"tableFieldItemForm:issuedCode").send_keys("123333")
        driver.find_element(By.ID,"tableFieldItemForm:validity_input").click()
        driver.find_element(By.ID,"tableFieldItemForm:validity_input").clear()
        driver.find_element(By.ID,"tableFieldItemForm:validity_input").send_keys("11.11.2025")
        driver.find_element(By.ID,"tableFieldItemForm:j_idt205").click()
        #Заполнение Регистрирующее учреждение
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:dateStartDisease_input").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:dateStartDisease_input").clear()
        driver.find_element(By.ID,"j_idt78:j_idt97:dateStartDisease_input").send_keys("15.03.2022")
        driver.find_element(By.CSS_SELECTOR,"#j_idt78\:j_idt97\:reasonsDetectingDisease_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#j_idt78\:j_idt97\:reasonsDetectingDisease_panel").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:reasonsDetectingDisease_2").click()
        time.sleep(1)
        #заполнение место работы
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='2']").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:tf_jobsTable_add").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm2\:socialStatus_label").click()
        # driver.find_element(By.CSS_SELECTOR,"#j_idt78\:j_idt97\:reasonsDetectingDisease_panel").click()
        driver.find_element(By.ID,"tableFieldItemForm2:socialStatus_3").click()
        driver.find_element(By.ID,"tableFieldItemForm2:profession").click()
        #driver.find_element(By.ID,"tableFieldItemForm2:profession").clear()
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"tableFieldItemForm2:orgName_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element(By.ID,"tableForm:main-table:j_id13").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id13").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id13").send_keys(u"Евангелическо-Лютеранская церковь"+Keys.ENTER)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element(By.ID,"tableFieldItemForm2:lastVisitedDate_input").click()
        driver.find_element(By.ID,"tableFieldItemForm2:lastVisitedDate_input").clear()
        driver.find_element(By.ID,"tableFieldItemForm2:lastVisitedDate_input").send_keys("16.03.2022")
        driver.find_element(By.ID,"tableFieldItemForm2:saveTableButton2").click()
        #заполнение диагноза
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='3']").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:conditionSeverity_label").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:conditionSeverity_2").click()
        driver.find_element(By.ID,"j_idt78:j_idt97:nosocomialInfection").click()

        driver.find_element(By.ID,"j_idt78:j_idt97:tf_diagnosesTable_add").click()
        driver.find_element(By.ID,"tableFieldItemForm2:diagnose_input").click()
        driver.find_element(By.ID,"tableFieldItemForm2:diagnose_input").send_keys("COVID-19 с проявлениями ОРВИ")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableFieldItemForm2\:diagStatus_label").click()
        driver.find_element(By.ID,"tableFieldItemForm2:diagStatus_4").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"tableFieldItemForm2:whoIsSet_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr > td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(3)
        driver.find_element(By.ID,"tableFieldItemForm2:clarification").click()
        driver.find_element(By.ID,"tableFieldItemForm2:clarification").clear()
        driver.find_element(By.ID,"tableFieldItemForm2:clarification").send_keys("Динозаврик")
        driver.find_element(By.ID,"tableFieldItemForm2:whoIsSetPerson").click()
        driver.find_element(By.ID,"tableFieldItemForm2:whoIsSetPerson").clear()
        driver.find_element(By.ID,"tableFieldItemForm2:whoIsSetPerson").send_keys("Динозавров Динозавр")
        driver.find_element(By.ID,"tableFieldItemForm2:saveTableButton2").click()

        time.sleep(2)
        assert driver.find_element(By.XPATH,
                "//span[@class='ui-dialog-title' and @id='dialogForm:j_idt186_title']").text=="Внимание"


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

