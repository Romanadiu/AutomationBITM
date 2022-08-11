from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import ActionChains

class Mouse():
    def switching_window(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(2)


        username = driver.find_element(By.Id, 'txtUsername')
        password = driver.find_element(By.Id, 'txtPassword')
        login_btn = driver.find_element(By.Id, 'txtLogin')

        username.send_keys('Admin')
        password.send_keys('admin123')
        time.sleep(5)

        leave_menu = driver.find_element(By.XPATH, '//*@id="menu_viewleaveModule"]/b')
        actions.move_to_element(leave_menu).perform()
        



