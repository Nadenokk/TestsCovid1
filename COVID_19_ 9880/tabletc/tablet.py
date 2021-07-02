# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
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

    def test_search_tablet(self):
        driver = self.driver
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt68 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(8) > a > div > div.layout-tabmenu-tooltip-text").click()
        #driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_id("tableForm:j_idt88").send_keys("05В102447")
        driver.find_element_by_id("tableForm:j_idt85_input").clear()
        driver.find_element_by_id("tableForm:j_idt91").click()
        time.sleep(7)
        assert driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']/tr[" + str(1) + "]/td[" + str(1) + "]").text=="05В102447"
        window_before=driver.window_handles[0]
        actionChains = ActionChains(driver)
        actionChains.double_click(driver.find_element_by_id("tableForm:main-table_data")).perform()
        window_after = driver.window_handles[0]
        driver.switch_to.window(window_after)
        time.sleep(20)
        driver.find_element_by_id("itemForm:tabView:compileDate_input").click()
        driver.find_element_by_id("itemForm:tabView:compileDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:compileDate_input").send_keys("21.07.2020 15:42")
        time.sleep(3)






