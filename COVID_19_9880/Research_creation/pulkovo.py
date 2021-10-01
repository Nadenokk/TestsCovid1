# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait


class CreatePCR(unittest.TestCase):
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
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Create_Antitel.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.create_antitel()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    

    def test_create_antitel(self):
        self.genlog()
    '''
    def test_create_pcr(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml")
        #driver.get("https://rpn19.ru:11443/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("pulkovo@pulkovo.ru")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("pulkovo@pulkovo.ru")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector("#j_idt66 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(2) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Создание заявки на исследование 2\"] > span").click()
        driver.find_element_by_css_selector("#buttonsForm\:createPcr").click()
        time.sleep(3)
        numberIss=driver.find_element_by_id("itemForm:docNumber").get_attribute("value")

        #driver.find_element_by_css_selector(
        #    "#itemForm\:tabView\:materialType > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("itemForm:tabView:materialType_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:materialType_items").click()
        driver.find_element_by_id("itemForm:tabView:materialType_2").click()
        time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:materialDate_input").click()
        driver.find_element_by_id("itemForm:tabView:materialDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:materialDate_input").send_keys("030820211000")
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("itemForm:tabView:lastName").click()
        driver.find_element_by_id("itemForm:tabView:lastName").clear()
        driver.find_element_by_id("itemForm:tabView:lastName").send_keys(u"СаблинАнтител")
        driver.find_element_by_id("itemForm:tabView:firstName").click()
        driver.find_element_by_id("itemForm:tabView:firstName").clear()
        driver.find_element_by_id("itemForm:tabView:firstName").send_keys(u"Роман")
        driver.find_element_by_id("itemForm:tabView:patronymicName").click()
        driver.find_element_by_id("itemForm:tabView:patronymicName").clear()
        driver.find_element_by_id("itemForm:tabView:patronymicName").send_keys(u"Евгеньевич")
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:sex > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("itemForm:tabView:birthDate_input").click()
        driver.find_element_by_id("itemForm:tabView:birthDate_input").clear()
        for date in "08911111":
            driver.find_element_by_id("itemForm:tabView:birthDate_input").send_keys(Keys.HOME, date)
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("itemForm:tabView:email").click()
        driver.find_element_by_id("itemForm:tabView:email").clear()
        driver.find_element_by_id("itemForm:tabView:email").send_keys("shamkin@proweb.ru")
        driver.find_element_by_id("itemForm:tabView:phone").click()
        driver.find_element_by_id("itemForm:tabView:phone").clear()
        driver.find_element_by_id("itemForm:tabView:phone").send_keys("+7(812)123-12-12")
        driver.find_element_by_id("itemForm:tabView:snils").click()
        driver.find_element_by_id("itemForm:tabView:snils").clear()
        driver.find_element_by_id("itemForm:tabView:snils").send_keys("78945212399")
        driver.find_element_by_id("itemForm:tabView:polisOmsSeria").click()
        driver.find_element_by_id("itemForm:tabView:polisOmsSeria").clear()
        driver.find_element_by_id("itemForm:tabView:polisOmsSeria").send_keys("745631")
        driver.find_element_by_id("itemForm:tabView:polisOmsNumber").click()
        driver.find_element_by_id("itemForm:tabView:polisOmsNumber").clear()
        driver.find_element_by_id("itemForm:tabView:polisOmsNumber").send_keys("147856")
        driver.find_element_by_id("itemForm:tabView:city_input").click()
        driver.find_element_by_id("itemForm:tabView:city_input").clear()
        driver.find_element_by_id("itemForm:tabView:city_input").send_keys(u"Ярославль")
        driver.find_element_by_xpath("//span[@id='itemForm:tabView:city_panel']/ul[1]/li[1]/span").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressStreet_input").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressStreet_input").clear()
        driver.find_element_by_id("itemForm:tabView:homeAddressStreet_input").send_keys(u"Мира")
        driver.find_element_by_id("itemForm:tabView:homeAddressBuilding_input").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressBuilding_input").clear()
        driver.find_element_by_id("itemForm:tabView:homeAddressBuilding_input").send_keys("1")
        time.sleep(2)

        driver.find_element_by_id("itemForm:tabView:homeAddressFlat").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressFlat").clear()
        driver.find_element_by_id("itemForm:tabView:homeAddressFlat").send_keys("18")

        driver.find_element_by_id("itemForm:tabView:orgName").clear()
        driver.find_element_by_id("itemForm:tabView:orgName").send_keys(u"Институт")
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").click()
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").send_keys(u"Мира")
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").click()
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").send_keys("24")
        time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:patientCategory").click()
        driver.find_element_by_id("itemForm:tabView:patientCategory_label").click()
        driver.find_element_by_id("itemForm:tabView:patientCategory_2").click()
        driver.find_element_by_id("itemForm:tabView:sender").click()
        driver.find_element_by_id("itemForm:tabView:sender").clear()
        driver.find_element_by_id("itemForm:tabView:sender").send_keys(u"Иванов И.И.")
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").click()
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").send_keys("20.11.2020")
        driver.find_element_by_id("itemForm:tabView:departureCountry_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:departureCountry_items").click()
        driver.find_element_by_id("itemForm:tabView:departureCountry_2").click()
        driver.find_element_by_id("itemForm:tabView:flightNumber").click()
        driver.find_element_by_id("itemForm:tabView:flightNumber").clear()
        driver.find_element_by_id("itemForm:tabView:flightNumber").send_keys(u"74ке")
        driver.find_element_by_id("itemForm:tabView:issueDate_input").click()
        driver.find_element_by_id("itemForm:tabView:issueDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:issueDate_input").send_keys("22.02.2021")
        driver.find_element_by_id("itemForm:tabView:description").click()
        driver.find_element_by_id("itemForm:tabView:description").clear()
        driver.find_element_by_id("itemForm:tabView:description").send_keys(u"Нет")
        driver.find_element_by_css_selector("body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        driver.find_element_by_id("itemForm:j_id5").click()
        driver.find_element_by_css_selector("div > div > div.ui-growl-message > p")
        time.sleep(2)
        driver.find_element_by_id("itemForm:j_id4").click()
        time.sleep(2)

        driver.find_element_by_css_selector(
            "#j_idt66 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(2) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Поиск исследований\"] > span").click()
        driver.find_element_by_id("filtersForm:j_idt101").click()
        driver.find_element_by_id("filtersForm:j_idt101").clear()
        driver.find_element_by_id("filtersForm:j_idt101").send_keys(numberIss)

        driver.find_element_by_id("filtersForm:j_idt187").click()
        time.sleep(30)
        driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        #driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]").click()
        wait = WebDriverWait(driver, 10)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles
        actionChains = ActionChains(driver)
        actionChains.double_click(driver.find_element_by_xpath("//tbody[@id='tableForm:main-table_data']//tr[" + str(1) + "]/td[" + str(1) + "]")).perform()
        wait.until(ec.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        driver.find_element_by_id("itemForm:j_id4")



