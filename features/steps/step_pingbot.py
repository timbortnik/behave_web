# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we open pingbot room')
def step_impl(context):
    context.lobby_page.open_pingbot_room()


@then('we get mention name name from settings')
def get_full_name(context):
    context.settings_page.navigate()
    context.hipchat_mention_name = context.settings_page.mention_name()


@when('we send message')
def step_impl(context):
    context.lobby_page.send_msg_in_room('/clear')
    context.lobby_page.send_msg_in_room('/ping me with 223')


@then('we receive pingbot reply')
def step_impl(context):
    context.lobby_page.mention_name(context.hipchat_mention_name)
    assert context.lobby_page.check_is_ping('223')

