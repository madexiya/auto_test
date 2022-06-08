from dms.api.scripts.sys_manage import SysManage


class TestSys:
    def setup_class(self):
        self.sys_manage = SysManage()

    def test_add_sys(self):
        self.sys_manage.add_sys()

    def test_query_sys(self):
        self.sys_manage.page_query_sys()
