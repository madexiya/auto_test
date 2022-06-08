import requests


class DataDetail:
    """
        数据检索
        """
    url = "http://10.192.119.24:8085"
    headers = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzA"
                         "xOCIsImlhdCI6MTY1NDQ3NzYxOSwiZXhwIjoxNjU0NDg0ODE5fQ.1564ABprDu4b1WOjUQpHQIuGn61Z-c-2fQikNeYJ"
                         "tEL1d1a8Z7cjXqlrSkWcpBEUCKSi4WdPezHguaVzVaktWA"
    }

    def table_baseinfo(self):
        """
        物理模型：表基础信息
        :return:
        """
        params = {"id": ""}
        r = requests.request("get", f"{self.url}/web/physical/model/base-info", params=params, headers=self.headers)
        print(r.json())

    def field_list(self):
        """
        字段列表
        :return:
        """
        params = {
            "physModeId": "",
            "entryName": ""
        }
        r = requests.request("get", f"{self.url}/web/physical/entry/list", params=params, headers=self.headers)
        print(r.json())

    def field_pratition_list(self):
        """
        字段分区列表
        :return:
        """
        params = {
            "physModeId": "",
            "entryName": ""
        }
        r = requests.request("get", f"{self.url}/web/physical/entry/partition", params=params, headers=self.headers)
        print(r.json())

    def consanguinity_list(self):
        """
        血缘关系列表
        :return:
        """
        params = {"id": ""}
        r = requests.request("get", f"{self.url}/web/physical/model/consanguinity", params=params, headers=self.headers)
        print(r.json())

    def table_change(self):
        """
        表变更
        :return:
        """
        params = {"id": ""}
        r = requests.request("get", f"{self.url}/web/physical/model/change", headers=self.headers, params=params)
        return r.json()

    def field_change(self):
        """
        字段变更
        :return:
        """
        params = {
            "physModeId": "",
            "entryName": ""
        }
        r = requests.request("get", f"{self.url}/web/physical/entry/change", headers=self.headers, params=params)
        return r.json()

    def field_change_detail(self):
        """
        字段变更详情
        :return:
        """
        params = {
            "physModeId": "",
            "id": ""
        }
        r = requests.request("get", f"{self.url}/web/physical/entry/change-detail", headers=self.headers, params=params)
        return r.json()

    def foreignkey_relation(self):
        params = {"id": ""}
        r = requests.request("get", f"{self.url}/web/physical/model/foreign-key", headers=self.headers, params=params)
        return r.json()
