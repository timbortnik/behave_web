from behave import when, then
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


driver = webdriver.Chrome


@when('we get full user name from settings')
def get_full_name(context):
    context.hipchat_full_name = context.settings_page.full_name()


@when('we are in chat window')
def step_impl1(context):
    context.lobby_page.navigate()


@then('we change status to "away"')
def stat_away(context):
    context.wait.until(ec.presence_of_element_located((By.ID, 'status_dropdown')))
    context.lobby_page.click_dropdown()
    context.wait.until(ec.presence_of_element_located((By.ID, context.lobby_page.status_shortcuts['away'])))
    context.lobby_page.click_away()
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(context.hipchat_full_name)
    status_str = wait.until(context.lobby_page.lobby_icon_changed(context.lobby_page, div, context.lobby_page.status_shortcuts['available']))
    assert context.lobby_page.status_shortcuts['away'] in status_str


@then('we change status to "do not disturb"')
def stat_dnd(context):
    context.lobby_page.click_dropdown()
    context.wait.until(ec.presence_of_element_located((By.ID, context.lobby_page.status_shortcuts['do not disturb'])))
    context.lobby_page.click_do_not_disturb()
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(context.hipchat_full_name)
    status_str = wait.until(context.lobby_page.lobby_icon_changed(context.lobby_page, div, context.lobby_page.status_shortcuts['away']))
    assert context.lobby_page.status_shortcuts['do not disturb'] in status_str


@then('we change status to "available"')
def stat_available(context):
    context.lobby_page.click_dropdown()
    context.wait.until(ec.presence_of_element_located((By.ID, context.lobby_page.status_shortcuts['away'])))
    context.lobby_page.click_available()
    wait = WebDriverWait(driver, 10)
    div = context.lobby_page.find_element_by_username(context.hipchat_full_name)
    status_str = wait.until(context.lobby_page.lobby_icon_changed(context.lobby_page, div, context.lobby_page.status_shortcuts['do not disturb']))
    assert context.lobby_page.status_shortcuts['available'] in status_str
