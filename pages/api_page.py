from selenium.webdriver.common.keys import Keys
from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ApiPage(Page):
    """
    Start page for API access
    """

    url = '/account/api'

    def token_lable(self):
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'label')))
        return self.context.driver.find_element_by_id('label')

    def create_button(self):
        self.context.wait.until(EC.element_to_be_clickable((By.ID, 'create')))
        return self.context.driver.find_element_by_id('create')

    def create_token_by_scopes(self, scopes):
        self.token_lable().send_keys(scopes)
        self.context.driver.find_element_by_xpath("//option[text()='{0}']".format(scopes)).click()
        self.create_button().click()

    def token(self, scopes):
        token_row_number = 0
        list_of_scope = []
        for scope in self.context.driver.find_elements_by_xpath('//tr//td[@class="scopes"]'):
            token_row_number += 1
            list_of_scope.append(scope)
            if scopes in scope.text:
                token = self.context.driver.find_element_by_xpath(
                    ('//tr[{0}]//td[@class="token"]'.format(token_row_number)))
                return token.text
        if scopes not in list_of_scope:
            self.create_token_by_scopes(scopes)
            token = self.context.driver.find_element_by_xpath\
                ('//tr[{0}]//td[@class="token"]'.format((token_row_number)+1))
            self.context.token = token.text

    def create_new_token(self):
        self.context.driver.find_element_by_id('label').click()
        self.context.driver.find_element_by_id('label').send_keys('test')
        self.context.driver.find_element_by_id('create').click()

    def check_token_by_name(self, token_name):
        for i in self.context.driver.find_elements_by_css_selector('#tokens tbody  tr.data'):
            if i.find_element_by_css_selector('td span.editable').text == token_name:
                return i.find_element_by_css_selector('td.token').text

    def room_manage_token(self):
        token_row_number = 0
        for scope in self.context.driver.find_elements_by_xpath('//tr//td[@class="scopes"]'):
            token_row_number += 1
            if scope.text == 'Manage Rooms':
                token = self.context.driver.find_element_by_xpath(
                    ('//tr[{0}]//td[@class="token"]'.format(token_row_number)))
                return token.text
