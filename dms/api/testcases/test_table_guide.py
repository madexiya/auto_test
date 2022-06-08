from dms.api.scripts.data_table_guide import DataTableGuide


class TestTableGuide:
    def setup_class(self):
        self.table_guide = DataTableGuide()

    def test_table_guide(self):
        self.table_guide.physical_model_guide()
