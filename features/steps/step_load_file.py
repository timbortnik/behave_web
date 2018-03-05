from behave import given, when, then


@given("we are on Hipchat chat Page")
def step_impl(context):
    context.chat_page.navigate()
    context.chat_page.set_home_room()
    context.chat_page.open_home_room()

@when('we click Attachment')
def step_impl(context):
    context.chat_page.upload_attach()

@then('we see new file')
def step_impl(context):
    assert "Selenium.txt" in context.chat_page.check_attach_by_name()
