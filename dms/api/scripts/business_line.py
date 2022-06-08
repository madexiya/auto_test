import requests

from dms.api.scripts.baseapi import BaseApi


class BusinessLine:
    """
    事业线
    """
    yaml_data = BaseApi().open_yaml_datas()
    url = yaml_data['url']
    headers = yaml_data['headers']

    def biz_line_list(self):
        r = requests.request("get", f"{self.url}/web/bizlineinfo/list", headers=self.headers)
        return r.json()
