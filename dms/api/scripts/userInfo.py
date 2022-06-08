import requests
import yaml

from dms.api.scripts.baseapi import BaseApi


class UserInfo:
    data = BaseApi().open_yaml_datas()
    url = data["url"]
    headers = data["headers"]
    # def __init__(self):
    #     with open("../datas/base.yml", encoding="utf-8") as f:
    #         yaml_data = yaml.safe_load(f)
    #     self.url = yaml_data["url"]
    #     self.headers = yaml_data["headers"]
    # url = "http://10.192.119.24:8085"
    # headers = {
    #     "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzAx"
    #                      "OCIsImlhdCI6MTY1NDU4MDIxNywiZXhwIjoxNjU0NTg3NDE3fQ.bZgGf5GeFlzpe77uVbIciDD1siF_YhHnzExE-k1TwJ"
    #                      "n4L2t6_p3h1TSXJm_Q-AOyGFoVSF3Z0RiBiWmGVATd3Q"
    # }

    def get_userinfo(self):
        code = "zt23058"
        r = requests.request("get", f"{self.url}/userInfo/get/{code}", headers=self.headers)
        print(r.json())

    def get_current_user(self):
        res = requests.request("get", f"{self.url}/userInfo/get/current", headers=self.headers)
        print(res.json())

    def get_userinfo_list(self):
        params = {
            "code": "zt2301",
            "name": "",
            "pageNum": "",
            "pageSize": ""
        }
        r = requests.request("get", f"{self.url}/userInfo/getUserInfoList", params=params, headers=self.headers)
        print(r.json())
