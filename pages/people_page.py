from selenium.webdriver.common.keys import Keys
from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class PeoplePage(Page):

    url = '/people'
    admins = ['Tim Bortnik', 'Yevhenii Udovychenko']

    def show_admins_only(self):
        self.context.driver.find_element_by_id('show_admins_only').click()
        for admin in self.context.driver.find_elements_by_xpath('//a[@class="name"]'):
            if admin.text in PeoplePage.admins:
                return True
            else:
                raise AssertionError

    def show_all_users(self):
        self.context.driver.find_element_by_id('show_all_users').click()
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//ol[@class="aui-nav-pagination"]')))
        users = self.context.driver.find_elements_by_xpath('//a[@class="name"]')
        all_users = users.split()
        print(all_users)

    def we_see(self):
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//ol[@class="aui-nav-pagination"]')))

    def open_user_page(self):
        self.context.driver.find_element_by_xpath('//a[contains(text(), "Test")]').click()

    def label_page_head_on_user_page(self):
        return self.context.driver.find_element_by_css_selector("div.aui-item > h2").text

    def we_see_all_users(self):
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//ol[@class="aui-nav-pagination"]')))
        all_users =[]
        for user in self.context.driver.find_elements_by_xpath('//a[@class="name"]'):
            all_users.append(user.text)
        return all_users


    def we_filter_user_by_name(self):
        correct_data = "ivan"
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'search_query')))
        form = self.context.driver.find_element_by_id('search_query')
        form.send_keys(correct_data, Keys.RETURN)
        if self.context.driver.find_element_by_xpath('//a[contains(text(), "' + correct_data + '")]'):
            self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="Clear search"]')))
            self.context.driver.find_element_by_xpath('//span[@title="Clear search"]').click()
        else:
            raise AssertionError

    def filter_form(self):
        return self.context.driver.find_element_by_id('search_query')

    def we_filter_incorrect_data(self):
        incorrect_data = ''.join([random.choice(string.ascii_letters) for n in range(10)])
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'search_query')))
        PeoplePage.filter_form(self).send_keys(incorrect_data, Keys.RETURN)
        try:
            if not self.context.driver.find_element_by_xpath('//a[contains(text(), "' + incorrect_data + '")]'):
                self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="Clear search"]')))
                self.context.driver.find_element_by_xpath('//span[@title="Clear search"]').click()
        except:
            self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="Clear search"]')))
            self.context.driver.find_element_by_xpath('//span[@title="Clear search"]').click()
