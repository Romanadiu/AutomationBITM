from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By


class Multiple_Window():
    def switching_window(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/windows")
        time.sleep(2)

        parent_window = driver.current_window_handle
        print()
        print(parent_window)

        driver.find_element(By.LINK_TEXT, 'Click Here').click()

        all_window = driver.window_handle
        time.sleep(3)
        print(all_window)

        # switch to child

    for child_window in all_window:
        if child_window not in parent_window:
            driver.switch_to.window(child_window)
            print('parent window Title : ' + driver.title)

        driver.close()

        driver.quir()


test_obj = Multiple_Window()
test_obj.switching_window()
