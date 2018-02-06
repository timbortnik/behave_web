from behave import when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from helpers.icon_in_div_changed import IconInDivChanged
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


FULL_NAME = None
driver = webdriver.Chrome
status_shortcuts = {'available': 'icon-avail',
                    'away': 'icon-xa',
                    'do not disturb': 'icon-dnd'}


def change_full_name(name):
    global FULL_NAME
    FULL_NAME = name


@when('we get full user name from settings')
def get_full_name(context):
    global FULL_NAME
    FULL_NAME = context.settings_page.full_name()


@when('we are in chat window')
def step_impl1(context):
    context.lobby_page.navigate()


@then('we change status to "away"')
def stat_away(context):
    context.wait.until(ec.presence_of_element_located((By.ID, 'status_dropdown')))
    context.lobby_page.click_dropdown()
    context.lobby_page.click_away()
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(FULL_NAME)
    status_str = wait.until(IconInDivChanged(div, status_shortcuts['available']))
    assert status_shortcuts['away'] in status_str


@then('we change status to "do not disturb"')
def stat_dnd(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_do_not_disturb()
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(FULL_NAME)
    status_str = wait.until(IconInDivChanged(div, status_shortcuts['away']))
    assert status_shortcuts['do not disturb'] in status_str


@then('we change status to "available"')
def stat_available(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_available()
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(FULL_NAME)
    status_str = wait.until(IconInDivChanged(div, status_shortcuts['do not disturb']))
    assert status_shortcuts['available'] in status_str
