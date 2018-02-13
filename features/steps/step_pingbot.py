# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we open pingbot room')
def step_impl(context):
    context.lobby_page.open_pingbot_room()


@when('we send message')
def step_impl(context):
    context.lobby_page.send_msg_in_room('/clear')
    context.lobby_page.send_msg_in_room('/ping me with 223')

@then('we receive pingbot reply')
def step_impl(context):
    assert context.lobby_page.check_is_ping('223')

