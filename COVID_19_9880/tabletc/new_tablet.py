# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
import sys
from selenium.webdriver.support import expected_conditions as ec

from selenium.webdriver.support.wait import WebDriverWait


class NewTablet(unittest.TestCase):

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

    def test_new_tablet(self):
        driver = self.driver
        driver.get("http://auraep.ru:9880/business/dashboard/dashboard.xhtml")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Ivwdk1Rp")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()

        # Копируем номер штрихкода
        driver.find_element_by_css_selector(
            "#j_idt68 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(11) > a > div").click()
        driver.find_element_by_css_selector(u"a[title=\"Штрих-коды\"] > span").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element_by_xpath("/html/body/div[9]/div[2]/ul/li[2]/div/div[2]/span").click()
        time.sleep(50)
        '''
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id5_input").click()
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id5_input").clear()
        driver.find_element_by_css_selector("#tableForm\:main-table\:j_id5_input").send_keys("04.03.2021")
        driver.find_element_by_css_selector("body").click()
        '''
        time.sleep(7)
        driver.find_elements_by_css_selector(
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(30)
        # driver.find_elements_by_css_selector(
        #    "#tableForm\:main-table_paginator_bottom > a.ui-paginator-first.ui-state-default.ui-corner-all")[0].click()
        # time.sleep(7)
        element = driver.find_elements_by_css_selector("#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(1)")[0].text


        #планшеты
        driver.find_element_by_css_selector(
            "#j_idt68 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(8) > a > div > div.layout-tabmenu-tooltip-text").click()
        #driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_id("j_idt76").click()
        time.sleep(3)
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:patientCategories_panel").click()
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:patientCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(1) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:patientCategories_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(2) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector("body.main-body").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_css_selector("span.ui-button-icon-left.ui-icon.ui-c.fa.fa-ellipsis-h").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:main-table_data > tr:nth-child(3)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        #проба
        driver.find_element_by_xpath(
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        driver.find_element_by_id("itemForm:tabView:j_idt114").click()
        driver.find_element_by_id("addByBarcodeForm:j_idt311").send_keys(element+Keys.ENTER)
        time.sleep(10)
        driver.find_element_by_css_selector("span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        '''
        window_before = driver.window_handles[0]
        driver.find_element_by_id("covidResearchForm:tabView:labContractor_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:main-table_data > tr:nth-child(3)").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        '''
        time.sleep(2)
        driver.find_element_by_css_selector("span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        driver.find_element_by_css_selector(
            "#covidResearchForm\:tabView\:materialType > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        time.sleep(2)
        driver.find_element_by_id("covidResearchForm:tabView:materialDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:materialDate_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:materialDate_input").send_keys("21.02.2021 10:00")
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:j_id179 > tbody").click()
        driver.find_element_by_id("covidResearchForm:tabView:lastName").click()
        driver.find_element_by_id("covidResearchForm:tabView:lastName").clear()
        driver.find_element_by_id("covidResearchForm:tabView:lastName").send_keys(u"СаблинАнтител")
        driver.find_element_by_id("covidResearchForm:tabView:firstName").click()
        driver.find_element_by_id("covidResearchForm:tabView:firstName").clear()
        driver.find_element_by_id("covidResearchForm:tabView:firstName").send_keys(u"Роман")
        driver.find_element_by_id("covidResearchForm:tabView:patronymicName").click()
        driver.find_element_by_id("covidResearchForm:tabView:patronymicName").clear()
        driver.find_element_by_id("covidResearchForm:tabView:patronymicName").send_keys(u"Евгеньевич")
        driver.find_element_by_css_selector(
            "#covidResearchForm\:tabView\:sex > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("covidResearchForm:tabView:birthDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:birthDate_input").clear()
        for date in "08911111":
            driver.find_element_by_id("covidResearchForm:tabView:birthDate_input").send_keys(Keys.HOME, date)
        driver.find_element_by_id("covidResearchForm:tabView:j_id150_content").click()
        driver.find_element_by_id("covidResearchForm:tabView:email").click()
        driver.find_element_by_id("covidResearchForm:tabView:email").clear()
        driver.find_element_by_id("covidResearchForm:tabView:email").send_keys("shamkin@proweb.ru")
        driver.find_element_by_id("covidResearchForm:tabView:phone").click()
        driver.find_element_by_id("covidResearchForm:tabView:phone").clear()
        driver.find_element_by_id("covidResearchForm:tabView:phone").send_keys("89546521456")
        driver.find_element_by_id("covidResearchForm:tabView:snils").click()
        driver.find_element_by_id("covidResearchForm:tabView:snils").clear()
        driver.find_element_by_id("covidResearchForm:tabView:snils").send_keys("789452123")
        driver.find_element_by_id("covidResearchForm:tabView:polisOmsSeria").click()
        driver.find_element_by_id("covidResearchForm:tabView:polisOmsSeria").clear()
        driver.find_element_by_id("covidResearchForm:tabView:polisOmsSeria").send_keys("745631")
        driver.find_element_by_id("covidResearchForm:tabView:polisOmsNumber").click()
        driver.find_element_by_id("covidResearchForm:tabView:polisOmsNumber").clear()
        driver.find_element_by_id("covidResearchForm:tabView:polisOmsNumber").send_keys("147856")
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:identityDocType_label").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:identityDocType_items").click()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocType_1").click()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocSeries").click()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocSeries").clear()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocSeries").send_keys("4598")
        driver.find_element_by_id("covidResearchForm:tabView:identityDocNumber").click()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocNumber").clear()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocNumber").send_keys("789456")
        driver.find_element_by_id("covidResearchForm:tabView:identityDocIssuedBy").click()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocIssuedBy").clear()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocIssuedBy").send_keys(u"ОУФМС")
        driver.find_element_by_id("covidResearchForm:tabView:identityDocIssuedDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocIssuedDate_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:identityDocIssuedDate_input").send_keys("11.11.2015")
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:addressType_label").click()
        driver.find_element_by_id("covidResearchForm:tabView:addressType_label").click()
        driver.find_element_by_id("covidResearchForm:tabView:addressType_1").click()
        driver.find_element_by_id("covidResearchForm:tabView:country_label").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:country_panel").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:country_1").click()
        driver.find_element_by_id("covidResearchForm:tabView:region_label").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:region_items").click()
        time.sleep(2)
        driver.find_element_by_id("covidResearchForm:tabView:region_1").click()
        time.sleep(2)
        driver.find_element_by_id("covidResearchForm:tabView:city_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:city_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:city_input").send_keys(u"Ярослав")
        driver.find_element_by_css_selector("span.ui-autocomplete-query").click()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressStreet_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressStreet_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressStreet_input").send_keys(u"Мира")
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressBuilding_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressBuilding_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressBuilding_input").send_keys("1")
        time.sleep(2)
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressFlat").click()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressFlat").clear()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressFlat").send_keys("18")
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressStringValue").click()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressStringValue").clear()
        driver.find_element_by_id("covidResearchForm:tabView:homeAddressStringValue").send_keys(u"Ярославль, Мира 1 - 18")
        driver.find_element_by_id("covidResearchForm:tabView:tempAddressStringValue").click()
        driver.find_element_by_id("covidResearchForm:tabView:tempAddressStringValue").clear()
        driver.find_element_by_id("covidResearchForm:tabView:tempAddressStringValue").send_keys(u"Ярославль, Мира 1 - 18")
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:homeCityArea_label").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:homeCityArea_items").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:homeCityArea_1").click()
        driver.find_element_by_id("covidResearchForm:tabView:orgName").clear()
        driver.find_element_by_id("covidResearchForm:tabView:orgName").send_keys(u"Институт")
        driver.find_element_by_id("covidResearchForm:tabView:workPositionStringValue").click()
        driver.find_element_by_id("covidResearchForm:tabView:workPositionStringValue").clear()
        driver.find_element_by_id("covidResearchForm:tabView:workPositionStringValue").send_keys(u"Студент")
        driver.find_element_by_id("covidResearchForm:tabView:workPhone").click()
        driver.find_element_by_id("covidResearchForm:tabView:workPhone").clear()
        driver.find_element_by_id("covidResearchForm:tabView:workPhone").send_keys("84561237458")
        driver.find_element_by_id("covidResearchForm:tabView:workAddressCountry_label").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:workAddressCountry_items").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressCountry_1").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressRegion_label").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:workAddressRegion_items").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressRegion_1").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressCity_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressCity_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressCity_input").send_keys(u"Яросла")
        driver.find_element_by_xpath("//span[@id='covidResearchForm:tabView:workAddressCity_panel']/ul/li/span").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressStreet_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressStreet_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressStreet_input").send_keys(u"Мира")
        driver.find_element_by_id("covidResearchForm:tabView:workAddressBuilding_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressBuilding_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressBuilding_input").send_keys("24")
        time.sleep(2)
        driver.find_element_by_id("covidResearchForm:tabView:workAddressFlat").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressFlat").clear()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressFlat").send_keys("5")
        driver.find_element_by_id("covidResearchForm:tabView:workAddressStringValue").click()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressStringValue").clear()
        driver.find_element_by_id("covidResearchForm:tabView:workAddressStringValue").send_keys(u"Ярославль, Мира 24 - 5")
        driver.find_element_by_id("covidResearchForm:tabView:patientCategory").click()
        driver.find_element_by_id("covidResearchForm:tabView:patientCategory_label").click()
        driver.find_element_by_id("covidResearchForm:tabView:patientCategory_2").click()
        driver.find_element_by_id("covidResearchForm:tabView:receiptInstitution_label").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:receiptInstitution_items").click()
        driver.find_element_by_id("covidResearchForm:tabView:receiptInstitution_3").click()
        driver.find_element_by_id("covidResearchForm:tabView:sender").click()
        driver.find_element_by_id("covidResearchForm:tabView:sender").clear()
        driver.find_element_by_id("covidResearchForm:tabView:sender").send_keys(u"Иванов И.И.")
        window_before = driver.window_handles[0]
        driver.find_element_by_id("covidResearchForm:tabView:sendInstitution_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_id("tableForm:main-table:j_id5").click()
        driver.find_element_by_id("tableForm:main-table:j_id5").clear()
        driver.find_element_by_id("tableForm:main-table:j_id5").send_keys(u"сбер")
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable.ui-state-hover").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        driver.find_element_by_id("covidResearchForm:tabView:arrivalDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:arrivalDate_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:arrivalDate_input").send_keys("20.11.2020")
        driver.find_element_by_id("covidResearchForm:tabView:departureCountry_label").click()
        driver.find_element_by_css_selector("#covidResearchForm\:tabView\:departureCountry_items").click()
        driver.find_element_by_id("covidResearchForm:tabView:departureCountry_2").click()
        driver.find_element_by_id("covidResearchForm:tabView:flightNumber").click()
        driver.find_element_by_id("covidResearchForm:tabView:flightNumber").clear()
        driver.find_element_by_id("covidResearchForm:tabView:flightNumber").send_keys(u"74ке")
        driver.find_element_by_id("covidResearchForm:tabView:epidNumber").click()
        driver.find_element_by_id("covidResearchForm:tabView:epidNumber").clear()
        driver.find_element_by_id("covidResearchForm:tabView:epidNumber").send_keys(u"78-41в")
        driver.find_element_by_id("covidResearchForm:tabView:simptomsDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:simptomsDate_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:simptomsDate_input").send_keys("15.02.2021")
        driver.find_element_by_id("covidResearchForm:tabView:medicalAidDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:medicalAidDate_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:medicalAidDate_input").send_keys("16.02.2021")
        driver.find_element_by_css_selector(
            "#covidResearchForm\:tabView\:medicalState > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#covidResearchForm\:tabView\:medicalState > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("covidResearchForm:tabView:complicationStringValue").click()
        driver.find_element_by_id("covidResearchForm:tabView:complicationStringValue").clear()
        driver.find_element_by_id("covidResearchForm:tabView:complicationStringValue").send_keys(u"Нет")
        driver.find_element_by_id("covidResearchForm:tabView:hospitalDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:hospitalDate_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:hospitalDate_input").send_keys("17.02.2021")
        driver.find_element_by_id("covidResearchForm:tabView:terapy").click()
        driver.find_element_by_id("covidResearchForm:tabView:terapy").clear()
        driver.find_element_by_id("covidResearchForm:tabView:terapy").send_keys(u"Нет")
        driver.find_element_by_id("covidResearchForm:tabView:issueDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:issueDate_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:issueDate_input").send_keys("22.02.2021")
        driver.find_element_by_id("covidResearchForm:tabView:description").click()
        driver.find_element_by_id("covidResearchForm:tabView:description").clear()
        driver.find_element_by_id("covidResearchForm:tabView:description").send_keys(u"Нет")
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsCount").click()
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsCount").clear()
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsCount").send_keys("2")
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsFullName").click()
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsFullName").clear()
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsFullName").send_keys(u"Иванов, Петров")
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsPhone").click()
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsPhone").clear()
        driver.find_element_by_id("covidResearchForm:tabView:patientContactsPhone").send_keys("87456911265")
        driver.find_element_by_id("covidResearchForm:tabView:issueDate_input").click()
        driver.find_element_by_id("covidResearchForm:tabView:issueDate_input").clear()
        driver.find_element_by_id("covidResearchForm:tabView:issueDate_input").send_keys("22.02.2021 8:52")
        driver.find_element_by_id("covidResearchForm:tabView:terapy").click()
        #driver.find_element_by_css_selector("body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        #time.sleep(2)
        driver.find_element_by_id("covidResearchForm:j_idt541").click()
        time.sleep(30)
        driver.find_element_by_id("itemForm:j_id4").click()

        #driver.find_element_by_css_selector("div > div > div.ui-growl-message > p")
        time.sleep(2)

        driver.find_element_by_id("j_idt76")





