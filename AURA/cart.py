from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver import ActionChains
import logging, os
import sys
import random
import string
from glob import glob
import os.path

from selenium.webdriver.support.wait import WebDriverWait


class CreateOrder(unittest.TestCase):

    def setUp(self):
        download_dir = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\downloads_pdf"
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

    '''    
    def genlog(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not os.path.exists("Logs"):
            os.mkdir("Logs")
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Barcode.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.barcode()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    

    def test_barcode(self):
        self.genlog()
    '''

    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))
        return rand_string

    def test_create_order(self):
        driver = self.driver
        driver.get("http://auraep.ru:8180/business/dashboard/dashboard.xhtml")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("tuilp")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("tuilp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()

        driver.find_element_by_css_selector(
            "#j_idt67 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Реестр клиентов\"] > span").click()
        driver.find_element_by_id("tableForm:j_idt76").click()
        #создание контакта
        driver.find_element_by_id("selectTypeForm:j_idt96").click()
        lastname = self.generate_random_string()
        driver.find_element_by_id("personForm:j_idt101:lastName").click()
        driver.find_element_by_id("personForm:j_idt101:lastName").clear()
        driver.find_element_by_id("personForm:j_idt101:lastName").send_keys(lastname)
        firstname = self.generate_random_string()
        driver.find_element_by_id("personForm:j_idt101:firstName").click()
        driver.find_element_by_id("personForm:j_idt101:firstName").clear()
        driver.find_element_by_id("personForm:j_idt101:firstName").send_keys(firstname)
        patronymicname = self.generate_random_string()
        driver.find_element_by_id("personForm:j_idt101:patronymicName").click()
        driver.find_element_by_id("personForm:j_idt101:patronymicName").clear()
        driver.find_element_by_id("personForm:j_idt101:patronymicName").send_keys(patronymicname)
        name = lastname+firstname+patronymicname
        driver.find_element_by_id("personForm:j_idt101:birthDate_input").click()
        driver.find_element_by_id("personForm:j_idt101:birthDate_input").clear()
        for date in "08911111":
            driver.find_element_by_id("personForm:j_idt101:birthDate_input").send_keys(Keys.HOME, date)
        driver.find_element_by_id("personForm:j_idt101:email").click()
        driver.find_element_by_id("personForm:j_idt101:email").clear()
        driver.find_element_by_id("personForm:j_idt101:email").send_keys("shamkin@proweb.ru")
        driver.find_element_by_css_selector(
            "#personForm\:j_idt101\:sex > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("personForm:j_idt101:snils").click()
        driver.find_element_by_id("personForm:j_idt101:snils").clear()
        driver.find_element_by_id("personForm:j_idt101:snils").send_keys("78945212311")
        driver.find_element_by_css_selector("#personForm\:j_idt101\:userCategory_label").click()
        driver.find_element_by_css_selector("#personForm\:j_idt101\:userCategory_items").click()
        driver.find_element_by_id("personForm:j_idt101:userCategory_2").click()
        time.sleep(2)
        driver.find_element_by_id("personForm:j_idt262").click()
        time.sleep(2)
        driver.find_element_by_id("tableForm:table:j_idt78").click()
        driver.find_element_by_id("tableForm:table:j_idt78").click()
        time.sleep(3)
        name2=driver.find_element_by_xpath("//tbody[@id='tableForm:table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text
        assert (re.match(r'(?i)' + re.sub(r'\s', '', name) + r'$', re.sub(r'\s', '', name2)))

        #создание ЮЛ
        driver.find_element_by_id("tableForm:j_idt76").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt94_label").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt94_items").click()
        driver.find_element_by_id("selectTypeForm:j_idt94_1").click()
        time.sleep(2)
        driver.find_element_by_id("selectTypeForm:j_idt96").click()
        name = self.generate_random_string()
        driver.find_element_by_id("legalForm:j_idt332:name").click()
        driver.find_element_by_id("legalForm:j_idt332:name").clear()
        driver.find_element_by_id("legalForm:j_idt332:name").send_keys(name)
        driver.find_element_by_css_selector("#legalForm\:j_idt332\:categories").click()
        driver.find_element_by_css_selector(
            "#legalForm\:j_idt332\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#legalForm\:j_idt332\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        #driver.find_element_by_id("legalForm:j_idt332:j_idt334").click()

        driver.find_element_by_id("legalForm:j_idt332:shortName").click()
        driver.find_element_by_id("legalForm:j_idt332:shortName").clear()
        driver.find_element_by_id("legalForm:j_idt332:shortName").send_keys(u"СаблинАнтител")
        driver.find_element_by_id("legalForm:j_idt332:seoName").click()
        driver.find_element_by_id("legalForm:j_idt332:seoName").clear()
        driver.find_element_by_id("legalForm:j_idt332:seoName").send_keys(u"Евгеньевич")
        driver.find_element_by_id("legalForm:j_idt332:email").click()
        driver.find_element_by_id("legalForm:j_idt332:email").clear()
        driver.find_element_by_id("legalForm:j_idt332:email").send_keys("shamkin@proweb.ru")
        driver.find_element_by_css_selector("#legalForm\:j_idt332\:userCategory_label").click()
        driver.find_element_by_css_selector("#legalForm\:j_idt332\:userCategory_items").click()
        driver.find_element_by_id("legalForm:j_idt332:userCategory_2").click()
        time.sleep(2)
        driver.find_element_by_id("legalForm:j_idt521").click()
        time.sleep(2)
        name3 = driver.find_element_by_xpath(
            "//tbody[@id='tableForm:table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text
        assert (re.match(r'(?i)' + re.sub(r'\s', '', name) + r'$', re.sub(r'\s', '', name3)))

        #создание ИП
        driver.find_element_by_id("tableForm:j_idt76").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt94_label").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt94_items").click()
        driver.find_element_by_id("selectTypeForm:j_idt94_2").click()
        time.sleep(2)
        driver.find_element_by_id("selectTypeForm:j_idt96").click()
        name = self.generate_random_string()
        driver.find_element_by_id("singleForm:j_idt612:name").click()
        driver.find_element_by_id("singleForm:j_idt612:name").clear()
        driver.find_element_by_id("singleForm:j_idt612:name").send_keys(name)
        driver.find_element_by_css_selector("#singleForm\:j_idt612\:categories").click()
        driver.find_element_by_css_selector(
            "#singleForm\:j_idt612\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#singleForm\:j_idt612\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        #driver.find_element_by_id("legalForm:j_idt332:j_idt334").click()

        driver.find_element_by_id("singleForm:j_idt612:shortName").click()
        driver.find_element_by_id("singleForm:j_idt612:shortName").clear()
        driver.find_element_by_id("singleForm:j_idt612:shortName").send_keys(u"СаблинПАСС")
        driver.find_element_by_id("singleForm:j_idt612:email").click()
        driver.find_element_by_id("singleForm:j_idt612:email").clear()
        driver.find_element_by_id("singleForm:j_idt612:email").send_keys("shamkin@proweb.ru")
        driver.find_element_by_css_selector("#singleForm\:j_idt612\:userCategory_label").click()
        driver.find_element_by_css_selector("#singleForm\:j_idt612\:userCategory_items").click()
        driver.find_element_by_id("singleForm:j_idt612:userCategory_2").click()
        time.sleep(2)
        driver.find_element_by_id("singleForm:j_idt792").click()
        time.sleep(2)
        name4 = driver.find_element_by_xpath(
            "//tbody[@id='tableForm:table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text
        assert (re.match(r'(?i)' + re.sub(r'\s', '', name) + r'$', re.sub(r'\s', '', name4)))

        #корзина
        driver.find_element_by_id("topbarForm:cartCount").click()

        assert driver.find_element_by_xpath("//a[@id='cartForm:j_idt97']//span[@style='color:#333333']").text == "Тульпова Марина"
        assert driver.find_element_by_xpath("//a[@id='cartForm:j_idt103:1:j_idt104']//span[@style='color:#333333']").text == name3
        assert driver.find_element_by_xpath("//a[@id='cartForm:j_idt103:2:j_idt104']//span[@style='color:#333333']").text == name4
        driver.find_element_by_id("cartForm:j_idt107").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt119_label").click()
        driver.find_element_by_css_selector("#selectTypeForm\:j_idt119_items").click()
        time.sleep(1)
        assert driver.find_element_by_id("selectTypeForm:j_idt119_0").text == "Юридическое лицо"
        assert driver.find_element_by_id("selectTypeForm:j_idt119_1").text == "Индивидуальный предприниматель"
        driver.find_element_by_id("selectTypeForm:j_idt119_0").click()
        driver.find_element_by_id("selectTypeForm:j_idt122").click()
        time.sleep(2)

        driver.find_element_by_id("headerForm:j_idt74").click()
        driver.find_element_by_id("offeringForm:j_idt17:1:j_idt25").click()
        driver.find_element_by_id("cartForm:j_idt115").click()

        #счет на оплату
        driver.find_element_by_id("orderForm:j_idt100").click()
        time.sleep(3)
        file = glob('C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\downloads_pdf\\*.pdf')
        namefile=str(file)[2:-2]
        f=open(namefile,'r')
        f.close()
        os.remove(namefile)

        #visa
        order1 = driver.find_element_by_xpath("//span[@style = 'font-size:large;margin-right:32px']").text
        order1 = order1.partition('№ ')[2]
        print(order1)
        driver.find_element_by_id("orderForm:j_idt107").click()
        driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/span").click()
        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element_by_xpath("//input[@name='card-number']")
        )
        inputCC.send_keys("5555555555554477")

        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element_by_xpath("//input[@name='expiry-month']")
        )
        inputCC.send_keys("09")

        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element_by_xpath("//input[@name='expiry-year']")
        )
        inputCC.send_keys("30")

        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element_by_xpath("//input[@name='security-code']")
        )
        inputCC.send_keys("123" + Keys.ENTER)

        time.sleep(3)

        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element_by_xpath("//input[@id='cvc']")
        )
        inputCC.send_keys("123")
        driver.find_element_by_id("submitcvc").click()
        time.sleep(4)

        driver.find_element_by_xpath("//span[@class='button__text']").click()
        assert driver.find_element_by_xpath("//span[@class='ui-messages-info-summary']").text=="Заказ оплачен"

        #оплата наличными
        driver.find_element_by_id("topbarForm:cartCount").click()
        driver.find_element_by_id("headerForm:j_idt74").click()
        driver.find_element_by_id("offeringForm:j_idt17:0:j_idt25").click()
        driver.find_element_by_id("cartForm:j_idt103:1:j_idt104").click()
        time.sleep(2)
        driver.find_element_by_id("cartForm:j_idt115").click()
        driver.find_element_by_id("orderForm:j_idt114").click()
        assert driver.find_element_by_xpath("//span[@class='ui-messages-info-summary']").text == "Выбран способ оплаты по наличному расчету"

        #со счета
        order2 = driver.find_element_by_xpath("//span[@style = 'font-size:large;margin-right:32px']").text
        order2 = order2.partition('№ ')[2]
        print(order2)
        driver.find_element_by_id("orderForm:j_idt121").click()
        time.sleep(3)
        assert driver.find_element_by_xpath(
            "//span[@class='ui-messages-info-summary']").text == "Заказ оплачен"


        #Биллинг
        driver.find_element_by_css_selector(
            "#j_idt67 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(8) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Заказы\"] > span").click()
        driver.find_element_by_id("tableForm:main-table:j_id3").click()
        time.sleep(2)
        print(driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").text)
        print(driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(1) + "]").text)
        assert driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").text == order1
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(8) + "]").text == "Тульпова Марина"
        assert driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(1) + "]").text == order2
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(8) + "]").text == name3
        #удаление заказов и клиентов
        driver.find_element_by_id("tableForm:main-table:0:j_idt82").click()
        driver.find_element_by_id("j_idt104:j_idt105").click()
        time.sleep(2)
        driver.find_element_by_id("tableForm:main-table:0:j_idt82").click()
        driver.find_element_by_id("j_idt104:j_idt105").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#j_idt67 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Реестр клиентов\"] > span").click()
        driver.find_element_by_id("tableForm:table:0:j_idt90").click()
        driver.find_element_by_id("j_idt901:j_idt902").click()
        time.sleep(2)
        driver.find_element_by_id("tableForm:table:0:j_idt90").click()
        driver.find_element_by_id("j_idt901:j_idt902").click()
        time.sleep(2)
        driver.find_element_by_id("tableForm:table:0:j_idt90").click()
        driver.find_element_by_id("j_idt901:j_idt902").click()
        time.sleep(2)






