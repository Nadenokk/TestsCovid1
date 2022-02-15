# -*- coding: utf-8 -*-
import autoit
import paramiko
from io import StringIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
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

    def ssh_client(self):

        # Абсолютный путь закрытого ключа
        private = paramiko.RSAKey.from_private_key_file(r'C:\Users\wd10\PycharmProjects\TestsCov\med\medspr_id_rsa')
        # Создаем экземпляр
        ssh = paramiko.SSHClient()
        # Загрузить системный ключ HostKeys
        ssh.load_system_host_keys()
        # Автоматически добавить политику, сохранить имя хоста и ключевую информацию удаленного хоста. Если вы не добавите его, то хост, который не записан в локальном файле know_hosts, не сможет подключиться, и значение по умолчанию будет отклонено
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # Подключиться к удаленному хосту, пароль здесь не нужен, это файл закрытого ключа
        ssh.connect('192.168.0.101', port=22, username='admin', pkey=private)
        # Выполнение заказа


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
        driver.find_element(By.XPATH, "//div[@id='usual']/a[2]").click()

        dir_name = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\vich"
        names = os.listdir(dir_name)
        for name in names:
            #print(names)
            #print(name)
            #print (dir_name + "\\"+name)
            driver.find_element(By.ID, 'uploadForm1')
            driver.find_element(By.ID, 'uploadFile').send_keys(dir_name + "\\"+name)
            time.sleep(1)
            driver.find_element(By.XPATH, '//input[@value="Загрузить"]').click()
            #button = driver.find_element(By.XPATH, '//input[@type="file"]').click()
            #button.sendFile("C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\ВИЧ_серт_шаблон_загрузка_медсправка.xml")
            time.sleep(3)
            driver.find_element(By.XPATH, '//input[@id="submitForm"]').click()
            autoit.win_wait("Безопасность Windows")
            autoit.win_activate("Безопасность Windows")
            autoit.send("{TAB}")
            autoit.send("{ENTER}")
            driver.find_element(By.XPATH, "//div[@id='msgSendResult']/a").click()
        driver.close()

