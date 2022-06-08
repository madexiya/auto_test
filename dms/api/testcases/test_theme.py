from dms.api.scripts.theme import Theme


class TestTheme:
    def setup_class(self):
        self.theme = Theme()

    def test_get_class_list(self):
        self.theme.get_theme_class_list()

    def test_get_theme_dirlist(self):
        self.theme.get_theme_list()
