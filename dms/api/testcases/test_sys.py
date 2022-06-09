import pytest

from dms.api.scripts.sys_manage import SysManage


class TestSys:
    def setup_class(self):
        self.sys_manage = SysManage()

    def test_add_sys(self):
        self.sys_manage.add_sys()

    def test_query_sys(self):
        self.sys_manage.page_query_sys()

    def test_query_sys_detail(self):
        self.sys_manage.query_sys_detail()

    def test_query_schema(self):
        print(self.sys_manage.page_query_schema())

    def test_query_binding_sys(self):
        print(self.sys_manage.query_binding_schema())

    @pytest.mark.parametrize('datas', [("UC-YT", "1", "10", "")])
    def test_query_unbound_sys(self, datas):
        print(self.sys_manage.query_unbound_schema(*datas))
