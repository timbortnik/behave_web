from behave import given, when, then
import features.steps.step_checking_status as CS


@given('we are on Hipchat People Page')
def step_impl(context):
    context.authorized_page.switch_to_people()


@when("we compare name of current user with name on Welcome title")
def step_impl(context):
    assert CS.FULL_NAME in context.authorized_page.get_page_head()


@when("we move to user page (on People Page)")
def step_impl(context):
    context.people_page.open_user_page()


@then("we compare name of current user with name in user page")
def step_impl(context):
    assert CS.FULL_NAME in context.people_page.label_page_head_on_user_page()
