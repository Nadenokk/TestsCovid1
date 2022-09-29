# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os


class SearchIssled(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
        self.driver.set_window_size(1024, 600)
        self.driver.maximize_window()
        self.driver.implicitly_wait(60)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_search_issled(self):
        driver = self.driver
        # driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        # driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt72 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(6) > a").click()
        driver.find_element(By.CSS_SELECTOR,u"a[title=\"Поиск исследований\"] > span").click()
        #по виду исследования
        driver.find_element(By.ID,"filtersForm:j_idt86_input").click()
        driver.find_element(By.ID,"filtersForm:j_idt86_input").clear()
        for date in "00:00 1202.80.71":
            driver.find_element(By.ID,"filtersForm:j_idt86_input").send_keys(Keys.HOME, date)

        driver.find_element(By.ID,"filtersForm:j_idt89_input").click()
        driver.find_element(By.ID,"filtersForm:j_idt89_input").clear()
        for date in "00:00 1202.80.81":
            driver.find_element(By.ID,"filtersForm:j_idt89_input").send_keys(Keys.HOME, date)

        driver.find_element(By.ID,"filtersForm:j_idt92").click()
        driver.find_element(By.ID,"filtersForm:j_idt92_label").click()
        driver.find_element(By.ID,"filtersForm:j_idt92_1").click()

        driver.find_element(By.ID,"filtersForm:j_idt97").click()
        driver.find_element(By.ID,"filtersForm:j_idt97_label").click()
        driver.find_element(By.ID,"filtersForm:j_idt97_3").click()

        driver.find_element(By.ID,"filtersForm:j_idt102").click()
        driver.find_element(By.ID,"filtersForm:j_idt102_label").click()
        driver.find_element(By.ID,"filtersForm:j_idt102_5").click()

        driver.find_element(By.ID,"filtersForm:j_idt202").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text=="821А23614183"
        #по номеру исследования
        driver.find_element(By.ID,"filtersForm:j_idt102").click()
        driver.find_element(By.ID,"filtersForm:j_idt102_label").click()
        driver.find_element(By.ID,"filtersForm:j_idt102_1").click()

        driver.find_element(By.ID,"filtersForm:j_idt107").click()
        driver.find_element(By.ID,"filtersForm:j_idt107").clear()
        driver.find_element(By.ID,"filtersForm:j_idt107").send_keys("8213621889")

        driver.find_element(By.ID,"filtersForm:j_idt202").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "8213621889"
        assert driver.find_element(By.XPATH,"//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(4) + "]").text=="Орлов"
        #по данным пациента
        driver.find_element(By.ID,"filtersForm:j_idt107").click()
        driver.find_element(By.ID,"filtersForm:j_idt107").clear()

        driver.find_element(By.ID,"filtersForm:j_idt133").click()
        driver.find_element(By.ID,"filtersForm:j_idt133").click()
        driver.find_element(By.ID,"filtersForm:j_idt133").clear()
        driver.find_element(By.ID,"filtersForm:j_idt133").send_keys("Объедков")
        driver.find_element(By.ID,"filtersForm:j_idt136").click()
        driver.find_element(By.ID,"filtersForm:j_idt136").clear()
        driver.find_element(By.ID,"filtersForm:j_idt136").send_keys("Петр")
        driver.find_element(By.ID,"filtersForm:j_idt139").click()
        driver.find_element(By.ID,"filtersForm:j_idt139").clear()
        driver.find_element(By.ID,"filtersForm:j_idt139").send_keys("Владимирович")

        driver.find_element(By.ID,"filtersForm:j_idt142_input").click()
        driver.find_element(By.ID,"filtersForm:j_idt142_input").clear()
        for date in "08910171":
            driver.find_element(By.ID,"filtersForm:j_idt142_input").send_keys(Keys.HOME, date)

        driver.find_element(By.ID,"filtersForm:j_idt145").click()
        driver.find_element(By.ID,"filtersForm:j_idt145").clear()
        driver.find_element(By.ID,"filtersForm:j_idt145").send_keys("78967878678")
        driver.find_element(By.ID,"filtersForm:j_idt148").click()
        driver.find_element(By.ID,"filtersForm:j_idt148").clear()
        driver.find_element(By.ID,"filtersForm:j_idt148").send_keys("40")

        driver.find_element(By.ID,"filtersForm:region_label").click()
        driver.find_element(By.CSS_SELECTOR,"#filtersForm\:region_items").click()
        driver.find_element(By.CSS_SELECTOR,"#filtersForm\:region_items > li:nth-child(49)").click()

        time.sleep(2)
        driver.find_element(By.ID,"filtersForm:j_idt202").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "821А23601873"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(4) + "]").text == "Объедков"
        #по направляющему учреждению
        driver.find_element(By.ID,"filtersForm:j_idt86_input").click()
        driver.find_element(By.ID,"filtersForm:j_idt86_input").clear()
        driver.find_element(By.ID,"filtersForm:j_idt89_input").click()
        driver.find_element(By.ID,"filtersForm:j_idt89_input").clear()
        driver.find_element(By.ID,"filtersForm:j_idt92").click()
        driver.find_element(By.ID,"filtersForm:j_idt92_label").click()
        driver.find_element(By.ID,"filtersForm:j_idt92_0").click()
        driver.find_element(By.ID,"filtersForm:j_idt133").click()
        driver.find_element(By.ID,"filtersForm:j_idt133").clear()
        driver.find_element(By.ID,"filtersForm:j_idt136").click()
        driver.find_element(By.ID,"filtersForm:j_idt136").clear()
        driver.find_element(By.ID,"filtersForm:j_idt139").click()
        driver.find_element(By.ID,"filtersForm:j_idt139").clear()
        driver.find_element(By.ID,"filtersForm:j_idt142_input").click()
        driver.find_element(By.ID,"filtersForm:j_idt142_input").clear()
        driver.find_element(By.ID,"filtersForm:j_idt145").click()
        driver.find_element(By.ID,"filtersForm:j_idt145").clear()
        driver.find_element(By.ID,"filtersForm:j_idt148").click()
        driver.find_element(By.ID,"filtersForm:j_idt148").clear()
        driver.find_element(By.ID,"filtersForm:region_label").click()
        #driver.find_element(By.CSS_SELECTOR,"#filtersForm\:region_items").click()
        #time.sleep(2)
        driver.find_element(By.ID,"filtersForm:region_0").click()
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR,"body").click()
        driver.find_element(By.ID,"filtersForm:j_idt167").click()
        time.sleep(2)
        driver.find_element(By.ID,"selectSendInstitutionsForm:j_idt246:j_idt248:filter").click()
        driver.find_element(By.ID,"selectSendInstitutionsForm:j_idt246:j_idt248:filter").clear()
        driver.find_element(By.ID,"selectSendInstitutionsForm:j_idt246:j_idt248:filter").send_keys("Хеликс" + Keys.ENTER)
        time.sleep(2)
        driver.find_element(By.XPATH,"//td[contains(text(), '7802122535')]").click()
        driver.find_element(By.ID,"selectSendInstitutionsForm:j_idt258").click()
        time.sleep(2)

        driver.find_element(By.ID,"filtersForm:j_idt170").click()
        driver.find_element(By.CSS_SELECTOR,"#filtersForm\:j_idt170_panel").click()
        driver.find_element(By.CSS_SELECTOR,
            "#filtersForm\:j_idt170_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,"body").click()

        driver.find_element(By.CSS_SELECTOR,"#filtersForm\:j_idt170_panel").click()
        driver.find_element(By.CSS_SELECTOR,
            "#filtersForm\:j_idt170_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(6) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,"body").click()

        driver.find_element(By.ID,"filtersForm:j_idt174").click()
        driver.find_element(By.CSS_SELECTOR,"#filtersForm\:j_idt174_panel").click()
        driver.find_element(By.CSS_SELECTOR,
            "#filtersForm\:j_idt174_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element(By.CSS_SELECTOR,"body").click()

        driver.find_element(By.ID,"filtersForm:j_idt202").click()
        time.sleep(20)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "1Ц189782"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(11) + "]").text == "ООО \"НПФ \"ХЕЛИКС\""
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(2) + "]").text == "1Ц202636"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(10) + "]").text == "4, Центральный"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(3) + "]/td[" + str(2) + "]").text == "1Ц318971"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(9) + "]").text == "Добровольцы"
        '''
        #по результату исследования
        driver.find_element(By.CSS_SELECTOR,
            "#filtersForm\:j_idt170 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li:nth-child(1) > span").click()
        time.sleep(2)
        driver.find_element(By.CSS_SELECTOR,
            "#filtersForm\:j_idt170 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li > span").click()
        driver.find_element(By.CSS_SELECTOR,
            "#filtersForm\:j_idt174 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li > span").click()
        driver.find_element(By.ID,"filtersForm:j_idt181_label").click()
        driver.find_element(By.CSS_SELECTOR,"#filtersForm\:j_idt181_items").click()
        driver.find_element(By.ID,"filtersForm:j_idt181_7").click()
        time.sleep(2)
        driver.find_element(By.ID,"filtersForm:j_idt186_input").click()
        driver.find_element(By.ID,"filtersForm:j_idt186_input").clear()
        for date in "00:00 1202.90.10":
            driver.find_element(By.ID,"filtersForm:j_idt186_input").send_keys(Keys.HOME, date)
        driver.find_element(By.ID,"filtersForm:j_idt189_input").click()
        driver.find_element(By.ID,"filtersForm:j_idt189_input").clear()
        for date in "00:21 1202.90.10":
            driver.find_element(By.ID,"filtersForm:j_idt189_input").send_keys(Keys.HOME, date)
        #driver.find_element(By.CSS_SELECTOR,"body").click()
        driver.find_element(By.ID,"filtersForm:j_idt193").click()
        time.sleep(2)
        driver.find_element(By.ID,"selectLabContractorForm:j_idt258:j_idt260:filter").click()
        driver.find_element(By.ID,"selectLabContractorForm:j_idt258:j_idt260:filter").clear()
        driver.find_element(By.ID,"selectLabContractorForm:j_idt258:j_idt260:filter").send_keys("Хеликс")
        time.sleep(2)
        driver.find_element(By.XPATH,"//tbody[@id='selectLabContractorForm:j_idt258_data']//tr[" + str(3) + "]/td[" + str(2) + "]").click()
        driver.find_element(By.ID,"selectLabContractorForm:j_idt276").click()
        time.sleep(2)
        driver.find_element(By.ID,"filtersForm:j_idt197").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "821Ч4089977"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(13) + "]").text == "Брак"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(2) + "]").text == "821Ч4090034"
        assert driver.find_element(By.XPATH,
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(3) + "]/td[" + str(2) + "]").text == "821Ч4090173"
        '''







