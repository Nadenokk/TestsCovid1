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

class CovidResearchByInstitution(unittest.TestCase):
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


    def test_covid_research_by_institution(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/reports/reports-list")
        # driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()

        driver.find_element(By.ID,"reportsForm:j_idt79:16:j_idt81").click()

        #фильтры
        driver.find_element(By.ID,"buildForm:j_idt80_input").click()
        driver.find_element(By.ID,"buildForm:j_idt80_input").clear()
        driver.find_element(By.ID,"buildForm:j_idt80_input").send_keys("01.08.21 00:00")
        driver.find_element(By.ID,"buildForm:j_idt82_input").click()
        driver.find_element(By.ID,"buildForm:j_idt82_input").clear()
        driver.find_element(By.ID,"buildForm:j_idt82_input").send_keys("16.08.21 23:59")
        driver.find_element(By.ID,"buildForm:j_idt88:j_idt91").click()
        time.sleep(6)
        driver.find_element(By.ID,"buildForm:j_idt88:j_idt96:j_idt98:1:filter").click()
        driver.find_element(By.ID,"buildForm:j_idt88:j_idt96:j_idt98:1:filter").clear()
        driver.find_element(By.ID,"buildForm:j_idt88:j_idt96:j_idt98:1:filter").send_keys("Веселая"+ Keys.ENTER)
        time.sleep(3)
        # driver.find_element(By.ID,"buildForm:j_idt89:j_idt96").click()
        driver.find_element(By.XPATH,"//td[contains(text(), 'ООО \"ВЕСЕЛАЯ УЛЫБКА\"')]").click()
        #driver.find_element(By.ID,"buildForm:j_idt87:tree-select-send-institutions-Table:0:j_idt102").click()
        driver.find_element(By.ID,"buildForm:j_idt88:j_idt101").click()

        driver.find_element(By.ID,"buildForm:j_idt104").click()
        # driver.find_element(By.ID,"buildForm:j_idt79_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#buildForm\:j_idt104_panel").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#buildForm\:j_idt104_panel > div.ui-widget-header.ui-corner-all.ui-selectcheckboxmenu-header.ui-helper-clearfix > div.ui-chkbox.ui-widget > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-active").click()
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR,
            "#buildForm\:j_idt104_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#buildForm\:j_idt104_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(7) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,"body").click()

        driver.find_element(By.ID,"buildForm:j_idt106").click()
        # driver.find_element(By.ID,"buildForm:j_idt79_label").click()
        driver.find_element(By.CSS_SELECTOR,"#buildForm\:j_idt106_panel").click()
        #driver.find_element(By.CSS_SELECTOR,
        #    "#buildForm\:j_idt100_panel > div.ui-widget-header.ui-corner-all.ui-selectcheckboxmenu-header.ui-helper-clearfix > div.ui-chkbox.ui-widget > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default.ui-state-active > span").click()

        driver.find_element(By.CSS_SELECTOR,
            "#buildForm\:j_idt106_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#buildForm\:j_idt106_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#buildForm\:j_idt106_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(5) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#buildForm\:j_idt106_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(6) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#buildForm\:j_idt106_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(7) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()

        driver.find_element(By.CSS_SELECTOR,"body").click()
        driver.find_element(By.ID,"buildForm:j_idt85").click()
        time.sleep(2)

        assert (driver.find_element(By.ID,"dataForm:j_idt119").text == "01.08.2021")
        assert (driver.find_element(By.ID,"dataForm:j_idt121").text == "16.08.2021")
        assert (driver.find_element(By.ID,"dataForm:j_idt123").text == "1, Юго-Западный; ФБУЗ \"Центр гигиены и эпидемиологии в городе Санкт-Петербург\", ул. Оборонная, д. 35")
        assert (driver.find_element(By.ID,"dataForm:j_idt125").text == "Определение наличия РНК SARS-CoV-2")
        assert (driver.find_element(By.ID,"dataForm:j_idt127").text == "Набор реагентов для выявления РНК коронавируса SARS-CoV-2 методом ОТ-ПЦР в режиме реального времени \"РеалБест РНК SARS-CoV-2\"")
        assert (driver.find_element(By.ID,"dataForm:j_idt131").text == "2")

        driver.find_element(By.ID,"buildForm:exportBtn").click()
        time.sleep(3)

        rootpath = 'C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\otchet\\downloads_exel'
        filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
        filelist = [f for f in filelist if os.path.isfile(f)]
        newest = max(filelist, key=lambda x: os.stat(x).st_mtime)

        wb = load_workbook(newest)
        sheet_ranges = wb['1']
        str1 = sheet_ranges['A22'].value
        status1 = sheet_ranges['A23'].value
        status2 = sheet_ranges['A28'].value
        status22 = sheet_ranges['A30'].value

        assert (str1 == "Учреждение, направившее материал: ООО \"ВЕСЕЛАЯ УЛЫБКА\"")
        assert (status1 or status2 or status22 == "SARS-CoV-2 - подтверждено")


if __name__ == "__main__":
    unittest.main()
