from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Chrome():
    def Chrome_launch(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://google.com")


test_obj=Chrome()
test_obj.Chrome_launch()


