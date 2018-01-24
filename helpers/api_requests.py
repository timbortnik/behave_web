# -*- coding: UTF-8 -*-

import requests
import json
token_group = 'nJQhJG3Kg60vubHtug2msT9yc4O7CUPFXwI442hN'

class ApiRequest(object):

    def api_get(self, **kwargs):
        url = 'https://bortnik.hipchat.com/v2/user'
        headers_get = {'Authorization': token_group}
        payload = {
            'start-index': 1,
            'max-results': 1,
            'include-guests': None,
            'include-deleted': None
        }


        headers_post = {
            "content-type": "application/json",
            "authorization": "Bearer %s" % token_group}

        url = 'https://bortnik.hipchat.com/v2/user'


        # payload = {
        #     "name": "Sergey Moroz API",
        #     "roles": [],
        #     "title": "sergeyApi",
        #     "mention_name": "@sergeyApi",
        #     "is_group_admin": False,
        #     "timezone": "UTC",
        #     "password": "api",
        #     "email": "testmail@com",
        #    }

        r = requests.get(url, params=payload, headers={'Authorization': 'Bearer ' + token_group})
        # r = requests.post(url, data=json.dumps(payload), headers=headers_post)

        # print(r.text)
        # print(r.status_code)
        # print(r.json())


        json_data = json.loads(r.text)
        print(json_data['items'][0]['name'])
