from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import ActionChains

class dragDrop():
    def dragDrop_demo(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("")
        time.sleep(2)

        from_element = driver.find_element(By.Id, 'column-a')
        to_element = driver.find_element(By.Id, 'column-b')

        actions = ActionChains(driver)
        actions.drag_and_drop(source, target).perform()
        time.sleep(5)

        driver.close()

obj = DragDrop()
obj.dragDrop_demo()