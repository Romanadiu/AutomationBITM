from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class OrangeHRM():
    def login(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")

        forgot_password = driver.find_element(By.LINK_TEXT,'Forgot your password?')

        if forgot_password is not None:
            print("We found forgot password by Link Text")
        else:
            print("We dont found forgot password by Link Text")


test_obj=OrangeHRM()
test_obj.login()


