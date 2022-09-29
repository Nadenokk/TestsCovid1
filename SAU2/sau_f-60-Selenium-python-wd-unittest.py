# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import logging, os
from openpyxl import load_workbook

class SauF60(unittest.TestCase):
    def setUp(self):
        download_dir = "C:\\Users\\user\\Desktop\\downloads_otchet"
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
    
    def test_sau_f60(self):
        driver = self.driver
        # Label: Test
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1920,937 | ]]
        driver.get("http://sau.rpn19.ru:11080/business/dashboard/dashboard.xhtml#")
        driver.find_element(By.ID,"form:usernameInput").click()
        driver.find_element(By.ID,"form:usernameInput").clear()
        driver.find_element(By.ID,"form:usernameInput").send_keys("borisova@webdom.net")
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").click()
        driver.find_element(By.ID,"form:passwordInput").clear()
        driver.find_element(By.ID,"form:passwordInput").send_keys("cudEJkKl")
        driver.find_element(By.CSS_SELECTOR,"span.ui-button-text.ui-c").click()
        driver.find_element(By.CSS_SELECTOR,
            "#j_idt71 > div.nano.layout-tabmenu-nav.has-scrollbar > ul > li:nth-child(9) > a").click()
        driver.find_element(By.XPATH,"//button[@id='reportsForm:j_idt79:5:j_idt81']/span").click()
        driver.find_element(By.ID,"buildForm:j_idt85_input").click()
        driver.find_element(By.ID, "buildForm:j_idt85_input").clear()
        driver.find_element(By.ID,"buildForm:j_idt85_input").send_keys("01.02.2022")
        driver.find_element(By.ID,"buildForm:j_idt88_input").click()
        driver.find_element(By.ID, "buildForm:j_idt88_input").clear()
        driver.find_element(By.ID, "buildForm:j_idt88_input").send_keys("01.02.2022")
        driver.find_element(By.ID,"buildForm:j_idt97_label").click()
        driver.find_element(By.ID,"buildForm:j_idt97_2").click()
        driver.find_element(By.ID,"buildForm:j_idt111_label").click()
        driver.find_element(By.ID,"buildForm:j_idt111_2").click()
        driver.find_element(By.ID, "buildForm:j_idt116").click()
        driver.find_element(By.ID, "buildForm:j_idt116_input").send_keys("СПБ ГБУЗ Городская поликлиника № 4 (поликлиника №4, ГП4)")
        driver.find_element(By.CSS_SELECTOR,"li.ui-autocomplete-item.ui-autocomplete-list-item.ui-corner-all.ui-state-highlight > span.ui-autocomplete-query").click()
        driver.find_element(By.ID,"buildForm:j_idt119_input").click()
        driver.find_element(By.ID, "buildForm:j_idt119_input").send_keys("7.1.2")
        driver.find_element(By.XPATH,"//span[@id='buildForm:j_idt119_panel']/ul/li").click()
        window_before = driver.window_handles[0]
        driver.find_element(By.ID, "buildForm:j_idt126").click()
        window_after = driver.window_handles[1]
        driver.switch_to.window(window_after)
        driver.find_element(By.ID, "tableForm:main-table:j_id13").send_keys("МЦ Хеликс ПР")
        time.sleep(3)
        driver.find_element(By.ID, "tableForm:main-table_data").click()
        driver.find_element(By.XPATH, "//td[contains(text(), 'МЦ Хеликс ПР')]").click()
        time.sleep(4)
        driver.find_element(By.ID, "tableForm:choose").click()
        driver.switch_to.window(window_before)
        driver.find_element(By.XPATH,"//button[@id='buildForm:j_idt79']/span").click()
        time.sleep(6)

        # Ищем iframe и переключаемся на него
        #iframe = driver.find_element(By.XPATH,'//*[@id="dataForm:reportPanel"]/embed')
        #driver.switch_to.frame(iframe)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "embed"))
        driver.switch_to.default_content()
        rol = driver.find_element(By.XPATH,
            "//table[@class='jrPage']//tbody//tr[" + str(3) + "]/td[" + str(1) + "]/span").get_attribute("textContent")
        print(rol)






       # assert (driver.find_element(By.XPATH,
                                #   "/html/body/table/tbody/tr/td[2]/table/tbody/tr[7]/td[2]").text== "1960738, 01.02.2022 05:50, ORN Нестеренко Надежда")
        time.sleep(5)

        driver.find_element(By.XPATH,"//button[@id='buildForm:j_idt80']/span").click()
        time.sleep(8)
        rootpath = 'C:\\Users\\user\\Desktop\\downloads_otchet'
        filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
        filelist = [f for f in filelist if os.path.isfile(f)]
        newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
        wb = load_workbook(newest)
        sheet_ranges = wb['information_note']
        str1 = sheet_ranges['A3'].value
        str2 = sheet_ranges['O4'].value
        assert (str1 == "1960738, 01.02.2022 05:50, ORN Нестеренко Надежда ")
        assert (str2 == "Спутник V, 10.10.2021, 1")
        os.remove(newest)







    
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
