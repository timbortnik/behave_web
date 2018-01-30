from behave import when, then


# from features.steps.step_checking_status import FULL_NAME


@when("we compare name of current user with name on Welcome title")
def step_impl(context):
    assert "Aned4enko" in context.authorized_page.get_page_head()


@when("we move to user page (on People Page)")
def step_impl(context):
    context.people_page.open_user_page()


@then("we compare name of current user with name in user page")
def step_impl(context):
    assert "Aned4enko" in context.people_page.label_page_head_on_user_page()
