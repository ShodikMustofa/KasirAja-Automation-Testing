import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from assets.element import elem

class TestRegist(unittest. TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_regist_success(self):
        driver = self.browser
        driver.get(elem.base_URL)
        self.browser.maximize_window()
        time.sleep(3)

        driver.find_element(By.XPATH, elem.reg_link).click()
        time.sleep(2)
        driver.find_element(By.XPATH, elem.reg_name).send_keys("TokoKU")
        driver.find_element(By.XPATH, elem.reg_email).send_keys("toko_ku@gmail.com")
        driver.find_element(By.XPATH, elem.reg_password).send_keys("qwerty")
        driver.find_element(By.XPATH, elem.reg_daftar).click()
        time.sleep(2)
    
if __name__ == "__main__": 
    unittest.main()