import pytest
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

    @pytest.mark.parametrize()
    def add_sys(self):
        datas = {
            "bizCode": "pdx",
            "bizName": "派大星",
            "bizStatus": 0,  # 系统状态; 0 未创建 1 使用中 2 停用
            "isDataDict": 0,  # 是否有数据字典; 0 否 1 是
            "principal": "zt23088",
            "applicationUrl": "www.du.com",
            "bizDesc": "玛卡巴卡呜",
            "bizFlowDiagramUrl": "www.maka.com",
            "bizLineCode": "LBU",
            "dataDictUrl": "www.dict.com",
            "erUrl": "www.er.com",
            "isBizFlowDiagram": 0,
            "isEr": 0,  # 是否有er图，0 否 1 是
            "subjectDomain": "marketSales",
            "sysDeptCode": "2835090"  # 传部门ID
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

    def query_sys_detail(self):
        params = {"id": 56}
        r = requests.request("get", f"{self.url}/businessInfo/detail", headers=self.headers, params=params)
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

    def query_unbound_schema(self, biz_code, page_num, page_size, dbname_or_id):
        """
        分页查询未绑定的schema列表
        :return:
        """
        params = {
            "bizCode": biz_code,
            "pageNum": page_num,
            "pageSize": page_size,
            "dbNameOrId": dbname_or_id
        }
        r = requests.request("get", f"{self.url}/web/collect/schema/with-biz/page", headers=self.headers, params=params)
        return r.json()

    def query_binding_schema(self):
        params = {
            "pageNum": "1",
            "pageSize": "10",
            "dbNameOrId": "",
            "bizCode": "UC-WT"
        }
        r = requests.request("get", f"{self.url}/businessInfo/schema-biz-releated/get", headers=self.headers,
                             params=params)
        return r.json()

    def page_query_schema(self):
        """
        分页查询 schema维护关系列表
        :return:
        """
        params = {
            "pageNum": "1",
            "pageSize": "10",
            "dbNameOrId": "",
            "bizCode": "UC-WT"
        }
        r = requests.request("get", f"{self.url}/businessInfo/schema-biz-releated/get", headers=self.headers,
                             params=params)
        return r.json()

    def maintain_schema(self):
        """
        维护schema
        :return:
        """
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
