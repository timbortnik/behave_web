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
from features.environment_secret import HIPCHAT_LOGIN_2, HIPCHAT_PASS_2
from pages.api_page import ApiPage
from pages.settings_page import SettingsPage
from pages.people_page import PeoplePage
from pages.lobby_page import LobbyPage
from pages.search_page import SearchPage
from features.environment_secret import HIPCHAT_LOGIN, HIPCHAT_PASS
import selenium.webdriver.support.ui as ui
import datetime
import time
from pages.emoticons_page import EmoticonsPage
from helpers.api_requests import ApiRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def get_date_time():
    dt_format = '%Y%m%d_%H%M%S'
    return datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)


def before_all(context):
    context.hipchat_login = HIPCHAT_LOGIN
    context.hipchat_pass = HIPCHAT_PASS
    context.hipchat_login_2 = HIPCHAT_LOGIN_2
    context.hipchat_pass_2 = HIPCHAT_PASS_2
    context.base_url = "https://bortnik.hipchat.com"
    context.driver = webdriver.Chrome()
    context.wait = ui.WebDriverWait(context.driver, 10)
    context.lobby_page = LobbyPage(context)
    context.login_page = LoginPage(context)
    context.authorized_page = AuthorizedPage(context)
    context.api_page = ApiPage(context)
    context.settings_page = SettingsPage(context)
    context.people_page = PeoplePage(context)
    context.emoticons_page = EmoticonsPage(context)
    context.search_page = SearchPage(context)
    context.people_page = PeoplePage(context)
    context.test_name = "@test"
    context.api = ApiRequest


def before_scenario(context, scenario):
    if 'delete_room' in scenario.tags:
        context.login_page.navigate()
        context.login_page.enter_login(context.hipchat_login)
        context.login_page.login()
        context.login_page.enter_pass(context.hipchat_pass)
        context.settings_page.navigate()
        context.settings_page.api_access()
        # context.login_page.enter_pass(context.hipchat_pass)
        # context.settings_page.api_submit()
        context.api_page.create_token_by_scopes("Manage Rooms")
        context.token = context.api_page.token("Manage Rooms")
        context.driver.save_screenshot('scenario_result/' + "tokenparty" + "_failed.png")
        print(context.token)
        context.lobby_page.open_created_room()
        context.room_number = context.driver.current_url.split("/")[(len(context.driver.current_url.split("/"))) - 1]
        print(context.room_number)

def after_scenario(context, scenario):
    if scenario.status == "failed":
        context.driver.save_screenshot('scenario_result/' + scenario.name + get_date_time() + "_failed.png")
        file = open('scenario_result/' + scenario.name + get_date_time() + '.html', 'w')
        file.write(context.driver.page_source)
        file.close()

    if 'delete_room' in scenario.tags:
        token = context.token
        room_url = context.room_number
        context.api.delete_room(self=context.api, room=room_url, token=token)


def after_all(context):
    context.driver.quit()
