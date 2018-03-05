# -*- coding: UTF-8 -*-

from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import random


class ChatPage(Page):

    """
    Chat page
    """

    url = '/chat'
    unique_name = 'test_' + str(random.random())


    def open_home_room(self):
        self.set_home_room().click()

    def set_home_room(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'status_dropdown')))
        xpath = "//a[@aria-label='" + self.context.hipchat_full_name + "']"
        return self.context.driver.find_element_by_xpath(xpath)


    def upload_attach(self):
        img_path = os.getcwd() + '/swap/Selenium.txt'
        attach = self.context.driver.find_element_by_id("fileInput")
        attach.send_keys(img_path)
        self.context.driver.find_element_by_id("hc-message-input").send_keys(self.unique_name, Keys.ENTER)
        xpath_uname = "//span[@class='description'][text()='" + self.unique_name + "']"
        self.context.wait.until(lambda driver: driver.find_element_by_xpath(xpath_uname))

    def check_attach_by_name(self):
        print(self.unique_name)
        for i in self.context.driver.find_elements_by_css_selector('div.hc-chat-msg'):
            if i.find_element_by_css_selector('span.description').text == self.unique_name:
                return i.find_element_by_css_selector('div.file-meta').text
