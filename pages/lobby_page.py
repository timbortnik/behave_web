from .base_page import Page
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LobbyPage(Page):
    """
    Start page for logged in user
    """
    url = '/chat'

    def open_dropdown(self):
        return self.context.driver.find_element_by_id("status_dropdown")

    def click_dropdown(self):
        self.open_dropdown().click()

    def click_away(self):
        return self.context.driver.find_element_by_id('hc-xa').click()

    def click_do_not_disturb(self):
        return self.context.driver.find_element_by_id('hc-dnd').click()

    def click_available(self):
        return self.context.driver.find_element_by_id('hc-avail').click()

    def find_away_user_status(self):
        return self.context.driver.find_element_by_id('icon-xa-selected')

    def find_do_not_disturb_user_status(self):
        return self.context.driver.find_element_by_id('icon-dnd-selected')

    def find_available_user_status(self):
        return self.context.driver.find_element_by_id('icon-available-selected')




