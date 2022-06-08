import yaml


class BaseApi:
    def open_yaml_datas(self):
        with open("../datas/base.yml", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data
