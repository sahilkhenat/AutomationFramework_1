import  selenium
from selenium.webdriver.common.by import  By

class LandingPage():
    def __init__(self,driver):
        self.driver = driver
        self.home_button_xpath = "//a[@title='Home']"

    def click_home(self):
        self.driver.find_element(By.XPATH, self.home_button_xpath ).click()

