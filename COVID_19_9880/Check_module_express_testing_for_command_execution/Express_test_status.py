# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class ExpressTestStatus(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")	
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_express_status(self):
        driver = self.driver
        barcode = "7800560979"
        iss = u"10Х396522" # u - кодировка utf-8
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
        driver.find_element(By.CSS_SELECTOR,"#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(7) > a > div").click()

        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys(barcode)
        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(10)
        assert driver.find_element(By.ID,"expressForm:j_idt82").text == iss

        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys("negative")
        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(5)
        #driver.find_element(By.CSS_SELECTOR,"#growlForm\:growl_container > div > div > div.ui-growl-message > p")
        assert driver.find_element(By.CSS_SELECTOR,"#expressForm\:j_idt95").text == iss
        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys(barcode)
        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(10)
        assert driver.find_element(By.CSS_SELECTOR,"#expressForm\:j_idt82").text == iss
        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys("positive")
        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(5)
        #driver.find_element(By.CSS_SELECTOR,"#growlForm\:growl_container > div > div > div.ui-growl-message > p")
        assert driver.find_element(By.CSS_SELECTOR,"#expressForm\:j_idt87").text == iss
        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys("clear-lists")
        driver.find_element(By.CSS_SELECTOR,"#expressForm\:inputValueId").send_keys(Keys.ENTER)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"#growlForm\:growl_container > div > div > div.ui-growl-message > p")

    


if __name__ == "__main__":
    unittest.main()
