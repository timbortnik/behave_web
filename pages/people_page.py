from selenium.webdriver.common.keys import Keys
from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
import string


class PeoplePage(Page):

    url = '/people'
    admins = ['Tim Bortnik']

    def show_admins_only(self):
        self.context.driver.find_element_by_id('show_admins_only').click()
        # TODO maybe we can find more automatisation way to get admins name
        admin = self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Tim Bortnik")]')))
        if admin:
            # TODO remove print's, we need to make test which fails or not fails
            print('\tAdmins found correctly')
            pass
        else:
            print("Admins not found")

    def show_all_users(self):
        self.context.driver.find_element_by_id('show_all_users').click()

    def we_see_all_users(self):
        # TODO this is check that we see all users?
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//ol[@class="aui-nav-pagination"]')))

    def we_filter(self):
        # TODO what kind of filter we are?) Please provide more informative name of method
        correct_data = "ivan"
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'search_query')))
        form = self.context.driver.find_element_by_id('search_query')
        form.send_keys(correct_data, Keys.RETURN)
        if self.context.driver.find_element_by_xpath('//a[contains(text(), "' + correct_data + '")]'):
            self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="Clear search"]')))
            self.context.driver.find_element_by_xpath('//span[@title="Clear search"]').click()
            pass
            # TODO looks like redundant
        else:
            # TODO remove prints, maybe you want to use except to raise error?
            print("Correct data was not filtered")

    def we_filter_incorrect(self):
        # TODO Please provide more informative name of method
        # TODO I don't sure, but IDE tell that "n" variable didn't use, please double check line 50.
        incorrect_data = ''.join([random.choice(string.ascii_letters) for n in range(10)])
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'search_query')))
        # TODO You should to make this variable as separated method
        form = self.context.driver.find_element_by_id('search_query')
        form.send_keys(incorrect_data, Keys.RETURN)
        # TODO If it possible remove "try"
        try:
            if not self.context.driver.find_element_by_xpath('//a[contains(text(), "' + incorrect_data + '")]'):
                self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="Clear search"]')))
                self.context.driver.find_element_by_xpath('//span[@title="Clear search"]').click()
                # TODO looks like redundant
                pass
        except:
            # TODO remove prints
            print("\tData filtered correctly. Incorrect result was not displayed")
            self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@title="Clear search"]')))
            self.context.driver.find_element_by_xpath('//span[@title="Clear search"]').click()
# TODO KISS principle, code hard to read