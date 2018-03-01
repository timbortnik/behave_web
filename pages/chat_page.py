# -*- coding: UTF-8 -*-

from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from os import listdir
import os
import  time


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
        #self.context.driver.find_element_by_css_selector(".hc-attach").click()
        attach = self.context.driver.find_element_by_id("fileInput")
        #attach.click()
        attach.send_keys(img_path)
        time.sleep(3)
        self.context.driver.find_element_by_id("hc-message-input").send_keys(Keys.ENTER)
        #self.context.driver.find_element_by_css_selector(".hc-attach").send_keys(self.img_path)
        #self.context.driver.find_element_by_css_selector(".hc-attach").send_keys("D:\\repository\\behave_web\\swap\\7z1801.exe")
        #self.driver.find_element_by_css_selector('input[type="file"]').clear()
        #self.driver.find_element_by_css_selector('input[type="file"]').send_keys(self.img_path)
        #self.context.driver.get(self.img_path)
        #self.context.driver.post(self.img_path)


    def click_add_attach(self):
        #self.context.driver.find_element_by_id('submit_emoticon').click()
        self.context.driver.find_element_by_id('hc-message-input').click()
