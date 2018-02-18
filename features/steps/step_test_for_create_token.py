from behave import given, when, then

@given('we are create token')
def step_impl(context):
    context.api_page.navigate()
    context.login_page.enter_pass(context.hipchat_pass)
    context.settings_page.api_submit()
    context.api_page.room_manage_token()

