# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os


class CreateAntitellGg(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome("C:/Users/user/Downloads/chromedriver.exe")
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
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Create_PCR.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.create_pcr()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    

    def test_create_pcr(self):
        self.genlog()
    '''

    def test_create_antitel_lGg(self):
        driver = self.driver
        # driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml")
        # driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt66 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Поиск исследований\"] > span").click()
        #по виду исследования
        driver.find_element_by_id("filtersForm:j_idt80_input").click()
        driver.find_element_by_id("filtersForm:j_idt80_input").clear()
        for date in "00:00 1202.80.71":
            driver.find_element_by_id("filtersForm:j_idt80_input").send_keys(Keys.HOME, date)

        driver.find_element_by_id("filtersForm:j_idt83_input").click()
        driver.find_element_by_id("filtersForm:j_idt83_input").clear()
        for date in "00:00 1202.80.81":
            driver.find_element_by_id("filtersForm:j_idt83_input").send_keys(Keys.HOME, date)

        driver.find_element_by_id("filtersForm:j_idt86").click()
        driver.find_element_by_id("filtersForm:j_idt86_label").click()
        driver.find_element_by_id("filtersForm:j_idt86_1").click()

        driver.find_element_by_id("filtersForm:j_idt91").click()
        driver.find_element_by_id("filtersForm:j_idt91_label").click()
        driver.find_element_by_id("filtersForm:j_idt91_3").click()

        driver.find_element_by_id("filtersForm:j_idt96").click()
        driver.find_element_by_id("filtersForm:j_idt96_label").click()
        driver.find_element_by_id("filtersForm:j_idt96_5").click()

        driver.find_element_by_id("filtersForm:j_idt187").click()
        time.sleep(2)
        assert driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text=="821Ч960"
        #по номеру исследования
        driver.find_element_by_id("filtersForm:j_idt96").click()
        driver.find_element_by_id("filtersForm:j_idt96_label").click()
        driver.find_element_by_id("filtersForm:j_idt96_1").click()

        driver.find_element_by_id("filtersForm:j_idt101").click()
        driver.find_element_by_id("filtersForm:j_idt101").clear()
        driver.find_element_by_id("filtersForm:j_idt101").send_keys("821Ч958")

        driver.find_element_by_id("filtersForm:j_idt187").click()
        time.sleep(2)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "821Ч958"
        assert driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(4) + "]").text=="ТЕСТИМ"
        #по данным пациента
        driver.find_element_by_id("filtersForm:j_idt101").click()
        driver.find_element_by_id("filtersForm:j_idt101").clear()

        driver.find_element_by_id("filtersForm:j_idt119").click()
        driver.find_element_by_id("filtersForm:j_idt122").click()
        driver.find_element_by_id("filtersForm:j_idt122").clear()
        driver.find_element_by_id("filtersForm:j_idt122").send_keys("Автотестов")
        driver.find_element_by_id("filtersForm:j_idt125").click()
        driver.find_element_by_id("filtersForm:j_idt125").clear()
        driver.find_element_by_id("filtersForm:j_idt125").send_keys("Автотест")
        driver.find_element_by_id("filtersForm:j_idt128").click()
        driver.find_element_by_id("filtersForm:j_idt128").clear()
        driver.find_element_by_id("filtersForm:j_idt128").send_keys("Петрович")

        driver.find_element_by_id("filtersForm:j_idt131_input").click()
        driver.find_element_by_id("filtersForm:j_idt131_input").clear()
        for date in "58913020":
            driver.find_element_by_id("filtersForm:j_idt131_input").send_keys(Keys.HOME, date)

        driver.find_element_by_id("filtersForm:j_idt134").click()
        driver.find_element_by_id("filtersForm:j_idt134").clear()
        driver.find_element_by_id("filtersForm:j_idt134").send_keys("78967878678")
        driver.find_element_by_id("filtersForm:j_idt137").click()
        driver.find_element_by_id("filtersForm:j_idt137").clear()
        driver.find_element_by_id("filtersForm:j_idt137").send_keys("36")

        driver.find_element_by_id("filtersForm:region_label").click()
        driver.find_element_by_css_selector("#filtersForm\:region_items").click()
        time.sleep(2)
        driver.find_element_by_id("filtersForm:region_48").click()
        time.sleep(2)
        driver.find_element_by_id("filtersForm:j_idt187").click()
        time.sleep(2)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "821Ч959"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(4) + "]").text == "АВТОТЕСТОВ"
        #по направляющему учреждению
        driver.find_element_by_id("filtersForm:j_idt122").click()
        driver.find_element_by_id("filtersForm:j_idt122").clear()
        driver.find_element_by_id("filtersForm:j_idt125").click()
        driver.find_element_by_id("filtersForm:j_idt125").clear()
        driver.find_element_by_id("filtersForm:j_idt128").click()
        driver.find_element_by_id("filtersForm:j_idt128").clear()
        driver.find_element_by_id("filtersForm:j_idt131_input").click()
        driver.find_element_by_id("filtersForm:j_idt131_input").clear()
        driver.find_element_by_id("filtersForm:j_idt134").click()
        driver.find_element_by_id("filtersForm:j_idt134").clear()
        driver.find_element_by_id("filtersForm:j_idt137").click()
        driver.find_element_by_id("filtersForm:j_idt137").clear()
        driver.find_element_by_id("filtersForm:region_label").click()
        driver.find_element_by_css_selector("#filtersForm\:region_items").click()
        time.sleep(2)
        driver.find_element_by_id("filtersForm:region_0").click()
        time.sleep(2)

        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("filtersForm:j_idt156").click()
        time.sleep(2)
        driver.find_element_by_id("selectSendInstitutionsForm:j_idt231:j_idt233:filter").click()
        driver.find_element_by_id("selectSendInstitutionsForm:j_idt231:j_idt233:filter").clear()
        driver.find_element_by_id("selectSendInstitutionsForm:j_idt231:j_idt233:filter").send_keys("Хеликс")
        time.sleep(2)
        # driver.find_element_by_id("buildForm:j_idt89:j_idt96").click()
        driver.find_element_by_xpath("//td[contains(text(), '7802122535')]").click()
        driver.find_element_by_id("selectSendInstitutionsForm:j_idt243").click()
        time.sleep(2)

        driver.find_element_by_id("filtersForm:j_idt160").click()
        # driver.find_element_by_id("buildForm:j_idt79_label").click()
        driver.find_element_by_css_selector("#filtersForm\:j_idt160_panel").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt160_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt160_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(6) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body").click()

        driver.find_element_by_id("filtersForm:j_idt164").click()
        # driver.find_element_by_id("buildForm:j_idt79_label").click()
        driver.find_element_by_css_selector("#filtersForm\:j_idt164_panel").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt164_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body").click()

        driver.find_element_by_id("filtersForm:j_idt187").click()
        time.sleep(2)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "821Ч961"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(11) + "]").text == "ООО \"НПФ \"ХЕЛИКС\""
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(2) + "]").text == "821Ч963"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(10) + "]").text == "Самотек"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(3) + "]/td[" + str(2) + "]").text == "821Ч964"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(9) + "]").text == "Добровольцы"

        #по результату исследования
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt160 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li:nth-child(1) > span").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt160 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li > span").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt164 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li > span").click()
        driver.find_element_by_id("filtersForm:j_idt171_label").click()
        driver.find_element_by_css_selector("#filtersForm\:j_idt171_items").click()
        time.sleep(2)
        driver.find_element_by_id("filtersForm:j_idt171_7").click()
        time.sleep(2)
        driver.find_element_by_id("filtersForm:j_idt176_input").click()
        driver.find_element_by_id("filtersForm:j_idt176_input").clear()
        for date in "00:00 1202.80.71":
            driver.find_element_by_id("filtersForm:j_idt176_input").send_keys(Keys.HOME, date)
        driver.find_element_by_id("filtersForm:j_idt179_input").click()
        driver.find_element_by_id("filtersForm:j_idt179_input").clear()
        for date in "00:12 1202.80.71":
            driver.find_element_by_id("filtersForm:j_idt179_input").send_keys(Keys.HOME, date)

        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("filtersForm:j_idt183").click()
        time.sleep(2)
        driver.find_element_by_id("selectLabContractorForm:j_idt248:j_idt250:filter").click()
        driver.find_element_by_id("selectLabContractorForm:j_idt248:j_idt250:filter").clear()
        driver.find_element_by_id("selectLabContractorForm:j_idt248:j_idt250:filter").send_keys("Хеликс")
        time.sleep(2)
        # driver.find_element_by_id("buildForm:j_idt89:j_idt96").click()
        driver.find_element_by_xpath("//tbody[@id='selectLabContractorForm:j_idt248_data']//tr[" + str(2) + "]/td[" + str(2) + "]").click()
        driver.find_element_by_id("selectLabContractorForm:j_idt266").click()
        time.sleep(2)
        driver.find_element_by_id("filtersForm:j_idt187").click()
        time.sleep(2)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "821Ч959"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(13) + "]").text == "Брак"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(2) + "]").text == "821Ч961"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(3) + "]/td[" + str(2) + "]").text == "821Ч964"







