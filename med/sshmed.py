#!/usr/bin/env python
#coding:utf-8
#https://russianblogs.com/article/11521237074/

import paramiko, time
from paramiko.ssh_exception import NoValidConnectionsError,AuthenticationException
# -*- coding: utf-8 -*-
import shutil
import time
import autoit
import paramiko
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import time
from selenium.webdriver.ie.service import Service
from selenium.webdriver.chrome.options import Options

def sftp_get(ip, user, local_file,remote_file, port=443):
    private = paramiko.RSAKey.from_private_key_file(r'C:\Users\wd10\PycharmProjects\TestsCov\med\id_rsa')
    # Создаем экземпляр
    ssh = paramiko.SSHClient()
    # Загрузить системный SSH-ключ
    ssh.load_system_host_keys()
    # Автоматически добавлять стратегию, сохранять имя хоста сервера и ключевую информацию, если вы не добавите, то хост, который не записан в локальном файле know_hosts, не сможет подключиться, и значение по умолчанию будет отклонено
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключить устройство
    try:
        t = paramiko.Transport((ip, port))
        t.connect(username=user, pkey=private)


        sftp = paramiko.SFTPClient.from_transport(t)

        yesterday = time.strftime('%d%m%Y', time.gmtime(time.time() - 86400))
        yestermonth = time.strftime('%m%Y', time.gmtime(time.time() - 86400))
        files = sftp.listdir(remote_file + '/' + yestermonth + '/' + yesterday)
        print (files)
        print (yesterday, yestermonth)
        for file in files:
            file_remote = remote_file + '/'+yestermonth+'/' +yesterday+ '/' + file
            #file_remote = remote_file + '/' + yestermonth + '/' + "20022022" + '/' + file
            file_local = local_file + '\\' + file
            print(file_remote + '>>>' + file_local)
            try:
                sftp.get(file_remote, file_local)

            except FileNotFoundError:
                print("Отсутствуют протоколы и папка со вчерашним числом")
                exit()
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
    start_time = time.time()
    ip = '195.19.96.255'
    user= 'nadya'
    sftp_get(ip='195.19.96.255', user="nadya", remote_file="/opt/wildfly/standalone/tmp/report/aids/", local_file=r'C:\Users\wd10\PycharmProjects\TestsCov\med\vichnewssh')

    #195.19.96.255 443
    #sftp_get(ip='31.187.96.100', user="nadya", remote_file="/home/nadya/namepapka", local_file=r'C:\Users\wd10\PycharmProjects\TestsCov\med\vichnewssh')

    #s = Service("C:\\Users\\wd10\\PycharmProjects\\TestsCov\\IEDriverServer.exe")
    driver = webdriver.Ie()
    driver.get("https://medblank.iac.spb.ru/uc/index.html")
    driver.find_element(By.XPATH, '//input[@name="xmlString"]').click()
    autoit.win_wait("Безопасность Windows")
    autoit.win_activate("Безопасность Windows")
    autoit.send("{TAB}")
    autoit.send("{ENTER}")
    driver.find_element(By.XPATH, "//div[@id='usual']/a[2]").click()

    dir_name = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\vichnewssh"
    dir_brak = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\done\\defect"
    dir_good = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\done\\good"
    dir_bug = "C:\\Users\\wd10\\PycharmProjects\\TestsCov\\med\\done\\bug"
    names = os.listdir(dir_name)
    count = len(names)
    print('Всего протоколов ', count)
    for name in names:
        print(name)
        driver.find_element(By.ID, 'uploadForm1')
        driver.find_element(By.ID, 'uploadFile').send_keys(dir_name + "\\" + name)
        time.sleep(1)
        driver.find_element(By.XPATH, '//input[@value="Загрузить"]').click()
        try:
            # с ошибкой
            if driver.find_element(By.XPATH, "//*[contains(@id,'submitForm') and contains(@style, 'not-allowed')]"):
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
                    print("!!!!!! нашел элемент невидимым и не кликнул на первый элемент ")
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

        count = count-1
        print('Осталось загрузить ', count)
    driver.close()
    #удаление файлов в локальной папке
    for the_file in os.listdir(dir_name):
        file_path = os.path.join(dir_name, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    print("--- %s seconds ---" % (time.time() - start_time))
