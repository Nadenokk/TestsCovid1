# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException, NoSuchWindowException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver import ActionChains
import logging, os
import sys
import random
import string
from glob import glob
import os.path


class BankDetails(unittest.TestCase):

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

    def generate_random_string_number(self):
        numbers = string.digits
        rand_string = ''.join(random.choice(numbers) for i in range(8))
        return rand_string


    def test_bank_details(self):
        driver = self.driver
        driver.get("http://auraep.ru:8180/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("tuilp")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("tuilp")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()

        driver.find_element(By.CSS_SELECTOR,
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(13) > a").click()

        driver.find_element(By.ID,"files-form:j_idt81").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//ul[@class='ui-tree-container']/li[last()]/span").click()
        time.sleep(2)
        #редактировать папку
        driver.find_element(By.ID,"files-form:j_idt82").click()
        driver.find_element(By.ID,"files-form:edit-folder-tabView:name").click()
        driver.find_element(By.ID,"files-form:edit-folder-tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element(By.ID,"files-form:edit-folder-tabView:name").send_keys(namefile)
        driver.find_element(By.CSS_SELECTOR,"#files-form\:edit-folder-tabView\:type_label").click()
        driver.find_element(By.ID,"files-form:edit-folder-tabView:type_label").click()
        driver.find_element(By.ID,"files-form:edit-folder-tabView:type_4").click()

        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.CSS_SELECTOR,"#files-form\:edit-folder-tabView\:icon_label").click()
        driver.find_element(By.ID,"files-form:edit-folder-tabView:icon_label").click()
        driver.find_element(By.ID,"files-form:edit-folder-tabView:icon_20").click()

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"files-form:j_idt122").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//ul[@class='ui-tree-container']/li[last()]/span").click()

        # новый файл
        driver.find_element(By.ID,"files-form:j_idt95").click()
        time.sleep(2)
        
        driver.find_element(By.XPATH,"//div[@id='files-form:j_idt114']//li[@data-item-value='file']//a[@id='files-form:j_idt118']").click()
        driver.find_element(By.ID,"itemForm:tabView:name").click()
        driver.find_element(By.ID,"itemForm:tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element(By.ID,"itemForm:tabView:name").send_keys(namefile)
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys("123")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_2").click()

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:validUntil_input").send_keys("07.09.2021 09:48")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:j_id58").click()
        time.sleep(6)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.ID,"toolbarform:j_idt17").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        button = driver.find_element(By.ID,"itemForm:tabView:j_idt106_input")
        button.send_keys(
            "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\files\\4316.xlsx")
        time.sleep(3)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(4)
        assert driver.find_element(By.XPATH,
                "//tbody[@id='files-form:file-datatable_data']/tr[" + str(1) + "]/td[" + str(2) + "]").text == namefile
        order2 = driver.find_element(By.XPATH,"//tbody[@id='files-form:file-datatable_data']/tr[" + str(1) + "]/td[" + str(5) + "]").text
        order2 = order2.partition(' -')[0]
        assert order2 == "ФАЙЛ"
        time.sleep(3)
        #новый общий документ
        driver.find_element(By.ID,"files-form:j_idt95").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//div[@id='files-form:j_idt114']//li[@data-item-value='common']//a[@id='files-form:j_idt118']").click()
        driver.find_element(By.ID,"itemForm:tabView:name").click()
        driver.find_element(By.ID,"itemForm:tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element(By.ID,"itemForm:tabView:name").send_keys(namefile)
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys("123")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_2").click()

        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:validUntil_input").send_keys("07.09.2021 09:48")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:j_id58").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.ID,"toolbarform:j_idt17").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        button = driver.find_element(By.ID,"itemForm:tabView:j_idt106_input")
        button.send_keys(
            "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\files\\4316.xlsx")
        time.sleep(3)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(3)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(2) + "]/td[" + str(2) + "]").text == namefile
        order2 = driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(2) + "]/td[" + str(5) + "]").text
        order2 = order2.partition(' -')[0]
        assert order2 == "ОБЩИЙ ДОКУМЕНТ"
        #входящий документ
        driver.find_element(By.ID,"files-form:j_idt95").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//div[@id='files-form:j_idt114']//li[@data-item-value='inbox-document']//a[@id='files-form:j_idt118']").click()
        driver.find_element(By.ID,"itemForm:tabView:name").click()
        driver.find_element(By.ID,"itemForm:tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element(By.ID,"itemForm:tabView:name").send_keys(namefile)
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys("123")
        driver.find_element(By.ID,"itemForm:tabView:sender").send_keys("ФБУН")

        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_2").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:validUntil_input").send_keys("07.09.2021 09:48")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:j_id60").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.ID,"toolbarform:j_idt17").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        button = driver.find_element(By.ID,"itemForm:tabView:j_idt106_input")
        button.send_keys(
            "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\files\\4316.xlsx")
        time.sleep(3)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(3)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(3) + "]/td[" + str(2) + "]").text == namefile
        order2 = driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(3) + "]/td[" + str(5) + "]").text
        order2 = order2.partition(' -')[0]
        assert order2 == "ВХОДЯЩИЙ ДОКУМЕНТ"

        #Исходящий документ
        driver.find_element(By.ID,"files-form:j_idt95").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//div[@id='files-form:j_idt114']//li[@data-item-value='outbox-document']//a[@id='files-form:j_idt118']").click()
        driver.find_element(By.ID,"itemForm:tabView:name").click()
        driver.find_element(By.ID,"itemForm:tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element(By.ID,"itemForm:tabView:name").send_keys(namefile)
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys("123")
        driver.find_element(By.ID,"itemForm:tabView:receiver").send_keys("ФБУН")

        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_2").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:outDate_input").send_keys("07.09.2021")
        driver.find_element(By.ID,"itemForm:tabView:validUntil_input").send_keys("07.09.2021 09:48")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:j_id62").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.ID,"toolbarform:j_idt17").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        button = driver.find_element(By.ID,"itemForm:tabView:j_idt106_input")
        button.send_keys(
            "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\files\\4316.xlsx")
        time.sleep(3)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(3)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(4) + "]/td[" + str(2) + "]").text == namefile
        order2 = driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(4) + "]/td[" + str(5) + "]").text
        order2 = order2.partition(' -')[0]
        assert order2 == "ИСХОДЯЩИЙ ДОКУМЕНТ"

        #договор
        driver.find_element(By.ID,"files-form:j_idt95").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//div[@id='files-form:j_idt114']//li[@data-item-value='contract']//a[@id='files-form:j_idt118']").click()
        driver.find_element(By.ID,"itemForm:tabView:name").click()
        driver.find_element(By.ID,"itemForm:tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element(By.ID,"itemForm:tabView:name").send_keys(namefile)
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys("123")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_2").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:client_label").click()
        driver.find_element(By.ID,"itemForm:tabView:client_label").click()
        driver.find_element(By.ID,"itemForm:tabView:client_1").click()
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:validUntil_input").send_keys("07.09.2021 09:48")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:workType_label").click()
        driver.find_element(By.ID,"itemForm:tabView:workType_label").click()
        driver.find_element(By.ID,"itemForm:tabView:workType_1").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:j_id66").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.ID,"toolbarform:j_idt17").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:contractCost_input").send_keys("300")
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        button = driver.find_element(By.ID,"itemForm:tabView:j_idt106_input")
        button.send_keys(
            "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\files\\4316.xlsx")
        time.sleep(3)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(3)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(5) + "]/td[" + str(2) + "]").text == namefile
        order2 = driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(5) + "]/td[" + str(5) + "]").text
        order2 = order2.partition(' -')[0]
        assert order2 == "ДОГОВОР"

        #счет
        driver.find_element(By.ID,"files-form:j_idt95").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//div[@id='files-form:j_idt114']//li[@data-item-value='invoice']//a[@id='files-form:j_idt118']").click()
        driver.find_element(By.ID,"itemForm:tabView:name").click()
        driver.find_element(By.ID,"itemForm:tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element(By.ID,"itemForm:tabView:name").send_keys(namefile)
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys("123")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_2").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:client_label").click()
        driver.find_element(By.ID,"itemForm:tabView:client_label").click()
        driver.find_element(By.ID,"itemForm:tabView:client_1").click()
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()

        driver.find_element(By.ID,"itemForm:tabView:paymentDate_input").send_keys("07.09.2021")
        driver.find_element(By.ID,"itemForm:tabView:reportDateFrom_input").send_keys("07.09.2021")
        driver.find_element(By.ID,"itemForm:tabView:reportDateTo_input").send_keys("07.09.2022")
        driver.find_element(By.ID,"itemForm:tabView:validUntil_input").send_keys("07.09.2021 09:48")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:j_id68").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.ID,"toolbarform:j_idt17").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:amount_input").send_keys("300")
        driver.find_element(By.ID,"itemForm:tabView:previouslyAmount_input").send_keys("123")
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        button = driver.find_element(By.ID,"itemForm:tabView:j_idt106_input")
        button.send_keys(
            "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\files\\4316.xlsx")
        time.sleep(3)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(3)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(5) + "]/td[" + str(2) + "]").text == namefile
        order2 = driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(5) + "]/td[" + str(5) + "]").text
        order2 = order2.partition(' -')[0]
        assert order2 == "СЧЕТ"
        #акт
        driver.find_element(By.ID,"files-form:j_idt95").click()
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//div[@id='files-form:j_idt114']//li[@data-item-value='act']//a[@id='files-form:j_idt118']").click()
        driver.find_element(By.ID,"itemForm:tabView:name").click()
        driver.find_element(By.ID,"itemForm:tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element(By.ID,"itemForm:tabView:name").send_keys(namefile)
        driver.find_element(By.ID,"itemForm:tabView:description").click()
        driver.find_element(By.ID,"itemForm:tabView:description").clear()
        driver.find_element(By.ID,"itemForm:tabView:description").send_keys("123")
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_label").click()
        driver.find_element(By.ID,"itemForm:tabView:assignee_2").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:client_label").click()
        driver.find_element(By.ID,"itemForm:tabView:client_label").click()
        driver.find_element(By.ID,"itemForm:tabView:client_1").click()
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        driver.find_element(By.ID,"itemForm:tabView:reportDateFrom_input").send_keys("07.09.2021")
        driver.find_element(By.ID,"itemForm:tabView:reportDateTo_input").send_keys("07.09.2022")
        driver.find_element(By.ID,"itemForm:tabView:validUntil_input").send_keys("07.09.2021 09:48")
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.XPATH,
            "//button[@id='itemForm:tabView:j_id66' and @type='button']").click()
        #driver.find_element(By.ID,"itemForm:tabView:j_id64").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1)").click()
        time.sleep(2)
        driver.find_element(By.ID,"toolbarform:j_idt17").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.XPATH,
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        button = driver.find_element(By.ID,"itemForm:tabView:j_idt106_input")
        button.send_keys(
            "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\files\\4316.xlsx")
        time.sleep(3)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(3)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(6) + "]/td[" + str(2) + "]").text == namefile
        order2 = driver.find_element(By.XPATH,
            "//tbody[@id='files-form:file-datatable_data']/tr[" + str(6) + "]/td[" + str(5) + "]").text
        order2 = order2.partition(' -')[0]
        assert order2 == "АКТ"


