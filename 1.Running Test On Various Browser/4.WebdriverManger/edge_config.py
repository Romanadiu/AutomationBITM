from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class edge():
    def edge_launch(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        driver.get('https://google.com')
        driver.close()

test_obj = edge()
test_obj.edge_launch()


