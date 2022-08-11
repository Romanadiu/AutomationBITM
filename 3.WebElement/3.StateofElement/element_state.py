from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Element():
    def enable(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()

        base_url = 'https://opensource-demo.orangehrmlive.com/index.php/auth/login'
        driver.get(base_url)

        save_and_continue_btn = driver.find_element(By.CLASS_NAME,'button')

        state = save_and_continue_btn. is_enabled()
        print(state)

        driver.close()
        time.sleep(5)


test_obj = Element()
test_obj.enable()

