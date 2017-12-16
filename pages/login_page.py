# -*- coding: UTF-8 -*-

from .base_page import Page


class LoginPage(Page):
    
    """
    Login form 
    """

    url = '/sign_in'

    def input_login(self):
        return self.context.driver.find_element_by_id("email")

    def input_pass(self):
        return self.context.driver.find_element_by_id("password")

    def btn_signin(self):
        return self.context.driver.find_element_by_id("signin")

    def enter_login(self, login):
        self.input_login().send_keys(login)

    def enter_pass(self, passwd):
        self.input_pass().send_keys(passwd)

    def login(self):
        self.btn_signin().click()
