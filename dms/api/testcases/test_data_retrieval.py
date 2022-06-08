from dms.api.scripts.data_retrieval import DataRetrieval


class TestDataRetrieval:
    def setup_class(self):
        self.data = DataRetrieval()

    def test_page_query(self):
        self.data.page_query()
