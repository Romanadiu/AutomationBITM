from selenium import webdriver
class Test_Edge():
    def launch_Edge(self):
        # instantiate Edge browser
        driver = webdriver.Edge(executable_path="/1.Running Test On Various Browser\\Drivers\\msedgedriver_103.0.1264.71.exe")

Edge_obj= Test_Edge()
Edge_obj.launch_Edge()
