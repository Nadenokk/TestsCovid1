# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class CreateAnalyzes(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_analyzes(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        #driver.get("http://127.0.0.1:48080/business/dashboard/dashboard.xhtml")
        #driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,"#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(3) > a > div").click()
        driver.find_element(By.ID,"tableForm:j_idt79").click()

        #driver.find_element(By.CSS_SELECTOR,"span.ui-button-icon-left ui-icon ui-c fa fa-plus").click()
        driver.find_element(By.ID,"itemForm:tabView:lastName").click()
        driver.find_element(By.ID,"itemForm:tabView:lastName").clear()
        driver.find_element(By.ID,"itemForm:tabView:lastName").send_keys(u"СаблинАн")
        driver.find_element(By.ID,"itemForm:tabView:firstName").click()
        driver.find_element(By.ID,"itemForm:tabView:firstName").clear()
        driver.find_element(By.ID,"itemForm:tabView:firstName").send_keys(u"Роман")
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").click()
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").clear()
        driver.find_element(By.ID,"itemForm:tabView:patronymicName").send_keys(u"Евгеньевич")
        driver.find_element(By.ID,"itemForm:tabView:passportNumber").click()
        driver.find_element(By.ID,"itemForm:tabView:passportNumber").clear()
        driver.find_element(By.ID,"itemForm:tabView:passportNumber").send_keys("478965")
        driver.find_element(By.ID,"itemForm:tabView:birthDateStr").click()
        driver.find_element(By.ID,"itemForm:tabView:birthDateStr").clear()
        driver.find_element(By.ID,"itemForm:tabView:birthDateStr").send_keys("11.11.1980")
        driver.find_element(By.ID,"itemForm:tabView:phone").click()
        driver.find_element(By.ID,"itemForm:tabView:phone").click()
        driver.find_element(By.ID,"itemForm:tabView:phone").clear()
        driver.find_element(By.ID,"itemForm:tabView:phone").send_keys("745698512457777")
        driver.find_element(By.ID,"itemForm:tabView:email").click()
        driver.find_element(By.ID,"itemForm:tabView:email").clear()
        driver.find_element(By.ID,"itemForm:tabView:email").send_keys("123@321")
        driver.find_element(By.ID,"itemForm:tabView:otherCountry_label").click()
        driver.find_element(By.CSS_SELECTOR,"#itemForm\:tabView\:otherCountry_items").click()
        driver.find_element(By.ID,"itemForm:tabView:otherCountry_1").click()
        driver.find_element(By.ID,"itemForm:tabView:otherCountryCity").click()
        driver.find_element(By.ID,"itemForm:tabView:otherCountryCity").clear()
        driver.find_element(By.ID,"itemForm:tabView:otherCountryCity").send_keys(u"Ярославль")
        driver.find_element(By.ID,"itemForm:tabView:otherCountryPeriod").click()
        driver.find_element(By.ID,"itemForm:tabView:otherCountryPeriod").clear()
        driver.find_element(By.ID,"itemForm:tabView:otherCountryPeriod").send_keys("11.11.2020")
        driver.find_element(By.CSS_SELECTOR,"span.ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,"span.ui-chkbox-icon.ui-icon.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,"div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover > span.ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,"div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover.ui-state-active > span.ui-chkbox-icon.ui-icon.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,"div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover > span.ui-chkbox-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,"div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-hover.ui-state-active > span.ui-chkbox-icon.ui-icon.ui-c").click()
        driver.find_element(By.ID,"itemForm:tabView:result").click()
        driver.find_element(By.ID,"itemForm:tabView:result").clear()
        driver.find_element(By.ID,"itemForm:tabView:result").send_keys(u"Нет")

        driver.find_element(By.CSS_SELECTOR,"body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        driver.find_element(By.ID,"itemForm:j_id4").click()
        driver.find_element(By.ID,"tableForm:j_idt79")


if __name__ == "__main__":
    unittest.main()
