# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import then
from helpers.datetime import Date

@then('we create room by name')
def step_impl(context):
    global room_name
    room_name = Date.get_date_time()
    context.lobby_page.create_room_by_name(room_name)


@then('we open created room')
def step_impl(context):
    context.lobby_page.open_rooms_list()
    assert context.lobby_page.open_room_by_name(room_name)
