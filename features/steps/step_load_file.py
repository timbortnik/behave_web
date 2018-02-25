from behave import given, when, then


@given("we are on Hipchat chat Page")
def step_impl(context):
    context.chat_page.navigate()


@when('we click Attachment')
def step_impl(context):
    #context.chat_page.go_to_filepicker()
    pass


@step_impl('we upload a file')
def step_impl(context):
    #context.emoticons_page.upload_image_emoticon()
    pass


@step_impl('we click Enter')
def step_impl(context):
    #context.emoticons_page.click_add_emoticon()
    pass


@then('we see new file')
def step_impl(context):
    #context.emoticons_page.wait_if_created()
    pass

