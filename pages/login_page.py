# -*- coding: UTF-8 -*-

from .base_page import Page
from selenium.webdriver.common.keys import Keys


class LoginPage(Page):
    
    """
    Login form 
    """

    url = '/sign_in'

    def input_login(self):  # TODO add 2nd var for 2nd driver
        return self.context.driver.find_element_by_id("email")  # TODO replace to driver+var

    def input_pass(self):
        return self.context.driver.find_element_by_id("password") # TODO same

    def btn_signin(self):
        return self.context.driver.find_element_by_id("signin") # TODO same

    def enter_login(self, login): # TODO add 3rd var for 2nd driver
        self.input_login().send_keys(login)

    def enter_pass(self, passwd): # TODO add 3rd var for 2nd driver
        self.input_pass().send_keys(passwd)

    def login(self):
        self.btn_signin().click()

    def login_error_tooltip(self):
        return self.context.driver.find_element_by_css_selector('.error-field').text

    def validation_error_tooltip(self):
        return self.context.driver.find_element_by_css_selector('.aui-message-error p').text

    def next_button(self):
        return self.context.driver.find_element_by_css_selector('form>input#signin')

    def press_next_button(self):
        self.next_button().click()

    def button_check_disabled(self):
        if self.next_button().get_attribute('disabled'):
            return True
        else:
            return False

    def input_incorrect_email_data(self):
        self.input_login().send_keys("@com")

    def email_input_form_press_enter(self):
        self.input_login().send_keys(Keys.ENTER)

    def password_input_field_press_enter(self):
        self.btn_signin().send_keys(Keys.ENTER)

    def backspace_icon(self):
        return self.context.driver.find_element_by_css_selector('a.back')

    def click_on_backspace_icon(self):
        self.backspace_icon().click()

    def current_url(self):
        return self.context.driver.current_url


