# -*- coding: utf-8 -*-
from selenium import webdriver
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



    def test_create_order_number(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")

        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()


        driver.find_element(By.CSS_SELECTOR,
            "#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(12) > a > div").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Поиск штрих-кодов\"] > span").click()
        driver.find_element(By.CSS_SELECTOR,"span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element(By.CSS_SELECTOR,"#filtersform\:j_idt85_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
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

        driver.find_element(By.CSS_SELECTOR,
            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(10) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Создание заявки\"] > span").click()

        driver.find_element(By.ID,"site-selection:j_idt161_label").click()
        driver.find_element(By.ID,"site-selection:j_idt161_1").click()
        # driver.find_element(By.XPATH,"//span[@class='ui-button-text ui-c' and @text='Выбрать']").click()
        driver.refresh()
        driver.find_element(By.ID,"site-selection:j_idt164").click()
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.ID,"participantIdDataForm:inputParticipantId").send_keys("1597898")
        driver.find_element(By.NAME,"participantIdDataForm:j_idt85").click()
        time.sleep(2)
        driver.find_element(By.ID,"participantDataForm:barcodeNumber").send_keys(barcode)
        driver.find_element(By.ID,"participantDataForm:createRequest").click()
        time.sleep(10)
        assert (driver.find_element(By.ID,"j_idt168").text) == "Заявка на исследование создана"

