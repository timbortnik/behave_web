from behave import then, given
from selenium import webdriver


@then('we get full user name from settings')
def get_full_name(context):
    context.hipchat_full_name = context.settings_page.full_name()


@given('we are in chat window')
def step_impl1(context):
    context.lobby_page.navigate()


@then('we change status to "away"')
def stat_away(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_away()
    context.lobby_page.find_element_by_username(context.hipchat_full_name)
    context.wait.until(context.lobby_page.LobbyIconChanged(context.lobby_page, context.lobby_page.status_shortcuts['available']))
    assert context.lobby_page.status_shortcuts['away'] in context.lobby_page.status_str


@then('we change status to "do not disturb"')
def stat_dnd(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_do_not_disturb()
    context.lobby_page.find_element_by_username(context.hipchat_full_name)
    context.wait.until(context.lobby_page.LobbyIconChanged(
        context.lobby_page, context.lobby_page.status_shortcuts['away']))
    assert context.lobby_page.status_shortcuts['do not disturb'] in context.lobby_page.status_str


@then('we change status to "available"')
def stat_available(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_available()
    context.lobby_page.find_element_by_username(context.hipchat_full_name)
    context.wait.until(context.lobby_page.LobbyIconChanged(
        context.lobby_page, context.lobby_page.status_shortcuts['do not disturb']))
    assert context.lobby_page.status_shortcuts['available'] in context.lobby_page.status_str
