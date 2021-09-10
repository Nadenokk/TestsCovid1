
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
from openpyxl import load_workbook


class CreateOrder(unittest.TestCase):

    def setUp(self):
        download_dir = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\SAU2\\otchets\\excel_downloads"
        chrome_options = webdriver.ChromeOptions()
        preferences = {"download.default_directory": download_dir,
                       "directory_upgrade": True,
                       "safebrowsing.enabled": True}
        chrome_options.add_experimental_option("prefs", preferences)
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe", options=chrome_options)
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True


    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))
        return rand_string

    def test_create_order(self):
        driver = self.driver
        driver.get("http://auraep.ru:11080/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("supervisor")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(3) > a").click()
        driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").click()
        driver.find_element_by_id("toolbarform:j_idt75").click()
        driver.find_element_by_id("itemForm:tabView:location").click()
        driver.find_element_by_id("itemForm:tabView:location").clear()
        driver.find_element_by_id("itemForm:tabView:location").send_keys("ООО Здоровый дух в здоровом теле")
        driver.find_element_by_id("itemForm:tabView:dateBegin_input").click()
        driver.find_element_by_id("itemForm:tabView:dateBegin_input").clear()
        driver.find_element_by_id("itemForm:tabView:dateBegin_input").send_keys("09.09.2021")
        driver.find_element_by_id("itemForm:tabView:dateEnd_input").click()
        driver.find_element_by_id("itemForm:tabView:dateEnd_input").clear()
        driver.find_element_by_id("itemForm:tabView:dateEnd_input").send_keys("09.09.2122")
        driver.find_element_by_id("itemForm:tabView:numSuffer").click()
        driver.find_element_by_id("itemForm:tabView:numSuffer").clear()
        driver.find_element_by_id("itemForm:tabView:numSuffer").send_keys("0")
        #driver.find_element_by_id("itemForm:tabView:preDiag_selectBtn").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_id("itemForm:tabView:preDiag_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_id("tableForm:main-table:j_id10").click()
        driver.find_element_by_id("tableForm:main-table:j_id10").clear()
        driver.find_element_by_id("tableForm:main-table:j_id10").send_keys(u"голово")
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        window_before = driver.window_handles[0]
        driver.find_element_by_id("itemForm:tabView:finalDiag_selectBtn").click()
        time.sleep(2)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_id("tableForm:main-table:j_id10").click()
        driver.find_element_by_id("tableForm:main-table:j_id10").clear()
        driver.find_element_by_id("tableForm:main-table:j_id10").send_keys(u"Эсгибиционизм")
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        driver.find_element_by_id("itemForm:tabView:symptoms").click()
        driver.find_element_by_id("itemForm:tabView:symptoms").clear()
        driver.find_element_by_id("itemForm:tabView:symptoms").send_keys("Повышенная любознательность")
        driver.find_element_by_id("itemForm:tabView:insureHardness").click()
        driver.find_element_by_id("itemForm:tabView:insureHardness").clear()
        driver.find_element_by_id("itemForm:tabView:insureHardness").send_keys("10")
        driver.find_element_by_id("itemForm:tabView:hospitalized").click()
        driver.find_element_by_id("itemForm:tabView:hospitalized").clear()
        driver.find_element_by_id("itemForm:tabView:hospitalized").send_keys("10")
        driver.find_element_by_id("itemForm:tabView:infected").click()
        driver.find_element_by_id("itemForm:tabView:infected").clear()
        driver.find_element_by_id("itemForm:tabView:infected").send_keys("10")
        driver.find_element_by_id("itemForm:tabView:orgCharact").click()
        driver.find_element_by_id("itemForm:tabView:orgCharact").clear()
        driver.find_element_by_id("itemForm:tabView:orgCharact").send_keys("10")
        driver.find_element_by_id("itemForm:tabView:sanepidEvent").click()
        driver.find_element_by_id("itemForm:tabView:sanepidEvent").clear()
        driver.find_element_by_id("itemForm:tabView:sanepidEvent").send_keys("09.09.2020")
        driver.find_element_by_id("itemForm:tabView:contingent").click()
        driver.find_element_by_id("itemForm:tabView:contingent").clear()
        driver.find_element_by_id("itemForm:tabView:contingent").send_keys("Динозаврики")
        driver.find_element_by_id("itemForm:tabView:situationDynamics").click()
        driver.find_element_by_id("itemForm:tabView:situationDynamics").clear()
        driver.find_element_by_id("itemForm:tabView:situationDynamics").send_keys("Динозаврики")
        driver.find_element_by_id("itemForm:tabView:epidSituationLocal").click()
        driver.find_element_by_id("itemForm:tabView:epidSituationLocal").clear()
        driver.find_element_by_id("itemForm:tabView:epidSituationLocal").send_keys("Динозаврики")
        driver.find_element_by_id("itemForm:tabView:tf_questResearchResults_add").click()
        driver.find_element_by_id("tableFieldItemForm:number").click()
        driver.find_element_by_id("tableFieldItemForm:number").clear()
        driver.find_element_by_id("tableFieldItemForm:number").send_keys("1")
        driver.find_element_by_id("tableFieldItemForm:materialName").click()
        driver.find_element_by_id("tableFieldItemForm:materialName").clear()
        driver.find_element_by_id("tableFieldItemForm:materialName").send_keys("мазок")
        driver.find_element_by_id("tableFieldItemForm:numberSamplesTaken").click()
        driver.find_element_by_id("tableFieldItemForm:numberSamplesTaken").clear()
        driver.find_element_by_id("tableFieldItemForm:numberSamplesTaken").send_keys("5")
        driver.find_element_by_id("tableFieldItemForm:numberSamplesTakenNonStandard").click()
        driver.find_element_by_id("tableFieldItemForm:numberSamplesTakenNonStandard").clear()
        driver.find_element_by_id("tableFieldItemForm:numberSamplesTakenNonStandard").send_keys("3")
        driver.find_element_by_id("tableFieldItemForm:pathogenDetected").click()
        driver.find_element_by_id("tableFieldItemForm:pathogenDetected").clear()
        driver.find_element_by_id("tableFieldItemForm:pathogenDetected").send_keys("1")
        driver.find_element_by_id("tableFieldItemForm:regulatoryDocument").click()
        driver.find_element_by_id("tableFieldItemForm:regulatoryDocument").clear()
        driver.find_element_by_id("tableFieldItemForm:regulatoryDocument").send_keys("m1")
        driver.find_element_by_id("tableFieldItemForm:saveTableButton").click()


        driver.find_element_by_css_selector("body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        driver.find_element_by_id("itemForm:j_id4").click()
        time.sleep(5)