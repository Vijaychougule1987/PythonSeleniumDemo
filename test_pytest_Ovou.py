import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from Ovou_Python_SeleniumProject.test_suite_ovou import current_directory


class Ovoutests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(current_directory + r"\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://test.ovou.me/")
        print("1] Ovou url Enter.")
        time.sleep(3)

    def test_CheckLoginWithInvalidEmail(self):
        print("2] Ovou Check Login With Invalid Email Address.....")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='login-email']").send_keys("aaaassss")
        time.sleep(2)
        print("3] Enter wrong login ID.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//body').click()
        time.sleep(5)
        errordrive = self.driver.find_element(By.ID, 'login-email-feedback')
        errorMsg = errordrive.text
        self.assertEqual('Email format is wrong.', errorMsg, 'error')

    def test_CheckLoginWithShortPassword(self):
        print("2] Ovou Check Login With Wrong Password.")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='login-email']").send_keys("hsk031995@gmail.com")
        print("3] Enter valid login ID.")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input[id='login-password']").send_keys("1234")
        print("4] Enter wrong & Short Password.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//body').click()
        time.sleep(3)
        passworderror = self.driver.find_element(By.ID, 'login-password-feedback')
        errorAlert = passworderror.text
        self.assertEqual('Password at least must be 8 characters.', errorAlert, 'password error')

    def test_CheckLoginWithWrongPassword(self):
        print("2] Ovou Check Login With Wrong Password.")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='login-email']").send_keys("hsk031995@gmail.com")
        print("3] Enter valid login ID.")
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input[id='login-password']").send_keys("1234@test")
        print("4] Enter wrong Password.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//body').click()
        time.sleep(3)

    def test_UserLoginOvou(self):
        print("2] Ovou Check Login With Valid UserName & Password.")
        self.driver.find_element(By.CSS_SELECTOR, "input[id='login-email']").send_keys("hsk031995@gmail.com")
        print("3] Enter login ID.")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "input[id='login-password']").send_keys("test@1234")
        print("4] Enter Password.")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "button[class='chakra-button css-bzjc2j']").click()
        print("5] Click On Login Button.")
        time.sleep(3)
        print("6] Login Successfully Done.")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("# Test Completed.")


if __name__ == '__main__':
    unittest.main()
