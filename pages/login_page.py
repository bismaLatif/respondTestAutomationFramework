from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    email_field = (By.ID, "input-7")
    password_field = (By.ID, "input-9")
    signin_button = (By.CSS_SELECTOR, '[data-pw="btn-signin"]')
    alert = (By.CSS_SELECTOR, "div.text.elevation-1")
    profile_icon = (By.CSS_SELECTOR, "div.v-avatar > i#isax-bold")
    signout_button = (By.XPATH, "//div[contains(@class, 'dls-txt-button') and .//div[text()='Sign out']]")

    def enter_email(self, email):
        self.find_element(self.email_field).send_keys(email)

    def enter_password(self, password):
        self.find_element(self.password_field).send_keys(password)

    def click_signin(self):
        self.find_element(self.signin_button).click()

    def login(self, email, password):
        self.open("/login")
        self.enter_email(email)
        self.enter_password(password)
        self.click_signin()

    def get_alert(self):
        return self.find_element(self.alert)

    def click_profile_icon(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.profile_icon)
        )
        self.find_element(self.profile_icon).click()

    def click_signout(self):
        self.click_profile_icon()
        self.find_element(self.signout_button).click()
