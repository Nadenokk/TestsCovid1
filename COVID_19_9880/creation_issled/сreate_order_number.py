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


class CreateOrderNumber(unittest.TestCase):

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
        # driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("supervisor")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Ivwdk1Rp")

        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()


        driver.find_element(By.CSS_SELECTOR,
            "#j_idt66 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(11) > a > div").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Штрих-коды\"] > span").click()
        driver.find_element(By.CSS_SELECTOR,"span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element(By.XPATH,"/html/body/div[9]/div[2]/ul/li[2]/div/div[2]/span").click()
        time.sleep(70)
        driver.find_elements(By.CSS_SELECTOR,
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(60)
        barcode = \
            driver.find_elements(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(1)")[
                0].text
        iss = driver.find_elements(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(3)")[
            0].text

        driver.find_element(By.CSS_SELECTOR,
            "#j_idt66 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Создание заявки\"] > span").click()

        driver.find_element(By.ID,"site-selection:j_idt160_label").click()
        driver.find_element(By.ID,"site-selection:j_idt160_1").click()
        # driver.find_element(By.XPATH,"//span[@class='ui-button-text ui-c' and @text='Выбрать']").click()
        driver.refresh()
        driver.find_element(By.ID,"site-selection:j_idt163").click()
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.ID,"participantIdDataForm:inputFindResearch").send_keys("02015983")
        driver.find_element(By.ID,"participantIdDataForm:j_idt86").click()
        time.sleep(2)
        driver.find_element(By.ID,"participantDataForm:barcodeNumber").send_keys(barcode)
        driver.find_element(By.ID,"participantDataForm:j_idt116").click()
        time.sleep(10)

        driver.switch_to.window(driver.window_handles[-1])
        numberiss = driver.find_element(By.ID,"itemForm:docNumber").get_attribute('value')
        assert numberiss==iss



