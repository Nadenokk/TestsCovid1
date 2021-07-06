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

    def test_edit_tablet(self):
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

        wait = WebDriverWait(driver, 10)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles
        actionChains = ActionChains(driver)
        actionChains.double_click(driver.find_element_by_id("tableForm:main-table_data")).perform()
        wait.until(ec.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        driver.find_element_by_id("itemForm:tabView:compileDate_input").click()
        driver.find_element_by_id("itemForm:tabView:compileDate_input").clear()
        for date in "11111111 1111":
            driver.find_element_by_id("itemForm:tabView:compileDate_input").send_keys(Keys.HOME, date)
        time.sleep(2)
        driver.find_element_by_css_selector("body").click()
        window_before = driver.window_handles[1]
        driver.find_element_by_id("itemForm:tabView:labContractor_selectBtn").click()
        window_after = driver.window_handles[2]
        driver.switch_to.window(window_after)
        driver.find_element_by_id("tableForm:main-table:j_id5").click()
        driver.find_element_by_id("tableForm:main-table:j_id5").clear()
        driver.find_element_by_id("tableForm:main-table:j_id5").send_keys(u"един")
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        # driver.find_element_by_css_selector(
        #    "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable.ui-state-hover").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element_by_id("itemForm:j_id4").click()
        time.sleep(63)

        driver.close()
        driver.switch_to.window(current_window)
        time.sleep(3)
        driver.refresh()
        time.sleep(3)
        driver.find_element_by_id("tableForm:j_idt88").send_keys("05В102447")
        driver.find_element_by_id("tableForm:j_idt85_input").clear()
        driver.find_element_by_id("tableForm:j_idt91").click()
        time.sleep(7)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']/tr[" + str(1) + "]/td[" + str(1) + "]").text == "05В102447"

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()





