# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class LabPlanshet3(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_lab_planshet(self):
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
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(8) > a > div").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Поиск штрих-кодов\"] > span").click()
        driver.find_element(By.CSS_SELECTOR,"span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element(By.CSS_SELECTOR,
            "#filtersform\:j_idt85_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"filtersform:j_idt87").click()
        time.sleep(40)
        driver.find_elements(By.CSS_SELECTOR,
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(25)
        barcode = \
            driver.find_elements(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(1)")[
                0].text
        iss = driver.find_elements(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(3)")[
            0].text

        driver.find_element(By.CSS_SELECTOR,"#j_idt71 > div.nano.layout-tabmenu-nav > ul > li:nth-child(2) > a > div").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Лабораторные планшеты. Версия 3.0.\"] > span").click()
        #driver.find_element(By.ID,"barcodeForm:j_idt97").click()
        #driver.find_element(By.ID,"barcodeForm:j_idt97").click()
        #driver.find_element(By.CSS_SELECTOR,"td").click()

        driver.find_element(By.ID,"barcodeForm:barcode-input").clear()
        driver.find_element(By.ID,"barcodeForm:barcode-input").send_keys(barcode)
        driver.find_element(By.ID,"barcodeForm:barcode-input").send_keys(Keys.ENTER)
        time.sleep(10)
        assert driver.find_element(By.CSS_SELECTOR,"#tabletForm\:tube_1_content > span.content-value").text == iss
        driver.find_element(By.ID,"buttonsForm:j_idt90").click()
        time.sleep(2)
        #driver.find_element(By.CSS_SELECTOR,"#buttonsForm\:j_idt79")
               


if __name__ == "__main__":
    unittest.main()
