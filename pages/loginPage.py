import  selenium
from selenium.webdriver.common.by import  By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.email_textbox_id ="email"
        self.password_textbox_id = "passwd"
        self.login_button_id = "SubmitLogin"

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.login_button_id).click()

