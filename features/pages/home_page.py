# -*- coding: UTF-8 -*-

from base_page import Page

class HomePage(Page):

    url = '/'

    def link_login(self):
        return self.context.driver.find_element_by_link_text('Log in')

    def to_login_page(self):
        self.link_login().click()
