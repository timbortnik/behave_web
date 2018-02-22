# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we are on search page')
def step_impl(context):
    context.search_page.navigate(context.driver)


@then('we input data in top search form')
def step_impl(context):
    context.search_page.input_in_search_top_form()


@when('we check data from middle search')
def step_impl(context):
    assert context.search_page.check_data_from_middle_form()


@given('we get correct data')
def step_impl(context):
    context.settings_page.navigate(context.driver)
    context.search_page.mention_name()


@when('we input correct data in middle search')
def step_impl(context):
    context.search_page.navigate(context.driver)
    context.search_page.input_correct_data(context.mention_name)


@then('we check search answer')
def step_impl(context):
    assert context.search_page.check_search_answer(context.mention_name)


@when('we generate and input incorrect data')
def step_impl(context):
    context.search_page.generate_and_input_incorect_data(context.mention_name)


@then('we check incorrect data')
def step_impl(context):
    assert context.search_page.check_no_result_text()
