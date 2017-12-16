# -*- coding: UTF-8 -*-


class Page(object):
    """
    Base class that all page models can inherit from
    """

    url = None
    context = None

    def __init__(self, context):
        self.context = context

    def navigate(self):
        self.context.driver.get(self.context.base_url+self.url)

    def at(self):
        return self.context.base_url + self.url == self.context.driver.current_url
