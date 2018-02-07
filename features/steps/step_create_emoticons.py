from behave import given, when, then

@given("we are on Hipchat Emoticons Page")
def step_impl(context):
    context.authorized_page.switch_to_emoticons()

@when('we go to emoticons constructor')
def step_impl(context):
    context.emoticons_page.go_to_filepicker()

@when('we upload a picture')
def step_impl(context):
    context.emoticons_page.upload_image()

@when('we click "Add emoticon"')
def step_impl(context):
    context.emoticons_page.click_add_emoticon()

@when('we see new emoticon')
def step_impl(context):
    context.emoticons_page.wait_if_created()

@when('we delete emoticon')
def step_impl(context):
    context.emoticons_page.delete_emoticon()
