from behave import given, when
import time


@given('we are in chat window')
def step_impl(context):
    context.authorized_page.enter_app()
    time.sleep(3)


@when('we change status for all available cases')
def step_impl(context):
    context.lobby_page.click_dropdown()
    context.lobby_page.click_away()
    assert context.lobby_page.find_away_user_status()
    time.sleep(3)
    context.lobby_page.click_dropdown()
    context.lobby_page.click_do_not_disturb()
    assert context.lobby_page.find_do_not_disturb_user_status()
    time.sleep(3)
    context.lobby_page.click_dropdown()
    context.lobby_page.click_available()
    assert context.lobby_page.find_available_user_status()
    time.sleep(3)


# @when('we check status')
# def step_impl(context):
#     assert context.lobby_page.find_away_user_status()

# def step_impl(context):
#     context.authorized_page.navigate()
#     assert context.authorized_page.at()

