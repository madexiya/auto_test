from dms.api.scripts.business_line import BusinessLine


class TestBiz:
    def setup_class(self):
        self.biz_line = BusinessLine()

    def test_get_biz_line(self):
        print(self.biz_line.biz_line_list())
