
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
        driver.get("http://sau.rpn19.ru:11080/documents")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("supervisor")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("zgA8SlfS")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(3) > a").click()
        driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").click()

        time.sleep(2)
        driver.find_element(By.ID,"toolbarform:j_idt75").click()
        name = self.generate_random_string()
        driver.find_element(By.ID,"itemForm:tabView:location").click()
        driver.find_element(By.ID,"itemForm:tabView:location").clear()
        driver.find_element(By.ID,"itemForm:tabView:location").send_keys(name)
        driver.find_element(By.ID,"itemForm:tabView:dateBegin_input").click()
        driver.find_element(By.ID,"itemForm:tabView:dateBegin_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:dateBegin_input").send_keys("09.09.2021")
        driver.find_element(By.ID,"itemForm:tabView:dateEnd_input").click()
        driver.find_element(By.ID,"itemForm:tabView:dateEnd_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:dateEnd_input").send_keys("09.09.2122")
        driver.find_element(By.ID,"itemForm:tabView:numSuffer").click()
        driver.find_element(By.ID,"itemForm:tabView:numSuffer").clear()
        driver.find_element(By.ID,"itemForm:tabView:numSuffer").send_keys("0")
        #driver.find_element(By.ID,"itemForm:tabView:preDiag_selectBtn").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:preDiag_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id11").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id11").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id11").send_keys(u"голово")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:finalDiag_selectBtn").click()
        time.sleep(2)
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id11").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id11").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id11").send_keys(u"Эсгибиционизм")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        driver.find_element(By.ID,"itemForm:tabView:symptoms").click()
        driver.find_element(By.ID,"itemForm:tabView:symptoms").clear()
        driver.find_element(By.ID,"itemForm:tabView:symptoms").send_keys("Повышенная любознательность")
        driver.find_element(By.ID,"itemForm:tabView:insureHardness").click()
        driver.find_element(By.ID,"itemForm:tabView:insureHardness").clear()
        driver.find_element(By.ID,"itemForm:tabView:insureHardness").send_keys("10")
        driver.find_element(By.ID,"itemForm:tabView:hospitalized").click()
        driver.find_element(By.ID,"itemForm:tabView:hospitalized").clear()
        driver.find_element(By.ID,"itemForm:tabView:hospitalized").send_keys("10")
        driver.find_element(By.ID,"itemForm:tabView:infected").click()
        driver.find_element(By.ID,"itemForm:tabView:infected").clear()
        driver.find_element(By.ID,"itemForm:tabView:infected").send_keys("10")
        driver.find_element(By.ID,"itemForm:tabView:orgCharact").click()
        driver.find_element(By.ID,"itemForm:tabView:orgCharact").clear()
        driver.find_element(By.ID,"itemForm:tabView:orgCharact").send_keys("10")
        driver.find_element(By.ID,"itemForm:tabView:sanepidEvent").click()
        driver.find_element(By.ID,"itemForm:tabView:sanepidEvent").clear()
        driver.find_element(By.ID,"itemForm:tabView:sanepidEvent").send_keys("09.09.2020")
        driver.find_element(By.ID,"itemForm:tabView:contingent").click()
        driver.find_element(By.ID,"itemForm:tabView:contingent").clear()
        driver.find_element(By.ID,"itemForm:tabView:contingent").send_keys("Динозаврики")
        driver.find_element(By.ID,"itemForm:tabView:situationDynamics").click()
        driver.find_element(By.ID,"itemForm:tabView:situationDynamics").clear()
        driver.find_element(By.ID,"itemForm:tabView:situationDynamics").send_keys("Динозаврики")
        driver.find_element(By.ID,"itemForm:tabView:epidSituationLocal").click()
        driver.find_element(By.ID,"itemForm:tabView:epidSituationLocal").clear()
        driver.find_element(By.ID,"itemForm:tabView:epidSituationLocal").send_keys("Динозаврики")
        driver.find_element(By.ID,"itemForm:tabView:tf_questResearchResults_add").click()
        driver.find_element(By.ID,"tableFieldItemForm:number").click()
        driver.find_element(By.ID,"tableFieldItemForm:number").clear()
        driver.find_element(By.ID,"tableFieldItemForm:number").send_keys("1")
        driver.find_element(By.ID,"tableFieldItemForm:materialName").click()
        driver.find_element(By.ID,"tableFieldItemForm:materialName").clear()
        driver.find_element(By.ID,"tableFieldItemForm:materialName").send_keys("мазок")
        driver.find_element(By.ID,"tableFieldItemForm:numberSamplesTaken").click()
        driver.find_element(By.ID,"tableFieldItemForm:numberSamplesTaken").clear()
        driver.find_element(By.ID,"tableFieldItemForm:numberSamplesTaken").send_keys("5")
        driver.find_element(By.ID,"tableFieldItemForm:numberSamplesTakenNonStandard").click()
        driver.find_element(By.ID,"tableFieldItemForm:numberSamplesTakenNonStandard").clear()
        driver.find_element(By.ID,"tableFieldItemForm:numberSamplesTakenNonStandard").send_keys("3")
        driver.find_element(By.ID,"tableFieldItemForm:pathogenDetected").click()
        driver.find_element(By.ID,"tableFieldItemForm:pathogenDetected").clear()
        driver.find_element(By.ID,"tableFieldItemForm:pathogenDetected").send_keys("1")
        driver.find_element(By.ID,"tableFieldItemForm:regulatoryDocument").click()
        driver.find_element(By.ID,"tableFieldItemForm:regulatoryDocument").clear()
        driver.find_element(By.ID,"tableFieldItemForm:regulatoryDocument").send_keys("m1")
        driver.find_element(By.ID,"tableFieldItemForm:saveTableButton").click()
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:tabView:epidDiag").click()
        driver.find_element(By.ID,"itemForm:tabView:epidDiag").clear()
        driver.find_element(By.ID,"itemForm:tabView:epidDiag").send_keys("Динозаврики")
        driver.find_element(By.ID,"itemForm:tabView:fociType").click()
        driver.find_element(By.ID,"itemForm:tabView:fociType").clear()
        driver.find_element(By.ID,"itemForm:tabView:fociType").send_keys("Динозаврики")
        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:pathogen_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id8").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").send_keys(u"антиген")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:infectionSource_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id8").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").send_keys(u"не")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:infectionWay_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id8").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").send_keys(u"не")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:infectionFactor_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id8").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").send_keys(u"не")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:clinicForms_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(5)").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        window_before = driver.window_handles[0]
        driver.find_element(By.ID,"itemForm:tabView:causes_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id8").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id8").send_keys(u"не")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)

        driver.find_element(By.ID,"itemForm:tabView:violations").click()
        driver.find_element(By.ID,"itemForm:tabView:violations").clear()
        driver.find_element(By.ID,"itemForm:tabView:violations").send_keys("Динозаврики")
        driver.find_element(By.ID,"itemForm:tabView:sanepidMeasures").click()
        driver.find_element(By.ID,"itemForm:tabView:sanepidMeasures").clear()
        driver.find_element(By.ID,"itemForm:tabView:sanepidMeasures").send_keys("Динозаврики")
        driver.find_element(By.ID,"itemForm:tabView:measures").click()
        driver.find_element(By.ID,"itemForm:tabView:measures").clear()
        driver.find_element(By.ID,"itemForm:tabView:measures").send_keys("Динозаврики")

        driver.find_element(By.ID,"itemForm:tabView:coordX").click()
        driver.find_element(By.ID,"itemForm:tabView:coordX").clear()
        driver.find_element(By.ID,"itemForm:tabView:coordX").send_keys("666")
        driver.find_element(By.ID,"itemForm:tabView:coordY").click()
        driver.find_element(By.ID,"itemForm:tabView:coordY").clear()
        driver.find_element(By.ID,"itemForm:tabView:coordY").send_keys("666")
        driver.find_element(By.CSS_SELECTOR,"body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(3) + "]").text == name