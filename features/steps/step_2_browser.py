from behave import when, then, given


@given('we are on the login page from 1st')
def step_impl(context):
    context.login_page.navigate()
    assert context.login_page.at()


@given('we are on the login page from 2nd')
def step_impl(context):
    context.login_page.navigate2()
    assert context.login_page.at2()


@when('we enter login on 1st')
def step_impl(context):
    context.login_page.enter_login(context.hipchat_login)
    context.login_page.login()


@when('we enter login on 2nd')
def step_impl(context):
    context.login_page.enter_login_2(context.hipchat_login_2)
    context.login_page.login_2()


@when('we enter pass on 1st')
def step_impl(context):
    context.login_page.enter_pass(context.hipchat_pass)
    context.login_page.login()


@when('we enter pass on 2nd')
def step_impl(context):
    context.login_page.enter_pass_2(context.hipchat_pass_2)
    context.login_page.login_2()


@then('we see Welcome title on 1st')
def step_impl(context):
    assert "Welcome," in context.authorized_page.get_page_head()


@then('we see Welcome title on 2nd')
def step_impl(context):
    assert "Welcome," in context.authorized_page.get_page_head2()



