from behave import when, then, given


@given('we are on Lobby Page')
def step_impl(context):
    context.lobby_page.navigate()


@when('we click Invite your team')
def step_impl(context):
    context.lobby_page.invite_team_form()


@when('we add the emails')
def step_impl(context):
    context.lobby_page.invite_team_email_input()


@when('we delete one email')
def step_impl(context):
    context.lobby_page.delete_email_from_list()


@when('we send invite')
def step_impl(context):
    context.lobby_page.click_send_invite()


@then('we see success message')
def step_impl(context):
    assert 'Invites sent' in context.lobby_page.success_invite_message()
