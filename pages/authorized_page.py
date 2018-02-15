# -*- coding: UTF-8 -*-

from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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
        return self.context.driver.find_element_by_xpath('//a[text()="Launch the web app"]')

    def switch_to_people(self):
        self.context.driver.find_element_by_xpath('//a[text()="People"]').click()
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//h2[text()="People"]')))

    def switch_to_emoticons(self):
        self.context.driver.find_element_by_xpath('//a[text()="Emoticons"]').click()
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'drop')))

