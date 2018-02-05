from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import features.steps.step_checking_status as cs


class PeoplePage(Page):
    url = '/people'
    admins = ['Tim Bortnik']

    def show_admins_only(self):
        self.context.driver.find_element_by_id('show_admins_only').click()
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "Tim Bortnik")]')))

    def show_all_users(self):
        self.context.driver.find_element_by_id('show_all_users').click()
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//ol[@class="aui-nav-pagination"]')))
        users = self.context.driver.find_elements_by_xpath('//a[@class="name"]')
        all_users = users.split()
        print(all_users)

    def we_see(self):
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//ol[@class="aui-nav-pagination"]')))

    def open_user_page(self):
        self.context.driver.find_element_by_xpath('//a[contains(text(), "' + cs.FULL_NAME + '")]').click()

    def label_page_head_on_user_page(self):
        return self.context.driver.find_element_by_css_selector("div.aui-item > h2")

    def get_label_page_head_on_user_page(self):
        return self.label_page_head_on_user_page().text
