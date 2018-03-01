from behave import when, then, given


@given('we are on the login page from "{browser}"')
def step_impl(context, browser):
    context.login_page.navigate(context.browsers[browser]['driver'])
    assert context.login_page.at(context.browsers[browser]['driver'])


@when('we enter login on "{browser}"')
def step_impl(context, browser):
    context.login_page.enter_login(context.browsers[browser]['driver'], context.browsers[browser]['login'])
    context.login_page.login(context.browsers[browser]['driver'])


@when('we enter pass on "{browser}"')
def step_impl(context, browser):
    context.login_page.enter_pass(context.browsers[browser]['driver'], context.browsers[browser]['pass'])
    context.login_page.login(context.browsers[browser]['driver'])


@then('we see Welcome title on {browser}')
def step_impl(context, browser):
    assert "Welcome," in context.authorized_page.get_page_head(context.browsers[browser]['driver'])


@given('we are on Hipchat Lobby Page on {browser}')
def step_impl(context, browser):
    context.authorized_page.enter_app(context.browsers[browser]['driver'])


@when('we enter in room from "{browser}"')
def step_impl(context, browser):
    context.lobby_page.open_pingbot_room(context.browsers[browser]['driver'], context.browsers[browser]['wait'])


@when('we send message from "{browser}"')
def step_impl(context, browser):
    context.lobby_page.first_browser_message(context.browsers[browser]['driver'])
