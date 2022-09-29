# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os


class DownloadDTVector(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_download_rez_DT_vector(self):
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
            "#j_idt70 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(6) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Загрузка результатов\"] > span").click()
        x = driver.find_element(By.CSS_SELECTOR,u"a[title=\"Загрузка результатов\"] > span").get_attribute("textContent")

        driver.find_element(By.ID,"toolbarform:j_idt78").click()
        button = driver.find_element(By.ID,"j_idt90:j_idt92_input")
        button.send_keys("C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\rezultat_issledov\\test.xlsx")
        time.sleep(10)
        string=driver.find_element(By.ID,"messageInError").text
        str = string.split("\n")
        assert str[0] == 'Пожалуйста, не закрывайте диалоговое окно до завершения работы'
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[@id='messageInError' and contains(text(), "'Результат'")]")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

if __name__ == "__main__":
    unittest.main()


