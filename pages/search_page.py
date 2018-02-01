from .base_page import Page
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .authorized_page import AuthorizedPage


class SearchPage(Page):
    """
    Page search
    """

    url = '/search'

    def search_header_form(self):
        return self.context.driver.find_element_by_css_selector("input.search")

    def input_in_search_top_form(self):
        self.search_header_form().send_keys('sometext')
        self.search_header_form().send_keys(Keys.ENTER)

    def search_middle_form(self):
        return self.context.driver.find_element_by_css_selector("input#q")

    def check_data_from_middle_form(self):
        if "sometext" == self.search_middle_form().get_attribute("value"):
            return True

    def user_name(self):
        return AuthorizedPage.label_page_head(self).text

    def input_correct_data(self):
        self.search_middle_form().clear()
        self.search_middle_form().send_keys(self.user_name().split()[1])
        self.search_middle_form().send_keys(Keys.ENTER)

    def list_with_search_phases(self):
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH,  "//span[@class='highlight']")))
        return self.context.driver.find_elements_by_xpath("//span[@class='highlight']")

    def check_search_answer(self):

        for word_from_search_answer in self.list_with_search_phases():
            if word_from_search_answer.text == self.user_name().split()[1]:
                return True
            else:
                continue
