# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we are on Lobby Page')
def step_impl(context):
    context.lobby_page.navigate()


@then('we open pingbot room')
def step_impl(context):
    context.lobby_page.open_rooms_list()
    context.lobby_page.open_room_by_name('Pingbot room')


@when('we send message')
def step_impl(context):
    context.lobby_page.room_send_msg('/clear')
    context.lobby_page.room_send_msg('/ping me with 223')


@then('we receive pingbot reply')
def step_impl(context):
    assert context.lobby_page.check_is_ping('223')
