# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we are on Hipchat Lobby Page')
def step_impl(context):
    context.authorized_page.enter_app()


@then('we create a room')
def step_impl(context):
    context.lobby_page.create_room()
    context.lobby_page.set_name()
    context.lobby_page.click_create_room()
    context.lobby_page.get_room_url()


@then('we invite member')
def step_impl(context):
    context.lobby_page.click_add_member()
    context.lobby_page.send_invite()
    context.lobby_page.invite()


@then('we accept the invitation')
def step_impl(context):
    context.lobby_page.accept_invite()


@then('we delete the room')
def step_impl(context):
    assert context.lobby_page.delete_room()

