from selenium import webdriver
class Test_Firefox():
    def launch_firefox(self):
        # instantiate firefox browser
        driver = webdriver.Firefox(executable_path="/1.Running Test On Various Browser\\Drivers\\geckodriver_0.31.0.exe")
        driver.get("https://google.com")
        driver.quit()
firefox_obj= Test_Firefox()
firefox_obj.launch_firefox()
