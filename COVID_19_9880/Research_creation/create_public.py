# -*- coding: utf-8 -*-
from contextlib import contextmanager
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
import unittest, time, re

import logging, os
import sys

from selenium.webdriver.support.wait import WebDriverWait


class CreatePublic(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
    '''
    def genlog(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        if not os.path.exists("Logs"):
            os.mkdir("Logs")
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Create_public.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.create_public()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')
        return logger

    def test_create_public(self):
        self.genlog()
    '''
    def test_create_public(self):

            driver = self.driver
            #driver.get("http://195.19.96.255:8981")
            driver.get("https://pub.rpn19.ru/forms/35")
            driver.refresh()
            driver.find_element(By.ID,"Familiya_").click()
            driver.find_element(By.ID,"Familiya_").clear()
            driver.find_element(By.ID,"Familiya_").send_keys(u"СаблинПабл")
            driver.find_element(By.ID,"Imya").click()
            driver.find_element(By.ID,"Imya").clear()
            driver.find_element(By.ID,"Imya").send_keys(u"Роман")
            driver.find_element(By.ID,"Otchestvo_Middle_name").click()
            driver.find_element(By.ID,"Otchestvo_Middle_name").clear()
            driver.find_element(By.ID,"Otchestvo_Middle_name").send_keys(u"Евгеньевич")
            driver.find_element(By.NAME,"Data_rozhdeniya").click()
            # driver.find_element(By.ID,"date-mask").clear()
            time.sleep(2)
            driver.find_element(By.NAME,"Data_rozhdeniya").send_keys("11")
            driver.find_element(By.NAME,"Data_rozhdeniya").send_keys("11")
            driver.find_element(By.NAME,"Data_rozhdeniya").send_keys("1980")
            driver.find_element(By.CSS_SELECTOR,"body").click()
            driver.find_element(By.ID,"0").click()
            driver.find_element(By.ID,"Email").click()
            driver.find_element(By.ID,"Email").clear()
            driver.find_element(By.ID,"Email").send_keys("2332@3221")
            driver.find_element(By.ID,"Telefon").click()
            driver.find_element(By.ID,"Telefon").clear()
            driver.find_element(By.ID,"Telefon").send_keys("89456321782")
            select = Select(driver.find_element(By.NAME,"Strana"))
            select.select_by_visible_text(u"Россия")
            select = Select(driver.find_element(By.NAME,"Region"))
            select.select_by_visible_text(u"Ярославская область")
            time.sleep(2)
            driver.find_element(By.ID,"city").send_keys(u"Ярославль" + Keys.TAB)
            time.sleep(2)
            driver.find_element(By.ID,"street").click()
            driver.find_element(By.ID,"street").clear()
            driver.find_element(By.ID,"street").send_keys(u"Мира" + Keys.TAB)
            driver.find_element(By.ID,"building").clear()
            driver.find_element(By.ID,"building").send_keys("1")
            driver.find_element(By.ID,"Kvartira").clear()
            driver.find_element(By.ID,"Kvartira").send_keys("1231")
            #driver.find_element(By.ID,"Naimenovanie_organizatsii_Company_name").click()
            #driver.find_element(By.ID,"Naimenovanie_organizatsii_Company_name").clear()
            driver.find_element(By.ID,"Naimenovanie_organizatsii_Company_name").send_keys(u"Институт")
            driver.find_element(By.ID,"Dolzhnost_Position").clear()
            driver.find_element(By.ID,"Dolzhnost_Position").send_keys(u"Студент")
            driver.find_element(By.ID,"Telefon_Phone_cellphone_number").clear()
            driver.find_element(By.ID,"Telefon_Phone_cellphone_number").send_keys("84965213647")
            select = Select(driver.find_element(By.NAME,"Strana_Country"))
            select.select_by_visible_text(u"Россия")
            time.sleep(2)
            select = Select(driver.find_element(By.NAME,"Region_Region"))
            select.select_by_visible_text(u"Ярославская область")
            time.sleep(2)
            driver.find_element(By.ID,"Gorod_City").send_keys(u"Ярославль" + Keys.TAB)
            driver.find_element(By.ID,"Ulitsa_Street").send_keys(u"Мира" + Keys.TAB)
            driver.find_element(By.ID,"Nomer_doma_House_number").clear()
            driver.find_element(By.ID,"Nomer_doma_House_number").send_keys("7")
            driver.find_element(By.ID,"Kvartira_Flat").clear()
            driver.find_element(By.ID,"Kvartira_Flat").send_keys("745")

            driver.find_element(By.NAME,"Seriya_Series").click()
            driver.find_element(By.NAME,"Seriya_Series").clear()
            driver.find_element(By.NAME,"Seriya_Series").send_keys("1111")
            #driver.find_element(By.NAME,"Nomer_Number").click()
            #driver.find_element(By.NAME,"Nomer_Number").clear()
            driver.find_element(By.NAME,"Nomer_Number").send_keys("123456789")
            driver.find_element(By.XPATH,"//input[@id='date-mask' and @name='Data_vyidachi_Date_of_issue']").send_keys("12.12.1999")
            driver.find_element(By.NAME,"Kem_vyidan_Issued_by").send_keys("УФМС Динозаврики")
            driver.find_element(By.NAME,"Kod_podrazdeleniya_Code").send_keys("123")

            driver.find_element(By.XPATH,"//input[@id='1' and @name='Direction']").click()
            driver.find_element(By.NAME,"Data_pribyitiya_v_RF_ubyitiya_iz_RF").clear()
            driver.find_element(By.NAME,"Data_pribyitiya_v_RF_ubyitiya_iz_RF").send_keys("11")
            driver.find_element(By.NAME,"Data_pribyitiya_v_RF_ubyitiya_iz_RF").send_keys("03")
            driver.find_element(By.NAME,"Data_pribyitiya_v_RF_ubyitiya_iz_RF").send_keys("2021")
            time.sleep(2)
            select = Select(driver.find_element(By.NAME,"Iz_kakoy_stranyi_pribyil_V_kakuyu_stranu_ubyivaet"))
            select.select_by_visible_text(u"Абхазия")
            time.sleep(2)
            driver.find_element(By.ID,"Nomer_reysa").clear()
            driver.find_element(By.ID,"Nomer_reysa").send_keys("7854пв")
            driver.find_element(By.ID,"flexCheckDefault").click()
            driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.CONTROL + Keys.END)
            driver.find_element(By.XPATH,"//input[@value='Отправить']").click()
            assert driver.find_element_by_tag_name("h3").get_attribute(
                "textContent") == u"Ваша заявка успешно создана!"
            time.sleep(5)


if __name__ == "__main__":
    unittest.main()
