# -*- coding: utf-8 -*-
import shutil

import autoit
import paramiko
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#import Alert
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
import os
import config
import datetime
import time
import io
class Medspravka(unittest.TestCase):


    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Ie()

    def test_medspravka(self):
        driver = self.driver
        # driver.get("http://195.19.96.255:8981/documents/")
        #driver.get("http://rpn19.ru:9880/business/dashboard/dashboard.xhtml")
        driver.get("https://medblank.iac.spb.ru/uc/index.html")
        driver.find_element(By.XPATH, '//input[@name="xmlString"]').click()
        autoit.win_wait("Безопасность Windows")
        autoit.win_activate("Безопасность Windows")
        autoit.send("{TAB}")
        autoit.send("{ENTER}")
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='usual']/a[2]").click()

        dir_name = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\bug"
        dir_brak = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\defect"
        dir_good = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\good"
        dir_bug = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\bugnew"
        names = os.listdir(dir_name)
        count = len(names)
        print('Всего протоколов ', count)
        for name in names:
            print(name)
            driver.find_element(By.ID, 'uploadForm1')
            driver.find_element(By.ID, 'uploadFile').send_keys(dir_name + "\\"+name)
            time.sleep(1)
            driver.find_element(By.XPATH, '//input[@value="Загрузить"]').click()
            time.sleep(2)
            try:
                # с ошибкой
                if driver.find_element(By.XPATH, "//input[@id='submitForm' and contains(@style, 'not-allowed')]"):
                    try:
                        driver.find_element(By.XPATH, "//input[@id='submitForm1']").click()
                        print("брак, но нашел первую кнопку невидимой")
                        autoit.win_wait("Безопасность Windows")
                        autoit.win_activate("Безопасность Windows")
                        autoit.send("{TAB}")
                        autoit.send("{ENTER}")
                        shutil.copy(dir_name + "\\" + name, dir_brak + "\\" + name)
                        driver.find_element(By.XPATH, "//div[@id='msgSendResult']/a").click()
                        driver.find_element(By.XPATH, "//div[@id='usual']/a[2]").click()
                    except ElementNotVisibleException:
                        print("!!!!!! нашел элемент невидимым и не кликнул на второй элемент ")
                        shutil.copy(dir_name + "\\" + name, dir_bug + "\\" + name)
            except NoSuchElementException:
                try:
                    # успешные
                    driver.find_element(By.XPATH, "//input[@id='submitForm']").click()
                    autoit.win_wait("Безопасность Windows")
                    autoit.win_activate("Безопасность Windows")
                    autoit.send("{TAB}")
                    autoit.send("{ENTER}")
                    driver.find_element(By.XPATH, "//div[@id='msgSendResult']/a").click()
                    shutil.copy(dir_name + "\\" + name, dir_good + "\\" + name)
                except ElementNotVisibleException:
                    # брак
                    driver.find_element(By.XPATH, "//input[@id='submitForm1']").click()
                    autoit.win_wait("Безопасность Windows")
                    autoit.win_activate("Безопасность Windows")
                    autoit.send("{TAB}")
                    autoit.send("{ENTER}")
                    shutil.copy(dir_name + "\\" + name, dir_brak + "\\" + name)
                    driver.find_element(By.XPATH, "//div[@id='msgSendResult']/a").click()
                    driver.find_element(By.XPATH, "//div[@id='usual']/a[2]").click()

            count = count - 1
            print('Осталось загрузить ', count)
        driver.close()
