# -*- coding: UTF-8 -*-

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import when, then


@when('we enter incorrect login')
def step_impl(context):
    context.login_page.enter_login(context.driver, context.hipchat_login + 'incorrect')
    context.login_page.login(context.driver)
    pass


@then('we see incorrect login tooltip')
def step_impl(context):
    assert 'We don\'t recognize that email address' in context.login_page.login_error_tooltip()


@when('we enter not valid login')
def step_impl(context):
    context.login_page.enter_login(context.driver, context.hipchat_login + ' invalid')
    context.login_page.login(context.driver)
    pass


@then('we see login validation tooltip')
def step_impl(context):
    assert 'Email address is not valid' in context.login_page.validation_error_tooltip()


@when('we enter incorrect password')
def step_impl(context):
    context.login_page.enter_pass(context.driver, context.hipchat_pass + 'incorrect')
    context.login_page.login(context.driver)
    pass


@then('we see password validation tooltip')
def step_impl(context):
    assert 'Invalid email and/or password!' in context.login_page.validation_error_tooltip()


@when('we check disabled next button')
def step_impl(context):
    context.login_page.input_incorrect_email_data(context.driver)
    context.login_page.press_next_button()
    assert context.login_page.button_check_disabled()


@then('we check backspace icon')
def step_impl(context):
    context.login_page.enter_login(context.driver, context.hipchat_login)
    context.login_page.email_input_form_press_enter(context.driver)
    context.login_page.click_on_backspace_icon()
    assert '/login' in context.login_page.current_url()


@when('we check logining with press Enter')
def step_impl(context):
    context.login_page.enter_login(context.driver, context.hipchat_login)
    context.login_page.email_input_form_press_enter(context.driver)
    context.login_page.enter_pass(context.driver, context.hipchat_pass)
    context.login_page.password_input_field_press_enter()
    assert "Welcome," in context.authorized_page.get_page_head(context.driver)
