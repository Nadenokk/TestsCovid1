# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class LabPlanshet1(unittest.TestCase):
    def setUp(self):

        download_dir = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\Filling_Lab_Tablets\\downloads_exel"
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
        time.sleep(25)
        driver.find_elements(By.CSS_SELECTOR,
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(25)
        barcode = \
            driver.find_elements(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(1)")[
                0].text
        iss = driver.find_elements(By.CSS_SELECTOR,"#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(3)")[
            0].text


        driver.find_element(By.CSS_SELECTOR,"#j_idt71 > div.nano.layout-tabmenu-nav > ul > li:nth-child(2) > a > div").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Лабораторные планшеты\"] > span").click()
        driver.find_element(By.ID,"buttonsForm:j_idt94").click()
        driver.find_element(By.ID,"buttonsForm:j_idt97").click()
        #driver.find_element(By.ID,"barcodeForm:j_idt109").click()
        #driver.find_element(By.ID,"barcodeForm:j_idt109").click()
        #driver.find_element(By.CSS_SELECTOR,"td").click()

        driver.find_element(By.ID,"barcodeForm:barcode-input").clear()
        driver.find_element(By.ID,"barcodeForm:barcode-input").send_keys(barcode)
        driver.find_element(By.ID,"barcodeForm:barcode-input").send_keys(Keys.ENTER)
        time.sleep(10)
        assert driver.find_element(By.CSS_SELECTOR,"#tabletForm\:tube_1_7_content > span.content-value").text == iss
        driver.find_element(By.CSS_SELECTOR,"#buttonsForm\:j_idt95").click()
        #driver.find_element(By.NAME,"buttonsForm:j_idt103").click()


        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
