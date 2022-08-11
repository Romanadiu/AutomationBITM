from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Headless():
    def chrome_headless(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        driver = webdriver.Chrome(ChromeDriverManager().install(), options = chrome_options)
        driver.get("https://google.com")
        print("Title on Headless Chrome : " + driver.title)
        driver.close()

    def firefox_headless(self):
        firefox_options = webdriver.ChromeOptions()
        firefox_options.headless = True
        driver = webdriver.Firefox(GeckoDriverManager().install(), options=firefox_options)
        driver.get("https://apple.com")
        print("Title on Headless Firefox : " + driver.title)

        driver.close()

obj = Headless()
obj.chrome_headless()
obj.firefox_headless()
