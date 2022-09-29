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


class Cart(unittest.TestCase):

    def setUp(self):
        download_dir = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\reestr\\downloads_pdf"
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

    def test_create_cart(self):
        driver = self.driver
        driver.get("http://auraep.ru:8180/business/dashboard/dashboard.xhtml")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("tuilp")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("tuilp")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()

        driver.find_element(By.CSS_SELECTOR,
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Реестр клиентов\"] > span").click()
        driver.find_element(By.ID,"tableForm:j_idt74").click()
        #создание контакта
        driver.find_element(By.ID,"selectTypeForm:j_idt95").click()
        lastname = self.generate_random_string()
        driver.find_element(By.ID,"personForm:j_idt100:lastName").click()
        driver.find_element(By.ID,"personForm:j_idt100:lastName").clear()
        driver.find_element(By.ID,"personForm:j_idt100:lastName").send_keys(lastname)
        firstname = self.generate_random_string()
        driver.find_element(By.ID,"personForm:j_idt100:firstName").click()
        driver.find_element(By.ID,"personForm:j_idt100:firstName").clear()
        driver.find_element(By.ID,"personForm:j_idt100:firstName").send_keys(firstname)
        patronymicname = self.generate_random_string()
        driver.find_element(By.ID,"personForm:j_idt100:patronymicName").click()
        driver.find_element(By.ID,"personForm:j_idt100:patronymicName").clear()
        driver.find_element(By.ID,"personForm:j_idt100:patronymicName").send_keys(patronymicname)
        name = lastname+firstname+patronymicname
        driver.find_element(By.ID,"personForm:j_idt100:birthDate_input").click()
        driver.find_element(By.ID,"personForm:j_idt100:birthDate_input").clear()
        for date in "08911111":
            driver.find_element(By.ID,"personForm:j_idt100:birthDate_input").send_keys(Keys.HOME, date)
        driver.find_element(By.ID,"personForm:j_idt100:email").click()
        driver.find_element(By.ID,"personForm:j_idt100:email").clear()
        driver.find_element(By.ID,"personForm:j_idt100:email").send_keys("shamkin@proweb.ru")
        driver.find_element(By.CSS_SELECTOR,
            "#personForm\:j_idt100\:sex > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.ID,"personForm:j_idt100:snils").click()
        driver.find_element(By.ID,"personForm:j_idt100:snils").clear()
        driver.find_element(By.ID,"personForm:j_idt100:snils").send_keys("78945212311")
        driver.find_element(By.CSS_SELECTOR,"#personForm\:j_idt100\:userCategory_label").click()
        driver.find_element(By.CSS_SELECTOR,"#personForm\:j_idt100\:userCategory_items").click()
        driver.find_element(By.ID,"personForm:j_idt100:userCategory_2").click()
        time.sleep(2)

        driver.find_element(By.ID,"personForm:j_idt100:contactTable:j_idt135").click()
        driver.find_element(By.CSS_SELECTOR,"#personContactForm\:contactType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#personContactForm\:contactType_items").click()
        driver.find_element(By.ID,"personContactForm:contactType_1").click()
        time.sleep(2)
        driver.find_element(By.ID,"personContactForm:contactInfo").click()
        driver.find_element(By.ID,"personContactForm:contactInfo").clear()
        driver.find_element(By.ID,"personContactForm:contactInfo").send_keys("1")
        driver.find_element(By.ID,"personContactForm:comments").click()
        driver.find_element(By.ID,"personContactForm:comments").clear()
        driver.find_element(By.ID,"personContactForm:comments").send_keys("1")
        driver.find_element(By.ID,"personContactForm:j_idt274").click()
        time.sleep(2)
        driver.find_element(By.ID,"personForm:j_idt100:identityTable:j_idt183").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#personIdentityForm\:type_label").click()
        driver.find_element(By.CSS_SELECTOR,"#personIdentityForm\:type_items").click()
        driver.find_element(By.ID,"personIdentityForm:type_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"personIdentityForm:series").click()
        driver.find_element(By.ID,"personIdentityForm:series").clear()
        driver.find_element(By.ID,"personIdentityForm:series").send_keys("44444")
        driver.find_element(By.ID,"personIdentityForm:number").click()
        driver.find_element(By.ID,"personIdentityForm:number").clear()
        driver.find_element(By.ID,"personIdentityForm:number").send_keys("444444")
        driver.find_element(By.ID,"personIdentityForm:issuedBy").click()
        driver.find_element(By.ID,"personIdentityForm:issuedBy").clear()
        driver.find_element(By.ID,"personIdentityForm:issuedBy").send_keys("ТП УФМС Адмиралтейский")
        driver.find_element(By.ID,"personIdentityForm:issuedDate_input").click()
        driver.find_element(By.ID,"personIdentityForm:issuedDate_input").clear()
        for date in "01021111":
            driver.find_element(By.ID,"personIdentityForm:issuedDate_input").send_keys(Keys.HOME, date)
        driver.find_element(By.CSS_SELECTOR,"body").click()
        driver.find_element(By.ID,"personIdentityForm:issuedCode").click()
        driver.find_element(By.ID,"personIdentityForm:issuedCode").clear()
        driver.find_element(By.ID,"personIdentityForm:issuedCode").send_keys("12345")
        driver.find_element(By.ID,"personIdentityForm:validity_input").click()
        driver.find_element(By.ID,"personIdentityForm:validity_input").clear()
        for date in "05021111":
            driver.find_element(By.ID,"personIdentityForm:validity_input").send_keys(Keys.HOME, date)
        driver.find_element(By.CSS_SELECTOR,"body").click()
        driver.find_element(By.ID,"personIdentityForm:j_idt326").click()
        driver.find_element(By.ID,"personForm:j_idt261").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableForm:table:j_idt77").click()
        driver.find_element(By.ID,"tableForm:table:j_idt77").click()
        time.sleep(3)
        name2=driver.find_element(By.XPATH,"//tbody[@id='tableForm:table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text
        assert (re.match(r'(?i)' + re.sub(r'\s', '', name) + r'$', re.sub(r'\s', '', name2)))

        #создание ЮЛ
        driver.find_element(By.ID,"tableForm:j_idt74").click()
        driver.find_element(By.CSS_SELECTOR,"#selectTypeForm\:j_idt93_label").click()
        driver.find_element(By.CSS_SELECTOR,"#selectTypeForm\:j_idt93_items").click()
        driver.find_element(By.ID,"selectTypeForm:j_idt93_1").click()
        time.sleep(2)
        driver.find_element(By.ID,"selectTypeForm:j_idt95").click()
        name = self.generate_random_string()
        driver.find_element(By.ID,"legalForm:j_idt331:name").click()
        driver.find_element(By.ID,"legalForm:j_idt331:name").clear()
        driver.find_element(By.ID,"legalForm:j_idt331:name").send_keys(name)
        driver.find_element(By.CSS_SELECTOR,"#legalForm\:j_idt331\:categories").click()
        driver.find_element(By.CSS_SELECTOR,
            "#legalForm\:j_idt331\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#legalForm\:j_idt331\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        #driver.find_element(By.ID,"legalForm:j_idt332:j_idt334").click()

        driver.find_element(By.ID,"legalForm:j_idt331:shortName").click()
        driver.find_element(By.ID,"legalForm:j_idt331:shortName").clear()
        driver.find_element(By.ID,"legalForm:j_idt331:shortName").send_keys(u"СаблинАнтител")
        driver.find_element(By.ID,"legalForm:j_idt331:seoName").click()
        driver.find_element(By.ID,"legalForm:j_idt331:seoName").clear()
        driver.find_element(By.ID,"legalForm:j_idt331:seoName").send_keys(u"Евгеньевич")
        driver.find_element(By.ID,"legalForm:j_idt331:email").click()
        driver.find_element(By.ID,"legalForm:j_idt331:email").clear()
        driver.find_element(By.ID,"legalForm:j_idt331:email").send_keys("shamkin@proweb.ru")
        driver.find_element(By.CSS_SELECTOR,"#legalForm\:j_idt331\:userCategory_label").click()
        driver.find_element(By.CSS_SELECTOR,"#legalForm\:j_idt331\:userCategory_items").click()
        driver.find_element(By.ID,"legalForm:j_idt331:userCategory_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"legalForm:j_idt331:contactTable:j_idt360").click()
        driver.find_element(By.CSS_SELECTOR,"#legalContactForm\:contactType_label").click()
        driver.find_element(By.CSS_SELECTOR,"#legalContactForm\:contactType_items").click()
        driver.find_element(By.ID,"legalContactForm:contactType_1").click()
        time.sleep(2)
        driver.find_element(By.ID,"legalContactForm:contactInfo").click()
        driver.find_element(By.ID,"legalContactForm:contactInfo").clear()
        driver.find_element(By.ID,"legalContactForm:contactInfo").send_keys("1")
        driver.find_element(By.ID,"legalContactForm:comments").click()
        driver.find_element(By.ID,"legalContactForm:comments").clear()
        driver.find_element(By.ID,"legalContactForm:comments").send_keys("1")
        driver.find_element(By.ID,"legalContactForm:j_idt533").click()
        time.sleep(2)
        driver.find_element(By.ID,"legalForm:j_idt331:addressTable:j_idt386").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#legalAddressForm\:type_label").click()
        driver.find_element(By.CSS_SELECTOR,"#legalAddressForm\:type_items").click()
        driver.find_element(By.ID,"legalAddressForm:type_0").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#legalAddressForm\:country_label").click()
        driver.find_element(By.CSS_SELECTOR,"#legalAddressForm\:country_items").click()
        driver.find_element(By.ID,"legalAddressForm:country_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"legalAddressForm:city_input").click()
        driver.find_element(By.ID,"legalAddressForm:city_input").clear()
        driver.find_element(By.ID,"legalAddressForm:city_input").send_keys("Санкт")
        driver.find_element(By.XPATH,"//span[@id='legalAddressForm:city_panel']/ul/li/span").click()
        driver.find_element(By.CSS_SELECTOR,"#legalAddressForm\:cityArea_label").click()
        driver.find_element(By.CSS_SELECTOR,"#legalAddressForm\:cityArea_items").click()
        driver.find_element(By.ID,"legalAddressForm:cityArea_1").click()
        time.sleep(2)
        driver.find_element(By.ID,"legalAddressForm:street_input").click()
        driver.find_element(By.ID,"legalAddressForm:street_input").clear()
        driver.find_element(By.ID,"legalAddressForm:street_input").send_keys("Лесная")
        driver.find_element(By.ID,"legalAddressForm:house_input").click()
        driver.find_element(By.ID,"legalAddressForm:house_input").clear()
        driver.find_element(By.ID,"legalAddressForm:house_input").send_keys("5")
        driver.find_element(By.ID,"legalAddressForm:flat").click()
        driver.find_element(By.ID,"legalAddressForm:flat").clear()
        driver.find_element(By.ID,"legalAddressForm:flat").send_keys("5")
        driver.find_element(By.CSS_SELECTOR,"body").click()
        driver.find_element(By.ID,"legalAddressForm:comment").click()
        driver.find_element(By.ID,"legalAddressForm:comment").clear()
        driver.find_element(By.ID,"legalAddressForm:comment").send_keys("Примечание")
        driver.find_element(By.ID,"legalAddressForm:j_idt564").click()
        time.sleep(2)
        driver.find_element(By.ID,"legalForm:j_idt520").click()
        time.sleep(2)
        name3 = driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text
        assert (re.match(r'(?i)' + re.sub(r'\s', '', name) + r'$', re.sub(r'\s', '', name3)))

        #создание ИП
        driver.find_element(By.ID,"tableForm:j_idt74").click()
        driver.find_element(By.CSS_SELECTOR,"#selectTypeForm\:j_idt93_label").click()
        driver.find_element(By.CSS_SELECTOR,"#selectTypeForm\:j_idt93_items").click()
        driver.find_element(By.ID,"selectTypeForm:j_idt93_2").click()
        time.sleep(2)
        driver.find_element(By.ID,"selectTypeForm:j_idt95").click()
        name = self.generate_random_string()
        driver.find_element(By.ID,"singleForm:j_idt611:name").click()
        driver.find_element(By.ID,"singleForm:j_idt611:name").clear()
        driver.find_element(By.ID,"singleForm:j_idt611:name").send_keys(name)
        driver.find_element(By.CSS_SELECTOR,"#singleForm\:j_idt611\:categories").click()
        driver.find_element(By.CSS_SELECTOR,
            "#singleForm\:j_idt611\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#singleForm\:j_idt611\:categories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        #driver.find_element(By.ID,"legalForm:j_idt332:j_idt334").click()

        driver.find_element(By.ID,"singleForm:j_idt611:shortName").click()
        driver.find_element(By.ID,"singleForm:j_idt611:shortName").clear()
        driver.find_element(By.ID,"singleForm:j_idt611:shortName").send_keys(u"СаблинПАСС")
        driver.find_element(By.ID,"singleForm:j_idt611:email").click()
        driver.find_element(By.ID,"singleForm:j_idt611:email").clear()
        driver.find_element(By.ID,"singleForm:j_idt611:email").send_keys("shamkin@proweb.ru")
        driver.find_element(By.CSS_SELECTOR,"#singleForm\:j_idt611\:userCategory_label").click()
        driver.find_element(By.CSS_SELECTOR,"#singleForm\:j_idt611\:userCategory_items").click()
        driver.find_element(By.ID,"singleForm:j_idt611:userCategory_2").click()
        time.sleep(2)

        driver.find_element(By.ID,"singleForm:j_idt791").click()
        time.sleep(2)
        name4 = driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text
        assert (re.match(r'(?i)' + re.sub(r'\s', '', name) + r'$', re.sub(r'\s', '', name4)))

        #корзина
        driver.find_element(By.ID,"topbarForm:cartCount").click()
        assert driver.find_element(By.XPATH,"//a[@id='cartForm:j_idt95']//span[@style='color:#333333']").text == "Тульпова Марина"
        assert driver.find_element(By.XPATH,"//a[@id='cartForm:j_idt101:0:j_idt102']//span[@style='color:#333333']").text or driver.find_element(By.XPATH,"//a[@id='cartForm:j_idt101:1:j_idt102']//span[@style='color:#333333']").text or driver.find_element(By.XPATH,"//a[@id='cartForm:j_idt101:2:j_idt102']//span[@style='color:#333333']").text== name3
        assert driver.find_element(By.XPATH,"//a[@id='cartForm:j_idt101:0:j_idt102']//span[@style='color:#333333']").text or driver.find_element(By.XPATH,"//a[@id='cartForm:j_idt101:1:j_idt102']//span[@style='color:#333333']").text or driver.find_element(By.XPATH,"//a[@id='cartForm:j_idt101:2:j_idt102']//span[@style='color:#333333']").text == name4
        '''
        driver.find_element(By.ID,"cartForm:j_idt105").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,"#selectTypeForm\:j_idt117_label").click()
        driver.find_element(By.CSS_SELECTOR,"#selectTypeForm\:j_idt117_items").click()
        time.sleep(2)
        assert driver.find_element(By.ID,"selectTypeForm:j_idt117_0").text == "Юридическое лицо"
        assert driver.find_element(By.ID,"selectTypeForm:j_idt117_1").text == "Индивидуальный предприниматель"
        driver.find_element(By.ID,"selectTypeForm:j_idt117_0").click()
        driver.find_element(By.ID,"selectTypeForm:j_idt120").click()
        time.sleep(2)
        '''
        driver.find_element(By.ID,"headerForm:j_idt72").click()
        driver.find_element(By.ID,"offeringForm:j_idt17:1:j_idt25").click()
        driver.find_element(By.ID,"cartForm:j_idt113").click()
        '''
        #счет на оплату
        driver.find_element(By.ID,"orderForm:j_idt97").click()
        time.sleep(4)
        file = glob('C:\\Users\\user\\PycharmProjects\\TestsCovid1\\AURA\\reestr\\downloads_pdf\\*.pdf')
        time.sleep(4)
        namefile=str(file)[2:-2]
        f=open(namefile,'r')
        f.close()
        os.remove(namefile)
        '''
        #visa
        order1 = driver.find_element(By.XPATH,"//span[@style = 'font-size:large;margin-right:32px']").text
        order1 = order1.partition('№ ')[2]
        #print(order1)
        driver.find_element(By.XPATH,"//button[@id='orderForm:j_idt105']").click()
        driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/span").click()
        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(By.XPATH,"//input[@name='card-number']")
        )
        inputCC.send_keys("5555555555554477")

        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(By.XPATH,"//input[@name='expiry-month']")
        )
        inputCC.send_keys("09")

        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(By.XPATH,"//input[@name='expiry-year']")
        )
        inputCC.send_keys("30")

        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(By.XPATH,"//input[@name='security-code']")
        )
        inputCC.send_keys("123" + Keys.ENTER)

        time.sleep(3)

        inputCC = WebDriverWait(driver, 15).until(
            lambda driver: driver.find_element(By.XPATH,"//input[@id='cvc']")
        )
        inputCC.send_keys("123")
        driver.find_element(By.ID,"submitcvc").click()
        time.sleep(4)

        driver.find_element(By.XPATH,"//span[@class='button__text']").click()
        assert driver.find_element(By.XPATH,"//span[@class='ui-messages-info-summary']").text=="Заказ оплачен"
        
        #оплата наличными
        driver.find_element(By.ID,"topbarForm:cartCount").click()
        driver.find_element(By.ID,"headerForm:j_idt72").click()
        driver.find_element(By.ID,"offeringForm:j_idt17:0:j_idt25").click()
        if driver.find_element(By.XPATH,
            "//a[@id='cartForm:j_idt101:0:j_idt102']//span[@style='color:#333333']").text == "ООО тульпова": driver.find_element(By.XPATH,
            "//a[@id='cartForm:j_idt101:0:j_idt102']//span[@style='color:#333333']").click()
        if driver.find_element(By.XPATH,
            "//a[@id='cartForm:j_idt101:1:j_idt102']//span[@style='color:#333333']").text == "ООО тульпова": driver.find_element(By.XPATH,
            "//a[@id='cartForm:j_idt101:1:j_idt102']//span[@style='color:#333333']").click()
        if driver.find_element(By.XPATH,
            "//a[@id='cartForm:j_idt101:2:j_idt102']//span[@style='color:#333333']").text == "ООО тульпова": driver.find_element(By.XPATH,
            "//a[@id='cartForm:j_idt101:2:j_idt102']//span[@style='color:#333333']").click()

        #driver.find_element(By.ID,"cartForm:j_idt103:0:j_idt104").click()
        time.sleep(2)
        driver.find_element(By.ID,"cartForm:j_idt113").click()
        driver.find_element(By.ID,"orderForm:j_idt111").click()
        assert driver.find_element(By.XPATH,"//span[@class='ui-messages-info-summary']").text == "Выбран способ оплаты по наличному расчету"

        #со счета
        order2 = driver.find_element(By.XPATH,"//span[@style = 'font-size:large;margin-right:32px']").text
        order2 = order2.partition('№ ')[2]
        #print(order2)
        driver.find_element(By.ID,"orderForm:j_idt119").click()
        time.sleep(3)
        assert driver.find_element(By.XPATH,
            "//span[@class='ui-messages-info-summary']").text == "Заказ оплачен"

        #Биллинг
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(8) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Заказы\"] > span").click()
        driver.find_element(By.ID,"tableForm:main-table:j_id3").click()
        time.sleep(2)
        #print(driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").text)
        #print(driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(1) + "]").text)
        assert driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").text == order1
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(8) + "]").text == "Тульпова Марина"
        assert driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(1) + "]").text == order2
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(8) + "]").text == "ООО тульпова"
        #удаление заказов и клиентов
        driver.find_element(By.ID,"tableForm:main-table:0:j_idt80").click()
        driver.find_element(By.ID,"j_idt102:j_idt103").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableForm:main-table:0:j_idt80").click()
        driver.find_element(By.ID,"j_idt102:j_idt103").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Реестр клиентов\"] > span").click()
        driver.find_element(By.ID,"tableForm:table:0:j_idt89").click()
        driver.find_element(By.ID,"j_idt900:j_idt901").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableForm:table:0:j_idt89").click()
        driver.find_element(By.ID,"j_idt900:j_idt901").click()
        time.sleep(2)
        driver.find_element(By.ID,"tableForm:table:0:j_idt89").click()
        driver.find_element(By.ID,"j_idt900:j_idt901").click()
        time.sleep(2)






