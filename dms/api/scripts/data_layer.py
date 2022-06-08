import requests

from dms.api.scripts.baseapi import BaseApi


class DataLayer:
    _yaml_data = BaseApi().open_yaml_datas()
    _url = _yaml_data['url']
    _headers = _yaml_data['headers']

    def get_data_layer(self):
        params = {"codeOrName": ""}
        r = requests.request("get", f"{self._url}/web/wareHouse/list", headers=self._headers, params=params)
        print(r.json())
