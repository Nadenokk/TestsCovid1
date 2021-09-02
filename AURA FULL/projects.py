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
from glob import glob
import os.path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class Cart(unittest.TestCase):

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

    def test_create_cart(self):
        driver = self.driver
        driver.get("http://auraep.ru:8180/business/dashboard/dashboard.xhtml")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("supervisor")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()

        driver.find_element_by_css_selector(
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(2) > a").click()
        driver.find_element_by_id("toolbarform:j_idt73").click()
        driver.find_element_by_id("itemForm:tabView:name").click()
        driver.find_element_by_id("itemForm:tabView:name").clear()
        name=self.generate_random_string()
        driver.find_element_by_id("itemForm:tabView:name").send_keys(name)
        driver.find_element_by_id("itemForm:tabView:startDate_input").click()
        #driver.find_element_by_id("itemForm:tabView:startDate_input").clear()
        for date in "1202.80.30":
            driver.find_element_by_id("itemForm:tabView:startDate_input").send_keys(Keys.HOME, date)
        time.sleep(2)
        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("itemForm:tabView:finishDate_input").click()
        driver.find_element_by_id("itemForm:tabView:finishDate_input").clear()
        for date in "2202.80.30":
            driver.find_element_by_id("itemForm:tabView:finishDate_input").send_keys(Keys.HOME, date)
        time.sleep(2)

        driver.find_element_by_css_selector("#itemForm\:tabView\:projectManager_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:projectManager_items").click()
        driver.find_element_by_id("itemForm:tabView:projectManager_3").click()

        driver.find_element_by_id("itemForm:tabView:categories").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:categories_panel").click()
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(5) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(7) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body").click()

        driver.find_element_by_css_selector("#itemForm\:tabView\:projectPlan_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:projectPlan_items").click()
        driver.find_element_by_id("itemForm:tabView:projectPlan_3").click()

        driver.find_element_by_id("itemForm:tabView:description").click()
        driver.find_element_by_id("itemForm:tabView:description").clear()
        driver.find_element_by_id("itemForm:tabView:description").send_keys("Описание")

        driver.find_element_by_id("itemForm:tabView:foldersTemplateName").click()
        driver.find_element_by_id("itemForm:tabView:foldersTemplateName").clear()
        driver.find_element_by_id("itemForm:tabView:foldersTemplateName").send_keys("Шаблон")
        driver.find_element_by_xpath(
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        driver.find_element_by_id("itemForm:tabView:plannedBudget").click()
        driver.find_element_by_id("itemForm:tabView:plannedBudget").clear()
        driver.find_element_by_id("itemForm:tabView:plannedBudget").send_keys("500")
        driver.find_element_by_id("itemForm:tabView:financialProjectNumber").click()
        driver.find_element_by_id("itemForm:tabView:financialProjectNumber").clear()
        driver.find_element_by_id("itemForm:tabView:financialProjectNumber").send_keys("1")
        driver.find_element_by_id("itemForm:tabView:tf_income_add").click()
        driver.find_element_by_id("tableFieldItemForm:date_input").click()
        driver.find_element_by_id("tableFieldItemForm:date_input").clear()
        for date in "2202.80.30":
            driver.find_element_by_id("tableFieldItemForm:date_input").send_keys(Keys.HOME, date)
        time.sleep(2)

        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm:moneyFlow_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)

        driver.find_element_by_id("tableFieldItemForm:description").click()
        driver.find_element_by_id("tableFieldItemForm:description").clear()
        driver.find_element_by_id("tableFieldItemForm:description").send_keys("Комментарий")

        driver.find_element_by_id("tableFieldItemForm:plan").click()
        driver.find_element_by_id("tableFieldItemForm:plan").clear()
        driver.find_element_by_id("tableFieldItemForm:plan").send_keys("1")

        driver.find_element_by_id("tableFieldItemForm:fact").click()
        driver.find_element_by_id("tableFieldItemForm:fact").clear()
        driver.find_element_by_id("tableFieldItemForm:fact").send_keys("1")
        driver.find_element_by_id("tableFieldItemForm:saveTableButton").click()

        driver.find_element_by_id("itemForm:tabView:tf_outcome_add").click()
        time.sleep(2)
        driver.find_element_by_id("tableFieldItemForm:date_input").click()
        driver.find_element_by_id("tableFieldItemForm:date_input").clear()
        for date in "2202.80.30":
            driver.find_element_by_id("tableFieldItemForm:date_input").send_keys(Keys.HOME, date)
        time.sleep(2)

        window_before = driver.window_handles[0]
        driver.find_element_by_id("tableFieldItemForm:moneyFlow_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)

        driver.find_element_by_id("tableFieldItemForm:description").click()
        driver.find_element_by_id("tableFieldItemForm:description").clear()
        driver.find_element_by_id("tableFieldItemForm:description").send_keys("Комментарий")

        driver.find_element_by_id("tableFieldItemForm:plan").click()
        driver.find_element_by_id("tableFieldItemForm:plan").clear()
        driver.find_element_by_id("tableFieldItemForm:plan").send_keys("1")

        driver.find_element_by_id("tableFieldItemForm:fact").click()
        driver.find_element_by_id("tableFieldItemForm:fact").clear()
        driver.find_element_by_id("tableFieldItemForm:fact").send_keys("1")
        driver.find_element_by_id("tableFieldItemForm:saveTableButton").click()
        driver.find_element_by_id("itemForm:tabView:j_id72").click()
        driver.find_element_by_id("toolbarform:j_idt73")
        driver.find_element_by_id("tableForm:main-table:j_id11").click()
        driver.find_element_by_id("tableForm:main-table:j_id11").clear()
        driver.find_element_by_id("tableForm:main-table:j_id11").send_keys(name)
        time.sleep(2)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == name





