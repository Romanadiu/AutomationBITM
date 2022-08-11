from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class Screenshots_demo():
    def capture(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://google.com')
        time.sleep(2)

        driver.get_screenshot_as_file('C:\\Users\\USER\\PycharmProjects\\AutomationBITM\\Bugs_Screenshots\\google.png')


obj = Screenshots_demo()
obj.capture()
