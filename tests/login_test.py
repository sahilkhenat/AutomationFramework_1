from selenium import  webdriver
from selenium.common.exceptions import NoSuchElementException
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import time
import pytest
from pages.loginPage import LoginPage
from pages.landingPage import LandingPage
from pages.homePage import HomePage
from  utils import utils as utils
import  allure
import  moment
from  Screenshot import Screenshot_Clipping
from PIL import  Image

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_email(utils.EMAIL)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        # driver.find_element(By.ID,"email").send_keys("skhenat_pr@medable.com")
        # driver.find_element(By.ID, "passwd").send_keys("medable123")
        # driver.find_element(By.ID, "SubmitLogin").click()

    def test_home_click(self):
        driver = self.driver
        landingpage = LandingPage(driver)
        landingpage.click_home()
        # driver.find_element(By.XPATH,"//a[@title='Home']").click()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_logout()
            x = driver.title
            print(x)
            if  x =="My Store":
                assert True
            else:
                assert False

        except NoSuchElementException as nosuch:
            print("No such element found")
            print(nosuch)

            currTime = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            ss = Screenshot_Clipping.Screenshot()
            screen_shot = ss.full_Screenshot(driver, save_path="D:/PycharmProjects/AutomationFramework_1/screenshots", image_name=screenshotName+".png")
            raise

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H:%M:%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("There was an exception")
            raise

        else:
            print("No exceptions occurred")

        finally:
            print("I am inside finally block")
        # driver.find_element(By.XPATH,"//a[@class='logout']").click()

