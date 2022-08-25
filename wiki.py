import selenium
from selenium import webdriver
from time import sleep

class information():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path="C:\\Users\\RITVIK JOHNSON\\OneDrive\\Desktop\\python_work\\AI\\Driver\\chromedriver_win32\\chromedriver.exe")

    def get_info(self,query):
        self.driver.get(url="https://wikipedia.org")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()


    



