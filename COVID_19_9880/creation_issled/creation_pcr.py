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
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")

        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt68 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(24) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"DB Query tool\"] > span").click()
        driver.find_element_by_id("j_idt75:j_idt76").click()
        driver.find_element_by_id("j_idt75:j_idt76").clear()
        text="update doc_barcodes\nset doc_status = 'Отправлен на печать'\nwhere doc_number = '7801436828';\nupdate doc_covid_researches\nset barcode_id = null\nwhere doc_number = '621Х624486';"
        driver.find_element_by_id("j_idt75:j_idt76").send_keys(text+Keys.TAB+Keys.ENTER)
        time.sleep(2)

        #driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt68 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Создание заявки\"] > span").click()
        driver.find_element_by_id("site-selection:j_idt132").click()
        driver.find_element_by_id("site-selection:j_idt132_1").click()
        # driver.find_element_by_xpath("//span[@class='ui-button-text ui-c' and @text='Выбрать']").click()
        driver.refresh()
        driver.find_element_by_id("site-selection:j_idt135").click()
        driver.refresh()
        time.sleep(2)

        driver.find_element_by_id("createPcr").click()
        driver.find_element_by_id("barcodeForm:j_idt147").send_keys("7801436828"+Keys.ENTER)
        time.sleep(5)


        time.sleep(4)