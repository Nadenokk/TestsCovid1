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
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("log")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("log")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()

        driver.find_element_by_css_selector(
            "#j_idt67 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(13) > a").click()
        # файлы
        driver.find_element_by_id("files-form:j_idt82").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        time.sleep(2)

        driver.find_element_by_id("files-form:j_idt83").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").send_keys("Файлы")
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_0").click()

        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_20").click()

        time.sleep(2)
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("files-form:j_idt122").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        assert driver.find_element_by_xpath(
            "//th[@id='files-form:file-datatable:j_idt101:5']/span").text == "ДАТА ДОКУМЕНТА"

        # Общие документы
        driver.find_element_by_id("files-form:j_idt82").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        time.sleep(2)

        driver.find_element_by_id("files-form:j_idt83").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").send_keys("Общие документы")
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_1").click()

        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_18").click()

        time.sleep(2)
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("files-form:j_idt122").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        assert driver.find_element_by_xpath(
            "//th[@id='files-form:file-datatable:j_idt101:5']/span").text == "ДАТА ДОКУМЕНТА"
        # Входящие документы
        driver.find_element_by_id("files-form:j_idt82").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        time.sleep(2)

        driver.find_element_by_id("files-form:j_idt83").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").send_keys("Входящие документы")
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_2").click()

        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_18").click()

        time.sleep(2)
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("files-form:j_idt122").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        assert driver.find_element_by_xpath(
            "//th[@id='files-form:file-datatable:j_idt101:6']/span").text == "ДАТА ДОКУМЕНТА"

        # Исходящие документы
        driver.find_element_by_id("files-form:j_idt82").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        time.sleep(2)

        driver.find_element_by_id("files-form:j_idt83").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").send_keys("Исходящие документы")
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_3").click()

        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_18").click()

        time.sleep(2)
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("files-form:j_idt122").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        assert driver.find_element_by_xpath(
            "//th[@id='files-form:file-datatable:j_idt101:7']/span").text == "ДАТА ДОКУМЕНТА"

        # Договоры
        driver.find_element_by_id("files-form:j_idt82").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        time.sleep(2)

        driver.find_element_by_id("files-form:j_idt83").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").send_keys("Договоры")
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_4").click()

        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_18").click()

        time.sleep(2)
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("files-form:j_idt122").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        assert driver.find_element_by_xpath(
            "//th[@id='files-form:file-datatable:j_idt101:7']/span").text == "ДАТА ДОКУМЕНТА"
        # Счета
        driver.find_element_by_id("files-form:j_idt82").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        time.sleep(2)

        driver.find_element_by_id("files-form:j_idt83").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").send_keys("Счета")
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_5").click()

        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_18").click()

        time.sleep(2)
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("files-form:j_idt122").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        assert driver.find_element_by_xpath(
            "//th[@id='files-form:file-datatable:j_idt101:9']/span").text == "ДАТА ДОКУМЕНТА"

        # Акты
        driver.find_element_by_id("files-form:j_idt82").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        time.sleep(2)

        driver.find_element_by_id("files-form:j_idt83").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").clear()
        namefile = self.generate_random_string()
        driver.find_element_by_id("files-form:edit-folder-tabView:name").send_keys("Акты")
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:type_6").click()

        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_css_selector("#files-form\:edit-folder-tabView\:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_label").click()
        driver.find_element_by_id("files-form:edit-folder-tabView:icon_18").click()

        time.sleep(2)
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("files-form:j_idt122").click()
        time.sleep(2)
        driver.find_element_by_xpath("//ul[@class='ui-tree-container']/li[last()]/span").click()
        assert driver.find_element_by_xpath(
            "//th[@id='files-form:file-datatable:j_idt101:8']/span").text == "ДАТА ДОКУМЕНТА"