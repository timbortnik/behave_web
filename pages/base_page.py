# -*- coding: UTF-8 -*-


class Page(object):
    """
    Base class that all page models can inherit from
    """

    url = None
    context = None

    def __init__(self, context):
        self.context = context

    def navigate(self, driver):
        driver.get(self.context.base_url+self.url)

    def at(self, driver):
        return self.context.base_url + self.url == driver.current_url

