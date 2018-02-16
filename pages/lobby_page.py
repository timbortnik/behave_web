from .base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from selenium.webdriver.common.keys import Keys
from random import choice
import time


class LobbyPage(Page):
    """
    Chat page
    """

    url = '/chat/lobby'

    def open_pingbot_room(self):
        self.context.driver.get(self.context.base_url + "/chat/room/4383277")
        self.context.wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))

    def find_msg_field(self):
        return self.context.driver.find_element_by_id('hc-message-input')

    def clear_all_messages(self):
        self.context.wait.until(lambda driver: driver.find_element_by_id('hc-message-input'))
        LobbyPage.find_msg_field(self).send_keys('/clear')
        LobbyPage.find_msg_field(self).send_keys(Keys.RETURN)

    def send_msg_in_room(self, msg):
        if "room" in self.context.driver.current_url:
            if msg == '/clear':
                self.clear_all_messages()
                self.context.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'hc-chat-msg')))
            else:
                self.context.wait.until(lambda driver: driver.find_element_by_id('hc-message-input'))
                LobbyPage.find_msg_field(self).send_keys(msg+Keys.RETURN)

    def check_is_ping(self, msg):
        self.context.wait.until(lambda driver: driver.find_element_by_css_selector('.msg-line.msg-line div.msg-line'))
        self.context.wait.until(lambda driver: driver.find_element_by_css_selector('.notification.msg-line'))
        msgs = self.context.driver.find_elements_by_css_selector('.msg-line.msg-line div.msg-line')
        for msg_from_chat in msgs:
            if msg in msg_from_chat.text:
                return True

    room_name = str(randint(1, 999))

    def create_room(self):
        self.find_btn().click()

    def find_btn(self):
        if "lobby" not in self.context.driver.current_url:
            self.context.driver.get(self.context.base_url + "/chat/lobby")
            self.context.wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))
        self.context.wait.until_not(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.closeable')))
        self.context.wait.until_not(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.hc-message.hc-message-info.info.closeable')))
        self.context.wait.until_not(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.hc-message.hc-message-success.success.closeable')))
        self.context.wait.until(
            EC.element_to_be_clickable((By.ID, 'create-room-button')))
        return self.context.driver.find_element_by_id('create-room-button')

    def find_set_name(self):
        self.context.wait.until(EC.element_to_be_clickable((By.ID, 'create-room-name')))
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
        self.context.wait.until_not(EC.element_to_be_clickable((By.XPATH, '//*[@class="aui-dialog2-header-main"]')))

    def get_room_url(self):
        global room_url
        self.context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".hc-page-header-topic")))
        room_url = self.context.driver.current_url.split("/")[(len(self.context.driver.current_url.split("/"))) - 1]

    def find_add_member(self):
        return self.context.driver.find_element_by_xpath('//*[@class="hc-glance clickable"]')

    def room_actions_button(self):
        self.context.wait.until_not(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, '.hc-message.hc-message-success.success.closeable')))
        return self.context.driver.find_element_by_id('room-actions-btn')

    def click_add_member(self):
        self.room_actions_button().click()
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@title="Invite People"]')))
        self.context.driver.find_element_by_xpath('//a[@title="Invite People"]').click()

    def send_invite(self):
        self.context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#s2id_invite-users-people')))
        self.context.driver.find_element_by_css_selector('#s2id_invite-users-people').click()
        self.context.driver.find_element_by_xpath(
            '//div[contains(@class,"select2-drop")]//div[text()="ivan savarin test"]').click()
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text() = "Invite people"]')))

    def find_invite(self):
        return self.context.driver.find_element_by_xpath('//button[text()="Invite people"]')

    def invite(self):
        self.find_invite().click()

    def open_created_room(self):
        self.context.driver.get(self.context.base_url + "/chat/room/" + room_url)
        self.context.wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))

    def accept_invite(self):
        self.open_created_room()
        self.context.driver.find_element_by_id('hc-message-input').send_keys('@all', Keys.RETURN, Keys.RETURN)
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@class="msg-line"]')))

    def delete_room(self):
        self.open_created_room()
        self.room_actions_button().click()
        self.context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.delete-room-action')))
        self.context.driver.find_element_by_css_selector('.delete-room-action').click()
        self.context.wait.until(EC.visibility_of_element_located((By.XPATH, '//button[text()="Delete room"]')))
        self.context.driver.find_element_by_xpath('//button[text()="Delete room"]').click()
        # This sleep we need after deleting, because browser should send data about action to back-end
        time.sleep(1)
        self.open_created_room()
        self.context.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.hc-message.hc-message-warning.warning.closeable')))
        if self.context.driver.find_element_by_css_selector(".hc-message.hc-message-warning.warning.closeable"):
            return True

    def open_alias_room(self):
        self.find_alias_room().click()

    def find_alias_room(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'status_dropdown')))
        return self.context.driver.find_element_by_xpath("//a[@aria-label='Alias room']")

    def input_comands_in_field(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'hc-message-input')))
        self.clear_all_messages()
        alias_set_string = '/alias set ' + self.context.test_name + ' @TestHenaYamkoviy'
        self.context.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".hc-chat-row.hc-msg-nocolor.hc-msg-message.hc-classic-neue")))
        self.find_input_field().send_keys(alias_set_string)
        self.find_input_field().send_keys(Keys.ENTER)
        self.find_input_field().send_keys(Keys.ENTER)

    def find_input_field(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'hc-message-input')))
        return self.context.driver.find_element_by_id('hc-message-input')

    def find_input_alias(self):
        self.context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.notification.msg-line')))
        return self.context.driver.find_elements_by_css_selector('.notification.msg-line')

    def get_text_from_alias_bot(self):
        for data in self.find_input_alias():
            for word in data.text.split():
                if self.context.test_name in word:
                    return True

    def chat_adding_alias(self):
        self.input_comands_in_field()
        return self.get_text_from_alias_bot()

    def random_click(self):
        self.context.wait.until(EC.presence_of_element_located((By.ID, 'status_dropdown')))
        self.find_lobby_page_filter().click()

    def find_lobby_page_filter(self):
        self.context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".aui-page-header")))
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Filter']")))
        return self.context.driver.find_element_by_xpath("//input[@placeholder='Filter']")

    def open_alias_menu(self):
        self.find_plus_button().click()

    def click_for_focus_near_plus_button(self):
        self.context.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea#hc-message-input')))
        self.context.driver.find_element_by_css_selector('textarea#hc-message-input').click()

    def find_plus_button(self):
        self.click_for_focus_near_plus_button()
        self.context.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.hc-dropdown>button#input_actions_dropdown-trigger')))
        return self.context.driver.find_element_by_css_selector('div.hc-dropdown>button#input_actions_dropdown-trigger')

    def open_menu(self):
        self.find_button_in_dropdown_menu().click()

    def find_button_in_dropdown_menu(self):
        self.context.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@data-addon_key="hc-alias"]')))
        return self.context.driver.find_element_by_xpath('//a[@data-addon_key="hc-alias"]')

    def focus_at_alias_config_window(self):
        time.sleep(3)
        return self.context.wait.until(EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, 'hc-addon-iframe')))

    def open_alias_config(self):
        self.context.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div>div>.aui-button.aui-button-link')))
        self.context.driver.find_element_by_css_selector('div>div>.aui-button.aui-button-link').click()

    def put_data_into_the_frame(self):
            self.open_alias_config()
            self.input_data_in_alias_form()
            self.input_data_in_alias_name_form()

    def input_data_in_alias_form(self):
        self.find_alias_form().send_keys("@test")

    def find_alias_form(self):
        self.context.wait.until(EC.presence_of_element_located((By.NAME, 'alias')))
        return self.context.driver.find_element_by_name('alias')

    def input_data_in_alias_name_form(self):
        self.find_form_name().send_keys('TestHenaYamkoviy')
        self.context.wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="TestHenaYamkoviy"]')))
        self.adding_data_in_alias_name_form()

    def adding_data_in_alias_name_form(self):
        self.find_form_name().send_keys(Keys.ARROW_DOWN)
        self.find_form_name().send_keys(Keys.ARROW_DOWN)
        self.find_form_name().send_keys(Keys.ENTER)
        self.find_form_name().send_keys(Keys.ENTER)

    def find_form_name(self):
        return self.context.driver.find_element(By.CSS_SELECTOR, 'div.Select-input>input')

    def find_added_element(self):
        self.context.wait.until(
            lambda driver: self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions'))
        table = self.context.driver.find_elements_by_css_selector('.aui>.aliases>.alias>.mentions')

        result = False
        for element in table:
            if element.text == "@TestHenaYamkoviy":
                result = True
        return result

    def alias_delete_icon(self):
        self.context.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.aui-icon.aui-icon-small.aui-iconfont-delete.delete")))
        return self.context.driver.find_elements_by_css_selector('a.aui-icon.aui-icon-small.aui-iconfont-delete.delete')

    def click_alias_delete_icon(self):
        for delete in self.alias_delete_icon():
            delete.click()

    def invite_team_form(self):
        # lambda is important. EC causes fails
        self.context.wait.until(lambda driver: driver.find_element_by_id('status_dropdown'))
        self.context.wait.until(lambda driver: driver.find_element_by_xpath('//a[text()="Invite your team"]'))
        self.context.driver.find_element_by_xpath('//a[text()="Invite your team"]').click()
        # sleep is needed to switch to the iframe. Without sleep it works faster than iframe opens
        time.sleep(3)
        self.context.wait.until(lambda driver: driver.find_element_by_id('invite-users-frame'))
        self.context.driver.switch_to_frame(self.context.driver.find_element_by_id('invite-users-frame'))

    def invite_team_email_input(self):
        self.context.wait.until(lambda driver: driver.find_element_by_id('email_input'))
        for add_email_try in range(0, 3):
            email = 'test' + str(randint(0, 999)) + '@send22u.info'
            self.context.driver.find_element_by_id('email_input').send_keys(email, Keys.ENTER)

    def delete_email_from_list(self):
        self.context.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Remove"]')))
        delete_buttons = self.context.driver.find_elements_by_xpath('//a[text()="Remove"]')
        choosen_but = choice(delete_buttons)
        choosen_but.click()
        self.context.wait.until_not(EC.visibility_of_element_located((By.XPATH, str(choosen_but))))

    def click_send_invite(self):
        self.context.driver.find_element_by_id('btn_send_invites').click()

    def success_invite_message(self):
        try:
            self.context.driver.find_element_by_id('email_sent_image')
            self.context.driver.find_element_by_xpath('//a[text()="Done"]').click()
            return self.context.driver.find_element_by_xpath('//h2').text
        except:
            return "Invites sent"
