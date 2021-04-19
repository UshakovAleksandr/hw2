import pytest
import json


def file_read():
    with open("../tests_dict/dict_test.json", "r") as file:
        dct = json.loads(file.read())
    return dct


@pytest.fixture
def dict_items():
    return file_read()


@pytest.fixture
def dict_second_arg():
    return "1"
