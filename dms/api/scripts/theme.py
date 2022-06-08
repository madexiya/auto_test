import requests


class Theme:
    """
    主题域
    """
    url = "http://10.192.119.24:8085"
    headers = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzA"
                         "xOCIsImlhdCI6MTY1NDQ3NzYxOSwiZXhwIjoxNjU0NDg0ODE5fQ.1564ABprDu4b1WOjUQpHQIuGn61Z-c-2fQikNeYJ"
                         "tEL1d1a8Z7cjXqlrSkWcpBEUCKSi4WdPezHguaVzVaktWA"
    }

    def get_theme_class_list(self):
        """
        获取主题域层级列表
        :return:
        """
        params = {"themeName": ""}
        r = requests.request("get", f"{self.url}/web/business/theme/classList", params=params, headers=self.headers)
        print(r.json())
