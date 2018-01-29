# -*- coding: UTF-8 -*-
from selenium.webdriver.common.keys import Keys

from .base_page import Page


class ApiPage(Page):
    """
    Start page for API access
    """

    url = '/account/api'

    def create_new_token(self):
        self.context.driver.find_element_by_id('label').click()
        self.context.driver.find_element_by_id('label').send_keys('test')
        self.context.driver.find_element_by_id('create').click()

    def check_token_by_name(self, token_name):
        for i in self.context.driver.find_elements_by_css_selector('#tokens tbody  tr.data'):
            if i.find_element_by_css_selector('td span.editable').text == token_name:
                return i.find_element_by_css_selector('td.token').text
