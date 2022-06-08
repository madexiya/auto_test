import requests


class Theme:
    url = "http://10.192.119.24:8085"
    headers = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzA"
                         "xOCIsImlhdCI6MTY1NDQ3NzYxOSwiZXhwIjoxNjU0NDg0ODE5fQ.1564ABprDu4b1WOjUQpHQIuGn61Z-c-2fQikNeYJ"
                         "tEL1d1a8Z7cjXqlrSkWcpBEUCKSi4WdPezHguaVzVaktWA"
    }

    def get_theme_list(self):
        params = {
            "themeType": "",
            "pid": ""
        }
        r = requests.request("get", f"{self.url}/web/business/theme/list", params=params, headers=self.headers)
        print(r.json())

    def get_theme_class_list(self):
        params = {"themeName": ""}
        r = requests.request("get", f"{self.url}/web/business/theme/classList", params=params, headers=self.headers)
        print(r.json())
