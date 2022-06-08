import requests


class DataRetrieval:
    """
    数据检索
    """
    url = "http://10.192.119.24:8085"
    headers = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzAx"
                         "OCIsImlhdCI6MTY1NDU2MzQ5MiwiZXhwIjoxNjU0NTcwNjkyfQ.aiUjXyJrw7LWq_KtV09PuKp45VwJZO6IIGzhoMVJ7g"
                         "LzXjMLa9ciZxps-TgOERHJKeKBrwpioQi2omWNjx3Wng"
    }

    def page_query(self):
        """
        数据检索分页查询
        :return:
        """
        params = {
            "bizCode": "",
            "deleteFlag": "0",  # 删除标记:0未删除,1已删除
            "modelLeader": "",  # 负责人,传员工编号
            "pageNum": "1",
            "pageSize": "10",
            "schemaId": "",
            "searchContent": "",
            "searchType": "1",  # 搜索类型1:按表,2按字段
            "themeCode": "",
            "whCode": ""
        }
        r = requests.request("get", f"{self.url}/web/physical/model/page", params=params, headers=self.headers)
        print(r.json())
