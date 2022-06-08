import requests
import yaml

from dms.api.scripts.baseapi import BaseApi


class TestDemo:
    def test_open_data(self):
        with open("./dms/api/datas/base.yml", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            # print(type(yaml_data))
        url = yaml_data["url"]
        print(url)
        headers = yaml_data["headers"]
        print(headers)
        code = "zt23058"
        r = requests.request("get", f"{url}/userInfo/get/{code}", headers=headers)
        print(r.json())

    # url = "http://10.192.119.24:8085"
    # headers = {
    #     "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzAx"
    #                      "OCIsImlhdCI6MTY1NDU2MzQ5MiwiZXhwIjoxNjU0NTcwNjkyfQ.aiUjXyJrw7LWq_KtV09PuKp45VwJZO6IIGzhoMVJ7g"
    #                      "LzXjMLa9ciZxps-TgOERHJKeKBrwpioQi2omWNjx3Wng"
    # }

    def test_get_userinfo(self):
        code = "zt23058"
        print(self.headers)
        r = requests.request("get", f"{self.url}/userInfo/get/{code}", headers=self.headers)
        print(r.json())


    def test_hehe(self):
        data = BaseApi().open_yaml_datas()
        url = data["url"]
        headers = data['headers']
        print(url)
        print(headers)
