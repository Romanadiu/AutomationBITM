from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class TitleURL():
    def title_verification(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        base_url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
        driver.get(base_url)
        title = driver.title
        print(title)

        actual_title = driver.title
        print(actual_title)

        expected_title = 'OrangeHRM'

        if expected_title == actual_title:
            print("Title matched. Test passed")

        else:
            print("Title mismatched. Test failed")


        driver.close()

    def url_verification(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        base_url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
        driver.get(base_url)

        current_url = driver.current_url
        print(current_url)

        driver.close()


test_obj = TitleURL()
test_obj.title_verification()
test_obj.url_verification()
