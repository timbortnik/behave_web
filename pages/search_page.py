from .base_page import Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random


class SearchPage(Page):
    """
    Page search
    """

    url = '/search'

    def find_search_header_form(self):
        self.context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search")))
        return self.context.driver.find_element_by_css_selector("input.search")

    def input_in_search_top_form(self):
        self.find_search_header_form().send_keys('sometext')
        self.find_search_header_form().send_keys(Keys.ENTER)

    def search_middle_form(self):
        return self.context.driver.find_element_by_css_selector("input#q")

    def check_data_from_middle_form(self):
        if "sometext" == self.search_middle_form().get_attribute("value"):
            return True

    def mention_name(self):
        self.context.mention_name = self.context.driver.find_element_by_id('mention_name').get_attribute("value")

    def input_correct_data(self, correct_data):
        self.search_middle_form().clear()
        self.search_middle_form().send_keys(correct_data)
        if self.search_middle_form().get_attribute("value") == correct_data:
            pass
        self.search_middle_form().send_keys(Keys.ENTER)

    def list_with_search_phrases(self):
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH,  "//span[@class='highlight']")))
        return self.context.driver.find_elements_by_xpath("//span[@class='highlight']")

    def check_search_answer(self, correct_data):
        for word_from_search_answer in self.list_with_search_phrases():
            if word_from_search_answer.text == correct_data:
                return True
            else:
                continue

    def generate_and_input_incorect_data(self, correct_data):
        incorrect_data = correct_data + str(random.random())
        self.search_middle_form().send_keys(incorrect_data)
        self.search_middle_form().send_keys(Keys.ENTER)

    def check_no_result_text(self):
        self.context.wait.until(EC.presence_of_element_located((By.XPATH, "//section[@id='content']//p")))
        if "No results found." == self.context.driver.find_element_by_xpath("//section[@id='content']//p").text:
            return True