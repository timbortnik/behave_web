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



    # def set_attach_name(self):
    #     self.context.wait.until(EC.visibility_of_element_located((By.ID, 'hc-message-input')))
    #     self.context.driver.find_element_by_id('hc-message-input').send_keys('test')

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
        #time.sleep(7)
        #self.context.wait.until_not(EC.visibility_of_element_located((By.ID, "hc-chat-actions")))

        unique_name = 'test' + str(random.random())


        self.context.driver.find_element_by_id("hc-message-input").send_keys(unique_name, Keys.ENTER)
        #self.context.wait.until_not(EC.presence_of_element_located((By.ID, "hc-chat-actions")))
        time.sleep(2)

        # for i in self.context.driver.find_elements_by_css_selector('div.hc-chat-msg'):
        #     if i.find_element_by_css_selector('span.description').text == unique_name:
        #         return i.find_element_by_css_selector('div.file-meta').text

    # def click_add_attach(self):
    #     #self.context.driver.find_element_by_id('submit_emoticon').click()
    #     self.context.driver.find_element_by_id('hc-message-input').click()
