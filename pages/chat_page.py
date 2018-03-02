# -*- coding: UTF-8 -*-

from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import listdir
import os
import  time
import random


class ChatPage(Page):

    """
    Chat page
    """

    url = '/chat'



    def open_home_room(self):
        self.set_home_room().click()

    def set_home_room(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'status_dropdown')))
        xpath = "//a[@aria-label='"+ self.context.hipchat_full_name + "']"
        return self.context.driver.find_element_by_xpath(xpath)


    def upload_attach(self):
        img_path = os.getcwd() + '/swap/Selenium.txt'
        attach = self.context.driver.find_element_by_id("fileInput")
        attach.send_keys(img_path)
        unique_name = 'test_' + str(random.random())
        self.context.driver.find_element_by_id("hc-message-input").send_keys(unique_name, Keys.ENTER)
        self.context.wait.until(lambda driver: driver.find_element_by_css_selector('span.description'))
        xpath_uname = "//span[@class='description'][text()='" + unique_name + "']"
        self.context.wait.until(lambda driver: driver.find_element_by_xpath(xpath_uname))


    # def check_is_attach(self, msg):
    #     self.context.wait.until(lambda driver: driver.find_element_by_css_selector('span.description'))
    #     xpath2 = "//span[@class='description'][text()="+ self.context.unique_name + "']"
    #     if self.context.driver.find_element_by_xpath(xpath2):
    #         msgs = self.context.driver.find_elements_by_css_selector('.msg-line.msg-line div.msg-line')
    #         for msg_from_chat in msgs:
    #             if msg == msg_from_chat.text:
    #                 return True

    # def click_add_attach(self):
    #     #self.context.driver.find_element_by_id('submit_emoticon').click()
    #     self.context.driver.find_element_by_id('hc-message-input').click()
