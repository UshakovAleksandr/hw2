import pytest
import json
import os


def file_read():
    with open(os.path.join("dict_test.json"), "r") as file:
        dct = json.loads(file.read())
    return dct


@pytest.fixture
def dict_items():
    return file_read()


@pytest.fixture
def dict_second_arg():
    return "1"
