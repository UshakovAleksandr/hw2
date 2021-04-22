import pytest
import os

def file_read():
    with open(os.path.join("list_test.txt"), "r", encoding="utf-8") as file:
        text = []
        for line in file.readlines():
            text.append(line.strip())
    return text


@pytest.fixture
def list_items():
    return file_read()


@pytest.fixture
def list_second_arg():
    return "1"
