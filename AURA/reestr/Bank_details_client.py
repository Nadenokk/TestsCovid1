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
        driver.find_element_by_id("form:usernameInput").send_keys("tuilp")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("tuilp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()

        driver.find_element_by_css_selector(
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Реестр клиентов\"] > span").click()
        #Юридическое лицо
        driver.find_element_by_id("tableForm:j_idt74").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt93_label").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt93_items").click()
        driver.find_element_by_id("selectTypeForm:j_idt93_1").click()
        time.sleep(2)
        driver.find_element_by_id("selectTypeForm:j_idt95").click()
        name = self.generate_random_string()
        driver.find_element_by_id("legalForm:j_idt331:name").click()
        driver.find_element_by_id("legalForm:j_idt331:name").clear()
        driver.find_element_by_id("legalForm:j_idt331:name").send_keys(name)
        driver.find_element_by_css_selector("#legalForm\:j_idt331\:categories").click()
        driver.find_element_by_css_selector(
            "#legalForm\:j_idt331\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#legalForm\:j_idt331\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        #driver.find_element_by_id("legalForm:j_idt332:j_idt334").click()

        driver.find_element_by_id("legalForm:j_idt331:shortName").click()
        driver.find_element_by_id("legalForm:j_idt331:shortName").clear()
        driver.find_element_by_id("legalForm:j_idt331:shortName").send_keys(u"СаблинАнтител")
        driver.find_element_by_id("legalForm:j_idt331:seoName").click()
        driver.find_element_by_id("legalForm:j_idt331:seoName").clear()
        driver.find_element_by_id("legalForm:j_idt331:seoName").send_keys(u"Евгеньевич")
        driver.find_element_by_id("legalForm:j_idt331:email").click()
        driver.find_element_by_id("legalForm:j_idt331:email").clear()
        driver.find_element_by_id("legalForm:j_idt331:email").send_keys("shamkin@proweb.ru")
        driver.find_element_by_css_selector("#legalForm\:j_idt331\:userCategory_label").click()
        driver.find_element_by_css_selector("#legalForm\:j_idt331\:userCategory_items").click()
        driver.find_element_by_id("legalForm:j_idt331:userCategory_2").click()
        time.sleep(2)
        #банковские реквизиты
        driver.find_element_by_xpath(
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        driver.find_element_by_id("legalForm:j_idt331:bankTable:j_idt416").click()
        driver.find_element_by_id("legalBankForm:name").send_keys("Сбербанк")
        filial = self.generate_random_string()
        driver.find_element_by_id("legalBankForm:branchName").send_keys(filial)
        inn=self.generate_random_string_number()
        driver.find_element_by_id("legalBankForm:branchINN").send_keys(inn)
        driver.find_element_by_id("legalBankForm:bik").send_keys("123456789")
        driver.find_element_by_id("legalBankForm:mainAccount").send_keys("123456789")
        driver.find_element_by_id("legalBankForm:corrAccount").send_keys("123456789")
        driver.find_element_by_id("legalBankForm:j_idt582").click()
        assert driver.find_element_by_xpath("//tbody[@id='legalForm:j_idt332:bankTable_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == filial
        assert driver.find_element_by_xpath("//tbody[@id='legalForm:j_idt332:bankTable_data']//tr[" + str(1) + "]/td[" + str(3) + "]").text == inn
        driver.find_element_by_id("legalForm:j_idt521").click()
        time.sleep(3)
        name3 = driver.find_element_by_xpath(
            "//tbody[@id='tableForm:table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text
        assert (re.match(r'(?i)' + re.sub(r'\s', '', name) + r'$', re.sub(r'\s', '', name3)))
        driver.find_element_by_id("tableForm:table:0:j_idt90").click()
        driver.find_element_by_id("j_idt901:j_idt902").click()
        time.sleep(2)

        #ИП
        driver.find_element_by_id("tableForm:j_idt76").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt94_label").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt94_items").click()
        driver.find_element_by_id("selectTypeForm:j_idt94_2").click()
        time.sleep(2)
        driver.find_element_by_id("selectTypeForm:j_idt96").click()

        name = self.generate_random_string()
        driver.find_element_by_id("singleForm:j_idt612:name").click()
        driver.find_element_by_id("singleForm:j_idt612:name").clear()
        driver.find_element_by_id("singleForm:j_idt612:name").send_keys(name)
        driver.find_element_by_css_selector("#singleForm\:j_idt612\:categories").click()
        driver.find_element_by_css_selector(
            "#singleForm\:j_idt612\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#singleForm\:j_idt612\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        # driver.find_element_by_id("legalForm:j_idt332:j_idt334").click()

        driver.find_element_by_id("singleForm:j_idt612:shortName").click()
        driver.find_element_by_id("singleForm:j_idt612:shortName").clear()
        driver.find_element_by_id("singleForm:j_idt612:shortName").send_keys(u"СаблинПАСС")
        driver.find_element_by_id("singleForm:j_idt612:email").click()
        driver.find_element_by_id("singleForm:j_idt612:email").clear()
        driver.find_element_by_id("singleForm:j_idt612:email").send_keys("shamkin@proweb.ru")
        driver.find_element_by_css_selector("#singleForm\:j_idt612\:userCategory_label").click()
        driver.find_element_by_css_selector("#singleForm\:j_idt612\:userCategory_items").click()
        driver.find_element_by_id("singleForm:j_idt612:userCategory_2").click()
        time.sleep(2)
        #Банковские реквизиты
        driver.find_element_by_xpath(
            "//a[@href='#singleForm:j_idt612:j_idt669']").click()
        driver.find_element_by_id("singleForm:j_idt612:bankTable:j_idt692").click()
        driver.find_element_by_id("singleBankForm:name").send_keys("Сбербанк")
        filial = self.generate_random_string()
        driver.find_element_by_id("singleBankForm:branchName").send_keys(filial)
        inn = self.generate_random_string_number()
        driver.find_element_by_id("singleBankForm:branchINN").send_keys(inn)
        driver.find_element_by_id("singleBankForm:bik").send_keys("123456789")
        driver.find_element_by_id("singleBankForm:mainAccount").send_keys("123456789")
        driver.find_element_by_id("singleBankForm:corrAccount").send_keys("123456789")
        driver.find_element_by_id("singleBankForm:j_idt853").click()
        assert driver.find_element_by_xpath(
            "//tbody[@id='singleForm:j_idt612:bankTable_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == filial
        assert driver.find_element_by_xpath(
            "//tbody[@id='singleForm:j_idt612:bankTable_data']//tr[" + str(1) + "]/td[" + str(3) + "]").text == inn
        driver.find_element_by_id("singleForm:j_idt792").click()
        time.sleep(3)
        name4 = driver.find_element_by_xpath(
            "//tbody[@id='tableForm:table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text
        assert (re.match(r'(?i)' + re.sub(r'\s', '', name) + r'$', re.sub(r'\s', '', name4)))

        driver.find_element_by_id("tableForm:table:0:j_idt90").click()
        driver.find_element_by_id("j_idt901:j_idt902").click()
        time.sleep(2)

