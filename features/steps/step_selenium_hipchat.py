# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we are on Hipchat Login Page')
def step_impl(context):
    context.login_page.navigate()
    assert context.login_page.at()


@given('we open 2nd browser window')
def step_impl(context):
    context.login_page.navigate2()


@when('we enter login')
def step_impl(context):
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.login()
    pass


@when('we enter password')
def step_impl(context):
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()
    pass


@when('we enter other login')
def step_impl(context):
    context.login_page.enter_login(context.hipchat_login_2)
    context.login_page.login()
    pass


@when('we enter other password')
def step_impl(context):
    context.login_page.enter_pass(context.hipchat_pass_2)
    context.login_page.login()
    pass


@then('we see welcome title')
def step_impl(context):
    assert "Welcome," in context.authorized_page.get_page_head()
