from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class FileUpload():
    def uploaded_file(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get("https://the-internet.herokuapp.com/upload")
        time.sleep(2)
        driver.maximize_window()

        choose_file_btn = driver.find_element(By.Id, 'file-upload')
        choose_file_btn.send_keys(" ")


        time.sleep(5)


obj = FileUpload()
obj.uploaded_file()