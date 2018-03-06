from behave import step


@step('we enter the room from "{browser}"')
def step_impl(context, browser):
    context.lobby_page.open_created_room(context.browsers[browser]['driver'], context.browsers[browser]['wait'])
