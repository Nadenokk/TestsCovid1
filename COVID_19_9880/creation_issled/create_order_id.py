# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
import sys


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

    def test_create_order_number(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("borisova")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Gi8BbtDN")

        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        '''
        driver.find_element_by_css_selector(
            "#j_idt68 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(24) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"DB Query tool\"] > span").click()
        driver.find_element_by_id("j_idt75:j_idt76").click()
        driver.find_element_by_id("j_idt75:j_idt76").clear()
        text="update doc_barcodes\nset doc_status = 'Отправлен на печать'\nwhere doc_number = '7801436828';\nupdate doc_covid_researches\nset barcode_id = null\nwhere doc_number = '621Х624486';"
        driver.find_element_by_id("j_idt75:j_idt76").send_keys(text+Keys.TAB+Keys.ENTER)
        time.sleep(2)

        #driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        '''

        driver.find_element_by_css_selector(
            "#j_idt72 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(11) > a > div").click()
        driver.find_element_by_css_selector(u"a[title=\"Поиск штрих-кодов\"] > span").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element_by_css_selector("#filtersform\:j_idt85_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("filtersform:j_idt87").click()
        time.sleep(25)
        driver.find_elements_by_css_selector(
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(25)
        barcode = \
            driver.find_elements_by_css_selector("#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(1)")[
                0].text
        iss = driver.find_elements_by_css_selector("#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(3)")[
            0].text

        driver.find_element_by_css_selector(
            "#j_idt72 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Создание заявки\"] > span").click()

        driver.find_element_by_id("site-selection:j_idt165_label").click()
        driver.find_element_by_id("site-selection:j_idt165_1").click()
        # driver.find_element_by_xpath("//span[@class='ui-button-text ui-c' and @text='Выбрать']").click()
        driver.refresh()
        driver.find_element_by_id("site-selection:j_idt168").click()
        driver.refresh()
        time.sleep(2)
        driver.find_element_by_id("participantIdDataForm:inputParticipantId").send_keys("1597898")
        driver.find_element_by_name("participantIdDataForm:j_idt86").click()
        time.sleep(2)
        driver.find_element_by_id("participantDataForm:barcodeNumber").send_keys(barcode)
        driver.find_element_by_id("participantDataForm:createRequest").click()
        time.sleep(10)
        assert (driver.find_element_by_id("j_idt171").text) == "Заявка на исследование создана"





        #driver.switch_to.window(window_before)

        #driver.switch_to.window(driver.window_handles[-1])
        #time.sleep(8)

        #numberiss = driver.find_element_by_id("itemForm:docNumber").get_attribute('value')
        #driver.find_element_by_name("participantDataForm:j_idt118").click()
        #time.sleep(5)