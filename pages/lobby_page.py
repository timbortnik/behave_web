# -*- coding: UTF-8 -*-

from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from random import randint


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

    # @staticmethod
    # def check_ico(div):
    #     return div.find_element_by_css_selector(
    #         '.hc-lobby-list-item>.hc-lobby-list-icon>span>span:nth-child(2)>svg>use').get_attribute(
    #         'xlink:href')

    room_name = str(randint(1, 999))

    def create_room(self):
        self.find_btn().click()
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'create-room-name')))

    def find_btn(self):
        self.context.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Create a room"]')))
        return self.context.driver.find_element_by_xpath('//span[text()="Create a room"]')

    def find_set_name(self):
        return self.context.driver.find_element_by_id('create-room-name')

    def set_name(self):
        self.find_set_name().send_keys(LobbyPage.room_name)
        self.context.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Create room"]')))

    def find_create_btn(self):
        self.context.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Create room"]')))
        return self.context.driver.find_element_by_xpath('//button[text()="Create room"]')

    def click_create_room(self):
        self.find_create_btn().click()
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="hc-glance clickable"]')))

    def find_add_member(self):
        return self.context.driver.find_element_by_xpath('//*[@class="hc-glance clickable"]')

    def click_add_member(self):
        import time
        time.sleep(3)
        self.context.driver.find_element_by_id('room-actions-btn').click()
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Invite People"]')))
        self.context.driver.find_element_by_xpath('//a[text()="Invite People"]').click()

    def send_invite(self):
        self.context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s2id_invite-users-people')))
        self.context.driver.find_element_by_css_selector('#s2id_invite-users-people').click()
        self.context.driver.find_element_by_xpath(
            '//div[contains(@class,"select2-drop")]//div[text()="ivan savarin test"]').click()
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Invite people"]')))

    def find_invite(self):
        return self.context.driver.find_element_by_xpath('//*[@id="invite-users-dialog"]/footer/div[1]/button[1]')

    def invite(self):
        self.find_invite().click()

    def accept_invite(self):
        from selenium.webdriver.common.keys import Keys
        try:
            room_xpath = '//div[contains(@class,"hc-lobby-panel-content")]//span[text()="' + LobbyPage.room_name + '"]'
            self.context.driver.find_element_by_xpath(room_xpath).click()
            self.context.driver.find_element_by_id('hc-message-input').send_keys('@all', Keys.RETURN, Keys.RETURN)
            self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="msg-line"]')))
        except:
            self.context.driver.find_element_by_id('hc-message-input').send_keys('@all', Keys.RETURN, Keys.RETURN)
            self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="msg-line"]')))

    def delete_room(self):
        try:
            room_xpath = '//div[contains(@class,"hc-lobby-panel-content")]//span[text()="' + LobbyPage.room_name + '"]'
            self.context.driver.find_element_by_xpath(room_xpath).click()
            self.context.driver.find_element_by_id('room-actions-btn').click()
            self.context.driver.find_element_by_css_selector('.delete-room-action').click()
            self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Delete room"]')))
            self.context.driver.find_element_by_xpath('//button[text()="Delete room"]').click()
        except:
            self.context.driver.find_element_by_id('room-actions-btn').click()
            self.context.driver.find_element_by_css_selector('.delete-room-action').click()
            self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Delete room"]')))
            self.context.driver.find_element_by_xpath('//button[text()="Delete room"]').click()
