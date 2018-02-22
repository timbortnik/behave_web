# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then


@when('we create new alias in chat')
def step_impl(context):

    context.lobby_page.navigate(context.driver)
    context.lobby_page.random_click()
    context.lobby_page.open_alias_room()
    assert context.lobby_page.chat_adding_alias()


@when('we create new alias with click buttons')
def step_impl(context):
    context.lobby_page.open_alias_menu()
    context.lobby_page.open_menu()
    context.lobby_page.focus_at_alias_config_window()
    context.lobby_page.put_data_into_the_frame()
    assert context.lobby_page.find_added_element()
    context.lobby_page.click_alias_delete_icon()
