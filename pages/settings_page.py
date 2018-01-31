# -*- coding: UTF-8 -*-

from .base_page import Page


class SettingsPage(Page):
    """
    Page for Account settings
    """

    url = '/account'


    def mention_name(self):
        return self.context.driver.find_element_by_id('mention_name').get_attribute('value')

    def full_name(self):
        return self.context.driver.find_element_by_id('name').get_attribute('value')

    def email(self):
        return self.context.driver.find_element_by_id('email').get_attribute('value')

    def api_access(self):
        self.context.driver.find_element_by_link_text('API access').click()

    def api_submit(self):
        self.context.driver.find_element_by_id('submit').click()


    @staticmethod
    def check_if_exist(*args):
        for i in args:
            if len(i) == 0:
                return False
        return True
