from behave import when, then, given


@given('we are on the login page from 1st')
def step_impl(context):
    context.login_page.navigate(context.driver)
    assert context.login_page.at(context.driver)


@given('we are on the login page from 2nd')
def step_impl(context):
    context.login_page.navigate(context.driver2)
    assert context.login_page.at(context.driver2)


@when('we enter login on 1st')
def step_impl(context):
    context.login_page.enter_login(context.driver, context.hipchat_login)
    context.login_page.login(context.driver)


@when('we enter login on 2nd')
def step_impl(context):
    context.login_page.enter_login(context.driver2, context.hipchat_login_2)
    context.login_page.login(context.driver2)


@when('we enter pass on 1st')
def step_impl(context):
    context.login_page.enter_pass(context.driver, context.hipchat_pass)
    context.login_page.login(context.driver)


@when('we enter pass on 2nd')
def step_impl(context):
    context.login_page.enter_pass(context.driver2, context.hipchat_pass_2)
    context.login_page.login(context.driver2)


@then('we see Welcome title on 1st')
def step_impl(context):
    assert "Welcome," in context.authorized_page.get_page_head(context.driver)


@then('we see Welcome title on 2nd')
def step_impl(context):
    assert "Welcome," in context.authorized_page.get_page_head(context.driver2)


@given('we are on Hipchat Lobby Page on 1st')
def step_impl(context):
    context.authorized_page.enter_app(context.driver)


@given('we are on Hipchat Lobby Page on 2nd')
def step_impl(context):
    context.authorized_page.enter_app(context.driver2)


@when('we enter in room from 1st')
def step_impl(context):
    context.lobby_page.open_pingbot_room(context.driver, context.wait)


@when('we enter in room from 2nd')
def step_impl(context):
    context.lobby_page.open_pingbot_room(context.driver2, context.wait2)


@when('we send message from 1st')
def step_impl(context):
    context.lobby_page.first_browser_message(context.driver)


@when('we send message from 2nd')
def step_impl(context):
    context.lobby_page.second_browser_answer(context.driver2)


