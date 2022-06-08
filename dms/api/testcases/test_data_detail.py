from dms.api.scripts.data_detail import DataDetail


class TestDataDetail:
    def setup_class(self):
        self.data_detail = DataDetail()

    def test_physical_model_baseinfo(self):
        self.data_detail.physical_model_baseinfo()
