from behave import when
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from features.icon_in_div_changed import IconInDivChanged
import time

FULL_NAME = None
driver = webdriver.Chrome
status_shortcuts = {'available': 'icon-avail',
                    'away': 'icon-xa',
                    'do not disturb': 'icon-dnd'}


@when('we get full user name from settings')
def get_full_name(context):
    global FULL_NAME
    FULL_NAME = context.settings_page.full_name()


@when('we are in chat window')
def step_impl1(context):
    context.lobby_page.navigate()
    time.sleep(6)
    # self.context.wait.until()


@when('we change status for all available cases')
def step_impl(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_away()
    # time.sleep(1)
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(FULL_NAME)
    status_str = wait.until(IconInDivChanged(div, status_shortcuts['available']))
    print(status_str)
    assert status_shortcuts['away'] in status_str
    context.lobby_page.click_dropdown()
    context.lobby_page.click_do_not_disturb()
    # time.sleep(1)
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(FULL_NAME)
    status_str = wait.until(IconInDivChanged(div, status_shortcuts['away']))
    print(status_str)
    assert status_shortcuts['do not disturb'] in status_str
    context.lobby_page.click_dropdown()
    context.lobby_page.click_available()
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(FULL_NAME)
    status_str = wait.until(IconInDivChanged(div, status_shortcuts['do not disturb']))
    print(status_str)
    assert status_shortcuts['available'] in status_str
    time.sleep(2)
