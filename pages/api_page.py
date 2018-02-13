# -*- coding: UTF-8 -*-
from selenium.webdriver.common.keys import Keys
from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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

    def room_manage_token(self):
        # token = self.context.driver.find_elements_by_xpath('//tr[1]//td[@class="token"]')
        self.context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'table.aui')))
        table = self.context.driver.find_element_by_xpath("//table[@id='tokens']")
        table_info = table.text.split()
        for i in table_info:
            if "Manage" in i:
                row_num = table_info.index(i)
                if table_info[row_num + 1] == "Rooms":
                    token_index = row_num - 2
                    token = table_info[token_index]
        return token


