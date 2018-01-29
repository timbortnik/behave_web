# -*- coding: UTF-8 -*-

from .base_page import Page


class AuthorizedPage(Page):
    """
    Start page for logged in user
    """

    url = '/home'

    def label_page_head(self):
        return self.context.driver.find_element_by_css_selector("div.aui-page-header-main > h1")

    def get_page_head(self):
        return self.label_page_head().text

    def enter_app(self):
        self.find_enter_btn().click()
        self.context.wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))

    def find_enter_btn(self):
        return self.context.driver.find_element_by_xpath('//*[@id="content"]/div/div/div/div[1]/div/a')
