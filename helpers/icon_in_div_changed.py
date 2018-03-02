from pages.lobby_page import LobbyPage


class IconInDivChanged(object):
    def __init__(self, div, icon_status):
        self.div = div
        self.icon_status = icon_status

    def __call__(self, *args, **kwargs):
        element = LobbyPage.find_ico_in_div(self.div)
        icon_str = str(element.get_attribute('xlink:href'))
        if self.icon_status not in icon_str:
            return icon_str
        else:
            return False
