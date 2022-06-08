import requests


class DataTableGuide:
    """
    数仓表导引
    """
    url = "http://10.192.119.24:8085"
    headers = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzA"
                         "xOCIsImlhdCI6MTY1NDQ3NzYxOSwiZXhwIjoxNjU0NDg0ODE5fQ.1564ABprDu4b1WOjUQpHQIuGn61Z-c-2fQikNeYJ"
                         "tEL1d1a8Z7cjXqlrSkWcpBEUCKSi4WdPezHguaVzVaktWA"
    }

    def physical_model_guide(self):
        params = {
            "bizCode": "",
            "deleteFlag": "0",  # 删除标记:0未删除,1已删除
            "modelLeader": "",  # 负责人,传员工编号
            "pageNum": "1",
            "pageSize": "10",
            "schemaId": "",
            "searchContent": "",
            "searchType": "1",  # 搜索类型1:按表,2按字段
            "themeCode": "0",
            "whCode": ""
        }
        r = requests.request("get", f"{self.url}/web/physical/model/guide", params=params, headers=self.headers)
        print(r.json())
