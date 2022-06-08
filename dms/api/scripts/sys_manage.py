import requests

from dms.api.scripts.baseapi import BaseApi


class SysManage:
    """
    系统管理
    """
    yaml_data = BaseApi().open_yaml_datas()
    url = yaml_data['url']
    headers = yaml_data['headers']

    # url = "http://10.192.119.24:8085"
    # headers = {
    #     "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzAx"
    #                      "OCIsImlhdCI6MTY1NDU2MzQ5MiwiZXhwIjoxNjU0NTcwNjkyfQ.aiUjXyJrw7LWq_KtV09PuKp45VwJZO6IIGzhoMVJ7g"
    #                      "LzXjMLa9ciZxps-TgOERHJKeKBrwpioQi2omWNjx3Wng"
    # }

    def add_sys(self):
        datas = {
            "bizCode": "MAKA",
            "bizName": "玛卡巴卡系统",
            "bizStatus": 0,  # 系统状态; 0 未创建 1 使用中 2 停用
            "isDataDict": 0,  # 是否有数据字典; 0 否 1 是
            "principal": "zt23018",
            "applicationUrl": "www.du.com",
            "bizDesc": "玛卡巴卡呜",
            "bizFlowDiagramUrl": "www.maka.com",
            "bizLineCode": "LBU",
            "dataDictUrl": "www.dict.com",
            "erUrl": "www.er.com",
            "isBizFlowDiagram": 0,
            "isEr": 0,  # 是否有er图，0 否 1 是
            "subjectDomain": "marketSales",
            "sysDeptCode": "10801"
        }
        r = requests.request("post", f"{self.url}/businessInfo/add", json=datas, headers=self.headers)
        print(r.json())

    def page_query_sys(self):
        params = {
            "pageNum": "1",
            "pageSize": "10",
            "bizCode": "",
            "bizName": "玛卡巴卡系统",
            "bizStatus": "",
            "userCode": ""
        }
        r = requests.request("get", f"{self.url}/businessInfo/page", headers=self.headers, params=params)
        print(r.json())

    def update_sys(self):
        datas = {
            "bizCode": "",
            "bizName": "",
            "bizStatus": 0,
            "isDataDict": 0,
            "principal": "",
            "applicationUrl": "",
            "bizDesc": "",
            "bizFlowDiagramUrl": "",
            "bizLineCode": "",
            "dataDictUrl": "",
            "erUrl": "",
            "id": 0,
            "isBizFlowDiagram": 0,
            "isEr": 0,
            "subjectDomain": "",
            "sysDeptCode": ""
        }
        r = requests.request("post", f"{self.url}/businessInfo/update", json=datas, headers=self.headers)
        print(r.json())

    def page_query_schema(self):
        params = {
            "pageNum": "1",
            "pageSize": "10",
            "dbNameOrId": ""
        }
        r = requests.request("get", f"{self.url}/businessInfo/schema-biz-releated/get", headers=self.headers,
                             params=params)
        return r.json()

    def maintain_schema(self):
        datas = [
            {
                "bind": 0,
                "bizCode": "",
                "dbId": 0,
                "id": 0,
                "sourceCode": ""
            }
        ]
        r = requests.request("post", f"{self.url}/businessInfo/maintain-schema", json=datas, headers=self.headers)
        print(r.json())
