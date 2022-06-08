import pytest
import requests
import yaml


class ProjectInfo:
    url = "http://10.192.119.26:8080"
    headers = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzAx"
                         "OCIsImlhdCI6MTY1Mzk2Njc5OCwiZXhwIjoxNjUzOTczOTk4fQ.G9wcYKhODvsejrxJUy_5K-EQEMALzs0qbtrxilq2Hd"
                         "6mhXI1fbQ7gh3hOdg0U3Nh83_sHe84KkVh7tX1wfxWWA"
    }

    def add_project(self, admins, member, projectname):
        datas = {
            "admins": f"{admins}",
            "member": f"{member}",
            "projectName": f"{projectname}"
        }
        r = requests.request("post", url=self.url + "/projectInfo/addProjectInfo", json=datas, headers=self.headers)
        return r.json()

    def get_project(self):
        params = {
            "pageNum": "1",
            "pageSize": "10"
        }
        r = requests.request("get", url=self.url + "/projectInfo/getProjectInfoByPage", headers=self.headers,
                             params=params)
        return r.json()

    def update_project(self):
        datas = {
            "admins": "zt23018",
            "member": "zt23088",
            "projectId": "0007",
            "projectName": "还业用接家东金"
        }
        r = requests.request("post", url=self.url + "/projectInfo/updateProjectInfoById", headers=self.headers,
                             json=datas)
        return r.json()
