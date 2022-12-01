import time

import pytest

from pytest_live.calculator import Calculator


# conftest.py文件必须放在package下面才生效
# 作用域：先找当前同级目录的，没有就找上级目录的
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope="class")
def get_calc():
    calc = Calculator()
    # return calc
    yield calc
    print("测试结束")


@pytest.fixture(autouse=True)
def calc_fix():
    print("开始计算")
    yield
    print("结束计算")


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """每次执行用例，重新按时间命名生成一个日志文件"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'output/log/' + now + '.logs'
    # request是pytest中内置fixture，固定写法
    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)
