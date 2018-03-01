from behave import then, given
from selenium import webdriver

driver = webdriver.Chrome


@then('we get full user name from settings')
def get_full_name(context):
    context.hipchat_full_name = context.settings_page.full_name()


@given('we are in chat window')
def step_impl1(context):
    context.lobby_page.navigate(context.driver)


@given('we are in chat window on 2nd user\'s lobby')
def step_impl1(context):
    context.lobby_page.navigate(context.driver_2)


@then('we change status to "away"')
def stat_away(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_away()
    # time.sleep(5)



@then('we check changing status to "away" on 2nd user\'s lobby')
def check_stat_away(context):
    # print(context.hipchat_full_name)
    context.lobby_page.find_element_by_username(context.driver_2, context.hipchat_full_name)
    context.wait.until(context.lobby_page.LobbyIconChanged(
        context.lobby_page, context.lobby_page.status_shortcuts['available']))
    # print('hhju')
    assert context.lobby_page.status_shortcuts['away'] in context.lobby_page.status_str


@then('we change status to "do not disturb"')
def stat_dnd(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_do_not_disturb()


@then('we check changing status to "do not disturb" on 2nd user\'s lobby')
def check_stat_dnd(context):
    context.lobby_page.find_element_by_username(context.driver_2, context.hipchat_full_name)
    context.wait.until(context.lobby_page.LobbyIconChanged(
        context.lobby_page, context.lobby_page.status_shortcuts['away']))
    assert context.lobby_page.status_shortcuts['do not disturb'] in context.lobby_page.status_str


@then('we change status to "available"')
def stat_available(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_available()


@then('we check changing status to "available" on 2nd user\'s lobby')
def check_stat_available(context):
    context.lobby_page.find_element_by_username(context.driver_2, context.hipchat_full_name)
    context.wait.until(context.lobby_page.LobbyIconChanged(
        context.lobby_page, context.lobby_page.status_shortcuts['do not disturb']))
    assert context.lobby_page.status_shortcuts['available'] in context.lobby_page.status_str
