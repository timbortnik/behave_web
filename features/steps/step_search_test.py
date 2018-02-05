# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then


@given('we open search page')
def step_impl(context):
    context.search_page.navigate()


@then('we input data in top search form')
def step_impl(context):
    context.search_page.input_in_search_top_form()


@when('we check data from middle search')
def step_impl(context):
    assert context.search_page.check_data_from_middle_form()


@when('we input correct data in middle search')
def step_impl(context):
    context.search_page.input_correct_data()


@then('we check search answer')
def step_impl(context):
    assert context.search_page.check_search_answer()
