from behave import when


@when("we compare name of current user with name on Welcome title")
def step_impl(context):
    assert 'Aned4enko_test' in context.authorized_page.get_page_head()
