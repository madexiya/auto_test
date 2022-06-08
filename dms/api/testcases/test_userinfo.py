from dms.api.scripts.userInfo import UserInfo


class TestUserInfo:
    def setup_class(self):
        self.userinfo = UserInfo()

    def test_get_userinfo(self):
        self.userinfo.get_userinfo()

    def test_get_current_user(self):
        self.userinfo.get_current_user()

    def test_get_userinfo_list(self):
        self.userinfo.get_userinfo_list()
