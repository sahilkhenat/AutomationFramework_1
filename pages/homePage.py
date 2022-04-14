import  selenium
from selenium.webdriver.common.by import  By

class HomePage():

    def __init__(self, driver):
        self.driver = driver
        self.logout_button_xpath = "//a[@class='logout']"

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()
