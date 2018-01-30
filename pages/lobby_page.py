from .base_page import Page


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

    def find_element_by_username(self, username):
        divs = self.context.driver.find_elements_by_class_name('hc-lobby-list-item')
        for div in divs:
            if div.find_element_by_css_selector('div:nth-child(2)>span:nth-child(1)').text == username:
                return div
        return False

    @staticmethod
    def find_ico_in_div(div):
        return div.find_element_by_css_selector(
            '.hc-lobby-list-item>.hc-lobby-list-icon>span>span:nth-child(2)>svg>use')
