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
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait


class EditTablet(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_edit_tablet(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        #driver.get("http://127.0.0.1:48080/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(5) > a > div > div.layout-tabmenu-tooltip-text").click()
        #driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.ID,"tableForm:j_idt87_input").clear()
        #driver.find_element(By.ID,"tableForm:j_idt87_input").send_keys("01.09.2021")
        driver.find_element(By.ID,"tableForm:j_idt90").send_keys("621П1073458")
        time.sleep(1)
        driver.find_element(By.ID,"tableForm:j_idt93").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']/tr[" + str(1) + "]/td[" + str(1) + "]").text=="621П1073458"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']/tr[" + str(1) + "]/td[" + str(4) + "]").text == "01.09.21 08:03"

        wait = WebDriverWait(driver, 10)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles
        actionChains = ActionChains(driver)
        actionChains.double_click(driver.find_element(By.ID,"tableForm:main-table_data")).perform()
        wait.until(ec.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        driver.find_element(By.CSS_SELECTOR,"body.main-body").click()


        driver.find_element(By.ID,"itemForm:tabView:compileDate_input").click()
        driver.find_element(By.ID,"itemForm:tabView:compileDate_input").clear()
        driver.find_element(By.ID,"itemForm:tabView:compileDate_input").send_keys("01.09.21 08:03")
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"body").click()
        window_before = driver.window_handles[1]
        driver.find_element(By.ID,"itemForm:tabView:labContractor_selectBtn").click()
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID,"tableForm:main-table:j_id15").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id15").clear()
        driver.find_element(By.ID,"tableForm:main-table:j_id15").send_keys(u"един")
        driver.find_element(By.CSS_SELECTOR,"#tableForm").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        # driver.find_element(By.CSS_SELECTOR,
        #    "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable.ui-state-hover").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        time.sleep(15)
        driver.close()
        driver.switch_to.window(current_window)
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.ID,"tableForm:j_idt90").send_keys("621П1073458")
        driver.find_element(By.ID,"tableForm:j_idt87_input").clear()
        driver.find_element(By.ID,"tableForm:j_idt93").click()
        time.sleep(11)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']/tr[" + str(1) + "]/td[" + str(1) + "]").text == "621П1073458"

if __name__ == "__main__":
    unittest.main()




