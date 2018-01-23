# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then


@when('we enter incorrect login')
def step_impl(context):
    context.login_page.enter_login(context.hipchat_login + 'incorrect')
    context.login_page.login()
    pass


@then('we see incorrect login tooltip')
def step_impl(context):
    assert 'We don\'t recognize that email address' in context.login_page.login_error_tooltip()


@when('we enter not valid login')
def step_impl(context):
    context.login_page.enter_login(context.hipchat_login + ' invalid')
    context.login_page.login()
    pass


@then('we see login validation tooltip')
def step_impl(context):
    assert 'Email address is not valid' in context.login_page.validation_error_tooltip()


@when('we enter incorrect password')
def step_impl(context):
    context.login_page.enter_pass(context.hipchat_pass + 'incorrect')
    context.login_page.login()
    pass


@then('we see password validation tooltip')
def step_impl(context):
    assert 'Invalid email and/or password!' in context.login_page.validation_error_tooltip()
