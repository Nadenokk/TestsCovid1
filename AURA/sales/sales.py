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
from selenium.common.exceptions import WebDriverException

class DiscountNaznach(unittest.TestCase):

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


    def test_discount_naznach(self):
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
            "#j_idt67 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(8) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Выданные скидки\"] > span").click()
        driver.find_element_by_id("tableForm:j_idt75").click()

        window_before = driver.window_handles[0]
        driver.find_element_by_id("itemForm:tabView:j_id60").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:main-table_data > tr:nth-child(4)").click()
        time.sleep(2)
        driver.find_element_by_id("toolbarform:j_idt17").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        #клиент
        window_before = driver.window_handles[0]
        driver.find_element_by_id("itemForm:tabView:client_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:table_data > tr:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_id("tableForm:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        assert driver.find_element_by_id("itemForm:tabView:clientCategories:0").get_property('disabled')
        assert driver.find_element_by_id("itemForm:tabView:productOffering_focus").get_property('disabled')
        assert driver.find_element_by_id("itemForm:tabView:productOfferingCategories:0").get_property('disabled')
        #категория клиентов
        driver.find_element_by_id("itemForm:tabView:client_clearBtn").click()
        time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:clientCategories").click()
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:clientCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        time.sleep(2)
        assert driver.find_element_by_id("itemForm:tabView:client_selectBtn").get_property('disabled')
        assert driver.find_element_by_id("itemForm:tabView:productOffering_focus").get_property('disabled')
        assert driver.find_element_by_id("itemForm:tabView:productOfferingCategories:0").get_property('disabled')
        #предложение
        driver.find_element_by_css_selector("span.ui-selectcheckboxmenu-token-icon.ui-icon.ui-icon-close").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#itemForm\:tabView\:productOffering_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:productOffering_items").click()
        #driver.find_element_by_id("itemForm:tabView:productOffering_1").click()
        time.sleep(2)
        assert driver.find_element_by_id("itemForm:tabView:client_selectBtn").get_property('disabled')
        assert driver.find_element_by_id("itemForm:tabView:clientCategories:0").get_property('disabled')
        assert driver.find_element_by_id("itemForm:tabView:productOfferingCategories:0").get_property('disabled')
        #категории предложений
        driver.find_element_by_css_selector("#itemForm\:tabView\:productOffering_label").click()
        driver.find_element_by_id("itemForm:tabView:productOffering_0").click()
        time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:productOfferingCategories").click()
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:productOfferingCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        #driver.find_element_by_css_selector(
        #    "#itemForm\:tabView\:productOfferingCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        time.sleep(2)
        assert driver.find_element_by_id("itemForm:tabView:client_selectBtn").get_property('disabled')
        assert driver.find_element_by_id("itemForm:tabView:productOffering_focus").get_property('disabled')
        assert driver.find_element_by_id("itemForm:tabView:clientCategories:0").get_property('disabled')
        driver.find_element_by_id("itemForm:j_idt304").click()
        time.sleep(2)
        driver.find_element_by_id("tableForm:j_idt75")

