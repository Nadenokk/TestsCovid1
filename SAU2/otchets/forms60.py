
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
from openpyxl import load_workbook


class CreateOrder(unittest.TestCase):

    def setUp(self):
        download_dir = "C:\\Users\\user\\PycharmProjects\\TestsCovid1\\SAU2\\otchets\\excel_downloads"
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


    def generate_random_string(self):
        letters = string.ascii_lowercase
        rand_string = ''.join(random.choice(letters) for i in range(8))
        return rand_string

    def test_create_order(self):
        driver = self.driver
        driver.get("http://auraep.ru:11080/documents/")
        driver.find_element_by_id("form:usernameInput").click()
        driver.find_element_by_id("form:usernameInput").clear()
        driver.find_element_by_id("form:usernameInput").send_keys("supervisor")
        driver.find_element_by_id("form:passwordInput").click()
        driver.find_element_by_id("form:passwordInput").clear()
        driver.find_element_by_id("form:passwordInput").send_keys("supervisor")
        driver.find_element_by_css_selector("span.ui-button-text.ui-c").click()
        driver.find_element_by_css_selector(
            "#j_idt65 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(7) > a").click()
        driver.find_element_by_id("reportsForm:j_idt74:3:j_idt76").click()
        #заполнение атрибутов
        driver.find_element_by_id("buildForm:j_idt79_input").click()
        driver.find_element_by_id("buildForm:j_idt79_input").clear()
        for date in "1202.80.10":
            driver.find_element_by_id("buildForm:j_idt79_input").send_keys(Keys.HOME, date)
        time.sleep(2)

        driver.find_element_by_id("buildForm:j_idt82_input").click()
        driver.find_element_by_id("buildForm:j_idt82_input").clear()
        for date in "1202.80.01":
            driver.find_element_by_id("buildForm:j_idt82_input").send_keys(Keys.HOME, date)
        time.sleep(2)

        driver.find_element_by_id("buildForm:j_idt85").click()
        driver.find_element_by_id("buildForm:j_idt85").click()
        driver.find_element_by_id("buildForm:j_idt85").send_keys("964587")
        driver.find_element_by_id("buildForm:j_idt88").click()
        driver.find_element_by_id("buildForm:j_idt88").click()
        driver.find_element_by_id("buildForm:j_idt88").send_keys("964599")

        driver.find_element_by_id("buildForm:j_idt97_input").send_keys("Лагерь при школе 69")
        driver.find_element_by_id("buildForm:j_idt97_panel").click()
        time.sleep(2)

        driver.find_element_by_css_selector("#buildForm\:j_idt92_label").click()
        driver.find_element_by_css_selector("#buildForm\:j_idt92_items").click()
        driver.find_element_by_id("buildForm:j_idt92_1").click()

        driver.find_element_by_id("buildForm:j_idt103").click()
        driver.find_element_by_id("buildForm:j_idt103_input").send_keys("Острый эпиглоттит")
        driver.find_element_by_id("buildForm:j_idt103_panel").click()
        time.sleep(2)



        driver.find_element_by_id("buildForm:j_idt73").click()
        time.sleep(4)

        '''
        rol = driver.find_element_by_xpath(
            "//table[@class='jrPage']//tr[" + str(6) + "]/td[" + str(2) + "]/span").text
        print(rol)
        '''
        driver.find_element_by_id("buildForm:j_idt75").click()
        time.sleep(4)

        rootpath = 'C:\\Users\\user\\PycharmProjects\\TestsCovid1\\SAU2\\otchets\\excel_downloads'
        filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
        filelist = [f for f in filelist if os.path.isfile(f)]
        newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
        wb = load_workbook(newest)
        sheet_ranges = wb['information_note']
        rol = sheet_ranges['B3'].value
        rol2 = "Лагерь при школе 69, Супервизор С. "
        #print(rol)
        #print(rol2)
        assert (re.match(r'(?i)' + re.sub(r'\s', '', rol) + r'$', re.sub(r'\s', '', rol2)))


        #print(driver.find_element_by_xpath(
        #    "//table[@class='jrPage']/tbody/tr[" + str(3) + "]/td[" + str(2) + "]/span").text)
        #assert (driver.find_element_by_xpath(
        #    "//table[@class='jrPage']//tbody//tr[" + str(3) + "]/td[" + str(1) + "]/span").text == "Журнал регистрации инфекционных заболеваний (ф.60) за период с 01.08.2021 по 10.08.2021")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()





