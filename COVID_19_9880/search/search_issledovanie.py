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


    def test_search_issled(self):
        driver = self.driver
        # driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://rpn19.ru:9880/business/dashboard/dashboard.xhtml")
        # driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("borisova")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt66 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Поиск исследований\"] > span").click()
        #по виду исследования
        driver.find_element_by_id("filtersForm:j_idt79_input").click()
        driver.find_element_by_id("filtersForm:j_idt79_input").clear()
        for date in "00:00 1202.80.71":
            driver.find_element_by_id("filtersForm:j_idt79_input").send_keys(Keys.HOME, date)

        driver.find_element_by_id("filtersForm:j_idt82_input").click()
        driver.find_element_by_id("filtersForm:j_idt82_input").clear()
        for date in "00:00 1202.80.81":
            driver.find_element_by_id("filtersForm:j_idt82_input").send_keys(Keys.HOME, date)

        driver.find_element_by_id("filtersForm:j_idt85").click()
        driver.find_element_by_id("filtersForm:j_idt85_label").click()
        driver.find_element_by_id("filtersForm:j_idt85_1").click()

        driver.find_element_by_id("filtersForm:j_idt90").click()
        driver.find_element_by_id("filtersForm:j_idt90_label").click()
        driver.find_element_by_id("filtersForm:j_idt90_3").click()

        driver.find_element_by_id("filtersForm:j_idt95").click()
        driver.find_element_by_id("filtersForm:j_idt95_label").click()
        driver.find_element_by_id("filtersForm:j_idt95_5").click()

        driver.find_element_by_id("filtersForm:j_idt191").click()
        time.sleep(2)
        assert driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text=="821А23614183"
        #по номеру исследования
        driver.find_element_by_id("filtersForm:j_idt95").click()
        driver.find_element_by_id("filtersForm:j_idt95_label").click()
        driver.find_element_by_id("filtersForm:j_idt95_1").click()

        driver.find_element_by_id("filtersForm:j_idt100").click()
        driver.find_element_by_id("filtersForm:j_idt100").clear()
        driver.find_element_by_id("filtersForm:j_idt100").send_keys("8213621889")

        driver.find_element_by_id("filtersForm:j_idt191").click()
        time.sleep(2)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "8213621889"
        assert driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(4) + "]").text=="Орлов"
        #по данным пациента
        driver.find_element_by_id("filtersForm:j_idt100").click()
        driver.find_element_by_id("filtersForm:j_idt100").clear()

        driver.find_element_by_id("filtersForm:j_idt123").click()
        driver.find_element_by_id("filtersForm:j_idt126").click()
        driver.find_element_by_id("filtersForm:j_idt126").clear()
        driver.find_element_by_id("filtersForm:j_idt126").send_keys("Объедков")
        driver.find_element_by_id("filtersForm:j_idt129").click()
        driver.find_element_by_id("filtersForm:j_idt129").clear()
        driver.find_element_by_id("filtersForm:j_idt129").send_keys("Петр")
        driver.find_element_by_id("filtersForm:j_idt132").click()
        driver.find_element_by_id("filtersForm:j_idt132").clear()
        driver.find_element_by_id("filtersForm:j_idt132").send_keys("Владимирович")

        driver.find_element_by_id("filtersForm:j_idt135_input").click()
        driver.find_element_by_id("filtersForm:j_idt135_input").clear()
        for date in "08910171":
            driver.find_element_by_id("filtersForm:j_idt135_input").send_keys(Keys.HOME, date)

        driver.find_element_by_id("filtersForm:j_idt138").click()
        driver.find_element_by_id("filtersForm:j_idt138").clear()
        driver.find_element_by_id("filtersForm:j_idt138").send_keys("78967878678")
        driver.find_element_by_id("filtersForm:j_idt141").click()
        driver.find_element_by_id("filtersForm:j_idt141").clear()
        driver.find_element_by_id("filtersForm:j_idt141").send_keys("40")

        driver.find_element_by_id("filtersForm:region_label").click()
        driver.find_element_by_css_selector("#filtersForm\:region_items").click()
        driver.find_element_by_css_selector("#filtersForm\:region_items > li:nth-child(49)").click()

        time.sleep(2)
        driver.find_element_by_id("filtersForm:j_idt191").click()
        time.sleep(2)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "821А23601873"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(4) + "]").text == "Объедков"
        #по направляющему учреждению
        driver.find_element_by_id("filtersForm:j_idt79_input").click()
        driver.find_element_by_id("filtersForm:j_idt79_input").clear()
        driver.find_element_by_id("filtersForm:j_idt82_input").click()
        driver.find_element_by_id("filtersForm:j_idt82_input").clear()
        driver.find_element_by_id("filtersForm:j_idt85").click()
        driver.find_element_by_id("filtersForm:j_idt85_label").click()
        driver.find_element_by_id("filtersForm:j_idt85_0").click()
        driver.find_element_by_id("filtersForm:j_idt126").click()
        driver.find_element_by_id("filtersForm:j_idt126").clear()
        driver.find_element_by_id("filtersForm:j_idt129").click()
        driver.find_element_by_id("filtersForm:j_idt129").clear()
        driver.find_element_by_id("filtersForm:j_idt132").click()
        driver.find_element_by_id("filtersForm:j_idt132").clear()
        driver.find_element_by_id("filtersForm:j_idt135_input").click()
        driver.find_element_by_id("filtersForm:j_idt135_input").clear()
        driver.find_element_by_id("filtersForm:j_idt138").click()
        driver.find_element_by_id("filtersForm:j_idt138").clear()
        driver.find_element_by_id("filtersForm:j_idt141").click()
        driver.find_element_by_id("filtersForm:j_idt141").clear()
        driver.find_element_by_id("filtersForm:region_label").click()
        #driver.find_element_by_css_selector("#filtersForm\:region_items").click()
        #time.sleep(2)
        driver.find_element_by_id("filtersForm:region_0").click()
        time.sleep(2)

        driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("filtersForm:j_idt160").click()
        time.sleep(2)
        driver.find_element_by_id("selectSendInstitutionsForm:j_idt235:j_idt237:filter").click()
        driver.find_element_by_id("selectSendInstitutionsForm:j_idt235:j_idt237:filter").clear()
        driver.find_element_by_id("selectSendInstitutionsForm:j_idt235:j_idt237:filter").send_keys("Хеликс")
        time.sleep(2)
        driver.find_element_by_xpath("//td[contains(text(), '7802122535')]").click()
        driver.find_element_by_id("selectSendInstitutionsForm:j_idt247").click()
        time.sleep(2)

        driver.find_element_by_id("filtersForm:j_idt164").click()
        driver.find_element_by_css_selector("#filtersForm\:j_idt164_panel").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt164_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body").click()

        driver.find_element_by_css_selector("#filtersForm\:j_idt164_panel").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt164_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(6) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body").click()

        driver.find_element_by_id("filtersForm:j_idt168").click()
        driver.find_element_by_css_selector("#filtersForm\:j_idt168_panel").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt168_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body").click()

        driver.find_element_by_id("filtersForm:j_idt191").click()
        time.sleep(15)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "1Ц189782"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(11) + "]").text == "ООО \"НПФ \"ХЕЛИКС\""
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(2) + "]").text == "1Ц202636"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(10) + "]").text == "4, Центральный"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(3) + "]/td[" + str(2) + "]").text == "1Ц318971"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(9) + "]").text == "Добровольцы"

        #по результату исследования
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt164 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li:nth-child(1) > span").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt164 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li > span").click()
        driver.find_element_by_css_selector(
            "#filtersForm\:j_idt168 > ul.ui-selectcheckboxmenu-multiple-container.ui-widget.ui-inputfield.ui-state-default.ui-corner-all > li > span").click()
        driver.find_element_by_id("filtersForm:j_idt175_label").click()
        driver.find_element_by_css_selector("#filtersForm\:j_idt175_items").click()
        driver.find_element_by_id("filtersForm:j_idt175_7").click()
        time.sleep(2)
        driver.find_element_by_id("filtersForm:j_idt180_input").click()
        driver.find_element_by_id("filtersForm:j_idt180_input").clear()
        for date in "00:00 1202.90.10":
            driver.find_element_by_id("filtersForm:j_idt180_input").send_keys(Keys.HOME, date)
        driver.find_element_by_id("filtersForm:j_idt183_input").click()
        driver.find_element_by_id("filtersForm:j_idt183_input").clear()
        for date in "00:21 1202.90.10":
            driver.find_element_by_id("filtersForm:j_idt183_input").send_keys(Keys.HOME, date)
        #driver.find_element_by_css_selector("body").click()
        driver.find_element_by_id("filtersForm:j_idt187").click()
        time.sleep(2)
        driver.find_element_by_id("selectLabContractorForm:j_idt252:j_idt254:filter").click()
        driver.find_element_by_id("selectLabContractorForm:j_idt252:j_idt254:filter").clear()
        driver.find_element_by_id("selectLabContractorForm:j_idt252:j_idt254:filter").send_keys("Хеликс")
        time.sleep(2)
        driver.find_element_by_xpath("//tbody[@id='selectLabContractorForm:j_idt252_data']//tr[" + str(3) + "]/td[" + str(2) + "]").click()
        driver.find_element_by_id("selectLabContractorForm:j_idt270").click()
        time.sleep(2)
        driver.find_element_by_id("filtersForm:j_idt191").click()
        time.sleep(2)
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(2) + "]").text == "821Ч4089977"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(13) + "]").text == "Брак"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(2) + "]/td[" + str(2) + "]").text == "821Ч4090034"
        assert driver.find_element_by_xpath(
            "//tbody[@id='tableForm:main-table_data']//tr[" + str(3) + "]/td[" + str(2) + "]").text == "821Ч4090173"







