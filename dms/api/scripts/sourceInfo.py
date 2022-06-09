class SourceInfo:
    url = "http://10.192.119.26:8080"
    headers = {
        "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VySWQiOiIiLCJhcHBJZCI6IiIsInVzZXJOYW1lIjoienQyMzAx"
                         "OCIsImlhdCI6MTY1Mzk2Njc5OCwiZXhwIjoxNjUzOTczOTk4fQ.G9wcYKhODvsejrxJUy_5K-EQEMALzs0qbtrxilq2Hd"
                         "6mhXI1fbQ7gh3hOdg0U3Nh83_sHe84KkVh7tX1wfxWWA"
    }

    def add_sourceinfo(self):
        datas = {
            "bizCode": "",
            "bizName": "",
            "id": 0,
            "isUsed": 0,
            "sourceAttrInfos": [
                {
                    "attrName": "",
                    "attrType": 0,
                    "attrValue": ""
                }
            ],
            "sourceCode": "",
            "sourceDesc": "",
            "sourceName": "",
            "sourcePwd": "",
            "sourceType": 0,
            "sourceUrl": "",
            "sourceUser": "",
            "sourceVersion": "",
            "subjectDomain": "",
            "userId": ""
        }


