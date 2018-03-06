# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import then, step


@step('we are on Account settings Page')
def step_impl(context):
    context.settings_page.navigate(context.driver)


@then('we see filled account settings')
def step_impl(context):
    assert context.settings_page.check_if_exist(context.settings_page.mention_name(),
                                                context.settings_page.email(),
                                                context.settings_page.full_name())
