import pytest
import yaml

from dms.api.scripts.projectInfo import ProjectInfo


class TestProject:
    def setup_class(self):
        self.project = ProjectInfo()

    @pytest.mark.parametrize(('admins', 'member', 'projectname'),
                             yaml.safe_load(open("../datas/project.yml", encoding="utf-8")))
    def test_add_project(self, admins, member, projectname):
        print(self.project.add_project(admins, member, projectname))

    def test_update_project(self):
        print(self.project.update_project())

    def test_get_project(self):
        print(self.project.get_project())
