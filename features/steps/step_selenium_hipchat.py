#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Based on ``behave tutorial``
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then

#
# HipChat
#

@given('we are on HipChat home page')
def step_impl(context):
    context.home_page.navigate()
    assert context.home_page.at()

@when('we proceed to the Login Page')
def step_impl(context):
    context.home_page.to_login_page()
    assert context.login_page.at()

@when('we login with valid credentials')
def step_impl(context):
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()
    pass

@then('we see welcome title')
def step_impl(context):
    assert "Welcome," in context.authorized_page.get_page_head()

