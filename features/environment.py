# -*- coding: UTF-8 -*-
"""
before_step(context, step), after_step(context, step)
    These run before and after every step.
    The step passed in is an instance of Step.

before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
    The scenario passed in is an instance of Scenario.

before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
    The feature passed in is an instance of Feature.

before_tag(context, tag), after_tag(context, tag)

"""


from selenium import webdriver
from pages.login_page import LoginPage
from pages.authorized_page import AuthorizedPage
from features.environment_secret import HIPCHAT_LOGIN, HIPCHAT_PASS
import os, datetime, time


def get_date_time():
    dt_format = '%Y%m%d_%H%M%S'
    return datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)


def before_all(context):

    context.hipchat_login = HIPCHAT_LOGIN
    context.hipchat_pass = HIPCHAT_PASS

    context.base_url = "https://www.hipchat.com"
    context.driver = webdriver.Chrome()

    context.login_page = LoginPage(context)
    context.authorized_page = AuthorizedPage(context)


def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("failed_scenarios_screenshots"):
            os.makedirs("failed_scenarios_screenshots")
        os.chdir("failed_scenarios_screenshots")
        context.driver.save_screenshot(scenario.name + get_date_time() + "_failed.png")
    context.driver.close()


def after_all(context):
    context.driver.quit()
