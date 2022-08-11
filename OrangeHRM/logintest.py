from selenium import webdriver
import time
from selenium.webdriver.common.by import By


class Launch_firefox():
    def run_firefox(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\USER\\PycharmProjects\\AutomationBITM\\Drivers\\geckodriver_0.31.0.exe")
        driver.get('https://opensource-demo.orangehrmlive.com')
        time.sleep(2)

        username = driver.find_element(By.NAME, 'txtUsername')
        password = driver.find_element(By.XPATH,   '//*[@id="txtPassword"]')
        loginBtn = driver.find_element(By.CSS_SELECTOR, '#btnLogin')

        username.send_keys("Admin")
        password.send_keys('admin123')
        loginBtn.click()

        time.sleep(3)

        driver.close()


test_obj = Launch_firefox()
test_obj.run_firefox()
