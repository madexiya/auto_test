import pytest
import yaml


class TestYaml:
    @pytest.mark.parametrize("env", yaml.safe_load(open("env.yml")))
    def test_yaml(self, env):
        if "test" in env:
            print("这是测试环境")
            print(env)
        elif "dev" in env:
            print("这是开发环境")
            print(env)
