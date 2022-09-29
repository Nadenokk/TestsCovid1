# -*- coding: utf-8 -*-
import glob
#COV-1010 Не выгружаются адреса в отчет /reports/covid-research-by-institution

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
from openpyxl import load_workbook

class CovidResearchByInstitutionNewBySections(unittest.TestCase):
    def setUp(self):
        download_dir = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\otchet\\downloads_exel"
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


    def test_covid_research_by_institution_new_by_sections(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/reports/reports-list")
        #driver.get("http://127.0.0.1:48080/business/dashboard/dashboard.xhtml")
        # driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.ID,"reportsForm:j_idt79:9:j_idt81").click()

        #фильтры
        driver.find_element(By.ID,"buildForm:j_idt80_input").click()
        driver.find_element(By.ID,"buildForm:j_idt80_input").clear()
        for date in "1202.80.10":
            driver.find_element(By.ID,"buildForm:j_idt80_input").send_keys(Keys.HOME, date)
        driver.find_element(By.ID,"buildForm:j_idt82_input").click()
        driver.find_element(By.ID,"buildForm:j_idt82_input").clear()
        for date in "1202.80.61":
            driver.find_element(By.ID,"buildForm:j_idt82_input").send_keys(Keys.HOME, date)

        driver.find_element(By.ID,"buildForm:j_idt84").click()
        time.sleep(4)
        assert (driver.find_element(By.ID,"dataForm:j_idt89").text == "01.08.2021 00:00 - 16.08.2021 23:59")
        assert (driver.find_element(By.ID,"dataForm:j_idt91").text == "Определение наличия РНК SARS-CoV-2")
        assert (driver.find_element(By.ID,
            "dataForm:j_idt93").text == "Набор реагентов для выявления РНК коронавируса SARS-CoV-2 методом ОТ-ПЦР в режиме реального времени \"РеалБест РНК SARS-CoV-2\"")
        assert (driver.find_element(By.ID,"dataForm:j_idt156").text == "562")

        driver.find_element(By.ID,"buildForm:j_idt85").click()
        time.sleep(2)

        rootpath = 'C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\otchet\\downloads_exel'
        filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
        filelist = [f for f in filelist if os.path.isfile(f)]
        newest = max(filelist, key=lambda x: os.stat(x).st_mtime)

        wb = load_workbook(newest)
        sheet_ranges = wb['1']
        str1 = sheet_ranges['A22'].value

        assert (str1 == "Учреждение, направившее материал: СПб ГБУЗ «ГБ №40»")


if __name__ == "__main__":
    unittest.main()

