# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import then

@then('we open created room')
def step_impl(context):
    context.settings_page.navigate()