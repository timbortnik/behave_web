from behave import given, when, then


@given('we are on Hipchat People Page')
def step_impl(context):
    context.authorized_page.switch_to_people()

@when('we show only admins')
def step_impl(context):
    context.people_page.show_admins_only()

@when('we show all users')
def step_impl(context):
    context.people_page.show_all_users()

@then('we see all users on page')
def step_impl(context):
    context.people_page.we_see_all_users()

@then('we filter data')
def step_impl(context):
    context.people_page.we_filter_user_by_name()
    context.people_page.we_filter_incorrect_data()
