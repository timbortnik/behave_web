# -*- coding: UTF-8 -*-

import requests
import json

BASE_URL = 'https://bortnik.hipchat.com'
#in future we can use context.base_url instead of BASE_URL and token from env.secret

class ApiRequest(object):

    def _get(self, url, payload, token):
        r = requests.get(BASE_URL + url, payload, headers = {'Authorization':'Bearer ' + token})
        return json.loads(r.text)

    def get_user(self, startindex = None, maxresults = None, includeguests = None, includedeleted = None):
        return self._get('/v2/user', {'start-index': startindex,
                                        'max-results': maxresults,
                                        'include-guests': includeguests,
                                        'include-deleted': includedeleted}, token='nJQhJG3Kg60vubHtug2msT9yc4O7CUPFXwI442hN')
