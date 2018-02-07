# -*- coding: UTF-8 -*-

from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os


class EmoticonsPage(Page):

    url = '/emoticons'

    def go_to_filepicker(self):
        self.context.driver.find_element_by_id('filepicker').click()

    def set_emoticon_name(self):
        self.context.wait.until(EC.visibility_of_element_located((By.ID, 'shortcut_0')))
        self.context.driver.find_element_by_id('shortcut_0').send_keys('test')

    def upload_image(self):
        img_path = os.getcwd() + '/doc/behave_web.png'
        self.context.driver.find_element_by_id('Filedata_0').send_keys(img_path)

    def click_add_emoticon(self):
        self.context.driver.find_element_by_id('submit_emoticon').click()

    def wait_if_created(self):
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//td[text()="(behaveweb)"]')))

    def delete_emoticon(self):  
        for element in self.context.driver.find_elements_by_xpath('//span[text()="Delete"]'):
            element.click()
            self.context.wait.until(EC.alert_is_present())
            self.context.driver.switch_to.alert.accept()
            self.context.wait.until_not(EC.visibility_of_element_located((By.XPATH, '//td[text()="(behaveweb)"]')))
