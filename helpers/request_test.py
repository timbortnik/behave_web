import requests
import json

# BASE_URL = 'https://bortnik.hipchat.com'
#
#
# class ApiRequest(object):
#
#     def _delete(self, url, token):
#         r = requests.delete(BASE_URL + url + "?auth_token=" + token)
#         return json.loads(r.text)
#
#     def delete_room(self, url, token):
#         return self._delete(url, token)
def test():
    r = requests.delete('https://bortnik.hipchat.com/v2/room/4445929?auth_token=vgCIl4CD2RIrIzPzHY6sKtlFe6AOXAu33wcdemEc')
    return json.loads(r.text)

test()