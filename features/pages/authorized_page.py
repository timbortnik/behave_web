# -*- coding: UTF-8 -*-

from base_page import Page

class AuthorizedPage(Page):

    url = '/home'

    def label_page_head(self):
        return self.context.driver.find_element_by_css_selector("div.aui-page-header-main > h1")

    def get_page_head(self):
        return self.label_page_head().text
