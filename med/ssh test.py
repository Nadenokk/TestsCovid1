#!/usr/bin/env python
#coding:utf-8
 # Добро пожаловать в публичный аккаунт WeChat: технология Bit by Bit
 # Вот надежные, ценные и растущие вместе, эксклюзив для сетевой осады льва

import paramiko, time
from paramiko.ssh_exception import NoValidConnectionsError,AuthenticationException
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
import os

def ssh_client(host, user, cmds, verbose=True):
         # Путь для хранения файла закрытого ключа
    private = paramiko.RSAKey.from_private_key_file(r'C:\Users\wd10\PycharmProjects\TestsCov\med\id_rsa')
         # Создаем экземпляр
    ssh = paramiko.SSHClient()
         # Загрузить системный SSH-ключ
    ssh.load_system_host_keys()
         # Автоматически добавлять стратегию, сохранять имя хоста сервера и ключевую информацию, если вы не добавите, то хост, который не записан в локальном файле know_hosts, не сможет подключиться, и значение по умолчанию будет отклонено
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
         # Подключить устройство
    try:
        ssh.connect(hostname=host,
                    username=user,
                    timeout=5,
                    compress=True,
                    pkey = private, # можно использовать подключение по ключу
                    )
        print ("Подключение к хосту {} .....")
    except NoValidConnectionsError:
                 print ('Проблема с подключением')
    except AuthenticationException:
                 print ('Неверное имя пользователя или пароль')
    except Exception as e:
                 print ('Другие проблемы с ошибками {)')
    finally:
                 # Активировать интерактивную оболочку
        chan = ssh.invoke_shell()
        time.sleep(1)

        for cmd in cmds:
            chan.send(cmd.encode())
                         # Должен быть возврат каретки 'Enter' это действие
            chan.send(b'\n')
            time.sleep(2)
            r = chan.recv(40960).decode()
            if verbose:
                print(r)
        chan.close()
        ssh.close()

def sftp_get(ip, user, local_file,remote_file, port=22):
    private = paramiko.RSAKey.from_private_key_file(r'C:\Users\wd10\PycharmProjects\TestsCov\med\id_rsa')
    # Создаем экземпляр
    ssh = paramiko.SSHClient()
    # Загрузить системный SSH-ключ
    ssh.load_system_host_keys()
    # Автоматически добавлять стратегию, сохранять имя хоста сервера и ключевую информацию, если вы не добавите, то хост, который не записан в локальном файле know_hosts, не сможет подключиться, и значение по умолчанию будет отклонено
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключить устройство
    try:
        t = paramiko.Transport(ip, port)
        t.connect(username=user, pkey = private)
        sftp = paramiko.SFTPClient.from_transport(t)
        yesterday = time.strftime('%d%m%Y', time.gmtime(time.time() - 86400))
        yestermonth = time.strftime('%m%Y', time.gmtime(time.time() - 86400))
        print(yesterday, yestermonth)
        files = sftp.listdir(remote_file + '/' + yestermonth + '/' + yesterday)
        print (files)
        print (yesterday, yestermonth)
        for file in files:
            file_remote = remote_file + '/'+yestermonth+'/' +yesterday+ '/' + file
            file_local = local_file + '\\' + file
            print (file_remote + '>>>' + file_local)
            sftp.get(file_remote, file_local)
        t.close()

    except Exception as e:
        print(e)


def sftp_put(ip, user, pwd, local_file, remote_file, port=22):
    try:
        t = paramiko.Transport(ip, port)
        t.connect(username=user, password=pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put(local_file, remote_file)
        t.close()

    except Exception as e:
        print(e)



if __name__ == '__main__':

    ip = '31.187.96.100'
    user= 'nadya'
    # local_file = r'D:\test\123.txt'
    # remote_file = 'flash:/vrpcfg.zip'
    # sftp_put(ip='192.168.0.200', user=user, pwd=pwd, local_file=local_file, remote_file='flash:/123.txt')
    sftp_get(ip='31.187.96.100', user="nadya", remote_file="/home/nadya/namepapka", local_file=r'C:\Users\wd10\PycharmProjects\TestsCov\med\vichnewssh11')


    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Ie(r"C:\Users\wd10\PycharmProjects\TestsCov\IEDriverServer.exe")
    driver = driver
    # driver.get("http://195.19.96.255:8981/documents/")
    # driver.get("http://rpn19.ru:9880/business/dashboard/dashboard.xhtml")
    driver.get("https://medblank.iac.spb.ru/uc/index.html")
    driver.find_element(By.XPATH, '//input[@name="xmlString"]').click()
    autoit.win_wait("Безопасность Windows")
    autoit.win_activate("Безопасность Windows")
    autoit.send("{TAB}")
    autoit.send("{ENTER}")
    driver.find_element(By.XPATH, "//div[@id='usual']/a[2]").click()

    dir_name = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\vichnewssh11"
    names = os.listdir(dir_name)
    for name in names:
        driver.find_element(By.ID, 'uploadForm1')
        driver.find_element(By.ID, 'uploadFile').send_keys(dir_name + "\\" + name)
        # time.sleep(1)
        driver.find_element(By.XPATH, '//input[@value="Загрузить"]').click()
        # time.sleep(3)
        driver.find_element(By.XPATH, '//input[@id="submitForm"]').click()
        autoit.win_wait("Безопасность Windows")
        autoit.win_activate("Безопасность Windows")
        autoit.send("{TAB}")
        autoit.send("{ENTER}")
        driver.find_element(By.XPATH, "//div[@id='msgSendResult']/a").click()
    driver.close()
    #удаление файлов в локальной папке
    for the_file in os.listdir(dir_name):
        file_path = os.path.join(dir_name, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
