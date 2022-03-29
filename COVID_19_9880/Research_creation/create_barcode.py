# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os

class CreatePcrBarcode(unittest.TestCase):

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
        handler = logging.FileHandler(str('logs/' + (time.strftime(''%d.%m.%Y_%H.%M_'', (time.localtime())))  + 'Create_barcode.log'))
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        try:
            self.create_barcode()
        except Exception as e:
            logger.error('Error detected', exc_info=True)
        else:
            logger.info('Test complete without errors')    
    
    def test_create_barcode(self):
        self.genlog()
    '''
    def test_create_barcode(self):
        driver = self.driver
        #driver.get("http://195.19.96.255:8981/documents/")
        driver.get("http://test.rpn19.ru/business/dashboard/dashboard.xhtml")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("borisova")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("Gi8BbtDN")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        
        # Копируем номер штрихкода
        driver.find_element_by_css_selector(
            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(11) > a > div").click()
        driver.find_element_by_css_selector(u"a[title=\"Поиск штрих-кодов\"] > span").click()
        driver.find_element_by_css_selector("span.ui-icon.ui-icon-triangle-1-s").click()
        driver.find_element_by_css_selector(
            "#filtersform\:j_idt85_panel > div.ui-selectcheckboxmenu-items-wrapper > ul > li:nth-child(3) > div > div.ui-chkbox-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("filtersform:j_idt87").click()
        time.sleep(25)
        driver.find_elements_by_css_selector(
            "#tableForm\:main-table_paginator_bottom > a.ui-paginator-last.ui-state-default.ui-corner-all")[-1].click()
        time.sleep(25)
        barcode = \
            driver.find_elements_by_css_selector("#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(1)")[
                0].text
        iss = driver.find_elements_by_css_selector("#tableForm\:main-table_data > tr:nth-child(1) > td:nth-child(3)")[
            0].text
        #Идем к исследованию по штрихкоду                     
        driver.find_element_by_css_selector("#j_idt72 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element_by_css_selector(u"a[title=\"Создание заявки на исследование 2\"] > span").click()
        driver.find_element_by_css_selector("#buttonsForm\:prepareBarcodeDialog").click()
        driver.find_element_by_css_selector("#barcodeForm\:j_idt86").click()
        driver.find_element_by_css_selector("#barcodeForm\:j_idt86").clear()
        driver.find_element_by_css_selector("#barcodeForm\:j_idt86").send_keys(barcode)
        driver.find_element_by_css_selector("#barcodeForm\:j_idt86").send_keys(Keys.ENTER)

        driver.find_element_by_css_selector("span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        window_before = driver.window_handles[0]
        driver.find_element_by_id("itemForm:tabView:labContractor_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_id("tableForm:main-table:j_id15").click()
        driver.find_element_by_id("tableForm:main-table:j_id15").clear()
        driver.find_element_by_id("tableForm:main-table:j_id15").send_keys(u"един"+Keys.ENTER)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable").click()
        # driver.find_element_by_css_selector(
        #    "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable.ui-state-hover").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        time.sleep(2)
        driver.find_element_by_css_selector("span.ui-radiobutton-icon.ui-icon.ui-icon-blank.ui-c").click()
        #driver.find_element_by_css_selector(
        #    "#itemForm\:tabView\:materialType > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("itemForm:tabView:materialType_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:materialType_items").click()
        driver.find_element_by_id("itemForm:tabView:materialType_2").click()
        time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:materialDate_input").click()
        driver.find_element_by_id("itemForm:tabView:materialDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:materialDate_input").send_keys("21.02.2021 10:00")
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
        driver.find_element_by_id("itemForm:tabView:birthDate_input").send_keys("08.08.1999")
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("itemForm:tabView:email").click()
        driver.find_element_by_id("itemForm:tabView:email").clear()
        driver.find_element_by_id("itemForm:tabView:email").send_keys("shamkin@proweb.ru")
        driver.find_element_by_id("itemForm:tabView:phone").click()
        driver.find_element_by_id("itemForm:tabView:phone").clear()
        driver.find_element_by_id("itemForm:tabView:phone").send_keys("89546521456")
        driver.find_element_by_id("itemForm:tabView:snils").click()
        driver.find_element_by_id("itemForm:tabView:snils").clear()
        driver.find_element_by_id("itemForm:tabView:snils").send_keys("78945212399")
        driver.find_element_by_id("itemForm:tabView:polisOmsSeria").click()
        driver.find_element_by_id("itemForm:tabView:polisOmsSeria").clear()
        driver.find_element_by_id("itemForm:tabView:polisOmsSeria").send_keys("745631")
        driver.find_element_by_id("itemForm:tabView:polisOmsNumber").click()
        driver.find_element_by_id("itemForm:tabView:polisOmsNumber").clear()
        driver.find_element_by_id("itemForm:tabView:polisOmsNumber").send_keys("147856")
        driver.find_element_by_css_selector("#itemForm\:tabView\:identityDocType_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:identityDocType_items").click()
        driver.find_element_by_id("itemForm:tabView:identityDocType_1").click()
        driver.find_element_by_id("itemForm:tabView:identityDocSeries").click()
        driver.find_element_by_id("itemForm:tabView:identityDocSeries").clear()
        driver.find_element_by_id("itemForm:tabView:identityDocSeries").send_keys("4598")
        driver.find_element_by_id("itemForm:tabView:identityDocNumber").click()
        driver.find_element_by_id("itemForm:tabView:identityDocNumber").clear()
        driver.find_element_by_id("itemForm:tabView:identityDocNumber").send_keys("789456")
        driver.find_element_by_id("itemForm:tabView:identityDocIssuedBy").click()
        driver.find_element_by_id("itemForm:tabView:identityDocIssuedBy").clear()
        driver.find_element_by_id("itemForm:tabView:identityDocIssuedBy").send_keys(u"ОУФМС")
        driver.find_element_by_id("itemForm:tabView:identityDocIssuedDate_input").click()
        driver.find_element_by_id("itemForm:tabView:identityDocIssuedDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:identityDocIssuedDate_input").send_keys("11.11.2015")
        driver.find_element_by_css_selector("#itemForm\:tabView\:addressType_label").click()
        driver.find_element_by_id("itemForm:tabView:addressType_label").click()
        driver.find_element_by_id("itemForm:tabView:addressType_1").click()
        driver.find_element_by_id("itemForm:tabView:country_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:country_panel").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:country_1").click()
        driver.find_element_by_id("itemForm:tabView:region_label").click()
        #driver.find_element_by_css_selector("#itemForm\:tabView\:region_items").click()
        #time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:region_1").click()
        time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:city_input").click()
        driver.find_element_by_id("itemForm:tabView:city_input").clear()
        driver.find_element_by_id("itemForm:tabView:city_input").send_keys(u"Ярославль"+Keys.TAB)
        #time.sleep(1)
        #driver.find_element_by_xpath("//span[@id='itemForm:tabView:city_panel']/ul[1]/li[1]/span").click()
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
        driver.find_element_by_id("itemForm:tabView:homeAddressStringValue").click()
        driver.find_element_by_id("itemForm:tabView:homeAddressStringValue").clear()
        driver.find_element_by_id("itemForm:tabView:homeAddressStringValue").send_keys(u"Ярославль, Мира 1 - 18")
        driver.find_element_by_id("itemForm:tabView:tempAddressStringValue").click()
        driver.find_element_by_id("itemForm:tabView:tempAddressStringValue").clear()
        driver.find_element_by_id("itemForm:tabView:tempAddressStringValue").send_keys(u"Ярославль, Мира 1 - 18")
        driver.find_element_by_css_selector("#itemForm\:tabView\:homeCityArea_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:homeCityArea_items").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:homeCityArea_1").click()
        driver.find_element_by_id("itemForm:tabView:orgName").clear()
        driver.find_element_by_id("itemForm:tabView:orgName").send_keys(u"Институт")
        driver.find_element_by_id("itemForm:tabView:workPositionStringValue").click()
        driver.find_element_by_id("itemForm:tabView:workPositionStringValue").clear()
        driver.find_element_by_id("itemForm:tabView:workPositionStringValue").send_keys(u"Студент")
        driver.find_element_by_id("itemForm:tabView:workPhone").click()
        driver.find_element_by_id("itemForm:tabView:workPhone").clear()
        driver.find_element_by_id("itemForm:tabView:workPhone").send_keys("84561237458")
        driver.find_element_by_id("itemForm:tabView:workAddressCountry_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:workAddressCountry_items").click()
        driver.find_element_by_id("itemForm:tabView:workAddressCountry_1").click()
        driver.find_element_by_id("itemForm:tabView:workAddressRegion_label").click()
        #driver.find_element_by_css_selector("#itemForm\:tabView\:workAddressRegion_items").click()
        driver.find_element_by_id("itemForm:tabView:workAddressRegion_1").click()
        driver.find_element_by_id("itemForm:tabView:workAddressCity_input").click()
        driver.find_element_by_id("itemForm:tabView:workAddressCity_input").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressCity_input").send_keys(u"Ярославль"+Keys.TAB)
        #driver.find_element_by_xpath("//span[@id='itemForm:tabView:workAddressCity_panel']/ul/li/span").click()
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").click()
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressStreet_input").send_keys(u"Мира")
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").click()
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressBuilding_input").send_keys("24")
        time.sleep(2)
        driver.find_element_by_id("itemForm:tabView:workAddressFlat").click()
        driver.find_element_by_id("itemForm:tabView:workAddressFlat").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressFlat").send_keys("5")
        driver.find_element_by_id("itemForm:tabView:workAddressStringValue").click()
        driver.find_element_by_id("itemForm:tabView:workAddressStringValue").clear()
        driver.find_element_by_id("itemForm:tabView:workAddressStringValue").send_keys(u"Ярославль, Мира 24 - 5")
        driver.find_element_by_id("itemForm:tabView:patientCategory").click()
        driver.find_element_by_id("itemForm:tabView:patientCategory_label").click()
        driver.find_element_by_id("itemForm:tabView:patientCategory_2").click()
        driver.find_element_by_id("itemForm:tabView:receiptInstitution_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:receiptInstitution_items").click()
        driver.find_element_by_id("itemForm:tabView:receiptInstitution_3").click()
        driver.find_element_by_id("itemForm:tabView:sender").click()
        driver.find_element_by_id("itemForm:tabView:sender").clear()
        driver.find_element_by_id("itemForm:tabView:sender").send_keys(u"Иванов И.И.")
        window_before = driver.window_handles[0]
        driver.find_element_by_id("itemForm:tabView:sendInstitution_selectBtn").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element_by_id("tableForm:main-table:j_id10").click()
        driver.find_element_by_id("tableForm:main-table:j_id10").clear()
        driver.find_element_by_id("tableForm:main-table:j_id10").send_keys(u"сбер"+Keys.ENTER)
        driver.find_element_by_css_selector("#tableForm").click()
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#tableForm\:main-table_data > tr.ui-widget-content.ui-datatable-even.ui-datatable-selectable.ui-state-hover").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#tableForm\:choose").click()
        driver.switch_to.window(window_before)
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").click()
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:arrivalDate_input").send_keys("20.11.2020")
        driver.find_element_by_id("itemForm:tabView:departureCountry_label").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:departureCountry_items").click()
        driver.find_element_by_id("itemForm:tabView:departureCountry_2").click()
        driver.find_element_by_id("itemForm:tabView:flightNumber").click()
        driver.find_element_by_id("itemForm:tabView:flightNumber").clear()
        driver.find_element_by_id("itemForm:tabView:flightNumber").send_keys(u"74ке")
        driver.find_element_by_id("itemForm:tabView:epidNumber").click()
        driver.find_element_by_id("itemForm:tabView:epidNumber").clear()
        driver.find_element_by_id("itemForm:tabView:epidNumber").send_keys(u"78-41в")
        driver.find_element_by_id("itemForm:tabView:simptomsDate_input").click()
        driver.find_element_by_id("itemForm:tabView:simptomsDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:simptomsDate_input").send_keys("15.02.2021")
        driver.find_element_by_id("itemForm:tabView:medicalAidDate_input").click()
        driver.find_element_by_id("itemForm:tabView:medicalAidDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:medicalAidDate_input").send_keys("16.02.2021")
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:medicalState > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_css_selector(
            "#itemForm\:tabView\:medicalState > tbody > tr > td:nth-child(1) > div > div.ui-radiobutton-box.ui-widget.ui-corner-all.ui-state-default > span").click()
        driver.find_element_by_id("itemForm:tabView:complicationStringValue").click()
        driver.find_element_by_id("itemForm:tabView:complicationStringValue").clear()
        driver.find_element_by_id("itemForm:tabView:complicationStringValue").send_keys(u"Нет")
        driver.find_element_by_id("itemForm:tabView:hospitalDate_input").click()
        driver.find_element_by_id("itemForm:tabView:hospitalDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:hospitalDate_input").send_keys("17.02.2021")
        driver.find_element_by_id("itemForm:tabView:terapy").click()
        driver.find_element_by_id("itemForm:tabView:terapy").clear()
        driver.find_element_by_id("itemForm:tabView:terapy").send_keys(u"Нет")
        driver.find_element_by_id("itemForm:tabView:issueDate_input").click()
        driver.find_element_by_id("itemForm:tabView:issueDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:issueDate_input").send_keys("22.02.2021")
        driver.find_element_by_id("itemForm:tabView:description").click()
        driver.find_element_by_id("itemForm:tabView:description").clear()
        driver.find_element_by_id("itemForm:tabView:description").send_keys(u"Нет")
        driver.find_element_by_id("itemForm:tabView:patientContactsCount").click()
        driver.find_element_by_id("itemForm:tabView:patientContactsCount").clear()
        driver.find_element_by_id("itemForm:tabView:patientContactsCount").send_keys("2")
        driver.find_element_by_id("itemForm:tabView:patientContactsFullName").click()
        driver.find_element_by_id("itemForm:tabView:patientContactsFullName").clear()
        driver.find_element_by_id("itemForm:tabView:patientContactsFullName").send_keys(u"Иванов, Петров")
        driver.find_element_by_id("itemForm:tabView:patientContactsPhone").click()
        driver.find_element_by_id("itemForm:tabView:patientContactsPhone").clear()
        driver.find_element_by_id("itemForm:tabView:patientContactsPhone").send_keys("87456911265")
        driver.find_element_by_id("itemForm:tabView:issueDate_input").click()
        driver.find_element_by_id("itemForm:tabView:issueDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:issueDate_input").send_keys("22.02.2021 8:52")
        driver.find_element_by_id("itemForm:tabView:terapy").click()
        driver.find_element_by_css_selector("body.main-body").send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)
        driver.find_element_by_id("itemForm:j_id5").click()
        driver.find_element_by_css_selector("div > div > div.ui-growl-message > p")
        time.sleep(5)
        '''
        driver.find_element_by_id("itemForm:j_id12_button").click()
        driver.find_element_by_id("itemForm:j_id12_menu").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#itemForm\:j_id22").click()
        time.sleep(5)
        driver.find_element_by_id("itemForm:j_id12_button").click()
        driver.find_element_by_id("itemForm:j_id12_menu").click()
        time.sleep(2)
        driver.find_element_by_css_selector("#itemForm\:j_id22").click()
        time.sleep(2).
        '''

        driver.find_element_by_xpath(
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='1']").click()
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("itemForm:tabView:controlResearchResult").click()
        driver.find_element_by_css_selector("#itemForm\:tabView\:controlResearchResult_label").click()
        # driver.find_element_by_css_selector("#itemForm\:tabView\:controlResearchResult_items").click()
        driver.find_element_by_id("itemForm:tabView:controlResearchResult_1").click()
        time.sleep(2)
        '''driver.find_element_by_id("itemForm:tabView:controlResearchDate_input").click()
        driver.find_element_by_id("itemForm:tabView:controlResearchDate_input").clear()
        driver.find_element_by_id("itemForm:tabView:controlResearchDate_input").send_keys("24.05.2021 8:52")'''
        driver.find_element_by_css_selector("body.main-body").click()
        driver.find_element_by_id("itemForm:tabView:controlPcr_input").click()
        driver.find_element_by_id("itemForm:tabView:controlPcr_input").clear()
        driver.find_element_by_id("itemForm:tabView:controlPcr_input").send_keys("1111")
        time.sleep(2)
        '''
        driver.find_element_by_xpath(
            "//li[@class='ui-tabs-header ui-state-default ui-corner-top' and @data-index='8']").click()
        button = driver.find_element_by_id("itemForm:tabView:j_idt137_input")
        button.send_keys(
            "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\COVID_19_9880\\rezultat_issledov\\210630_11_621В1287765-621В912437.xlsx")
        time.sleep(5)
        '''
        driver.find_element_by_id("itemForm:j_id4").click()
        time.sleep(2)


        driver.find_element_by_css_selector("#buttonsForm\:prepareBarcodeDialog")


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
