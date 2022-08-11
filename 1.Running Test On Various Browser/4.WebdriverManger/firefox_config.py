from selenium import webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

class firefox():
    def firefox_launch(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        driver.get("https://google.com")
        driver.close()

test_obj = firefox()
test_obj.firefox_launch()

