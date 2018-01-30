from pages.lobby_page import LobbyPage


class LobbyPageIconInDivChanged(object):
    def __init__(self, lobby_page, div, icon_status):
        self.div = div
        self.icon_status = icon_status
        self.lobby_page = lobby_page

    def __call__(self, *args, **kwargs):
        element = self.lobby_page.find_ico_in_div(self.div)
        icon_str = str(element.get_attribute('xlink:href'))
        if self.icon_status not in icon_str:
            return icon_str
        else:
            return False
