from source.list import *
import pytest


@pytest.mark.parametrize("test_data, expected", [
    (["2", "1", "привет"],
     ["2", "1", "привет"])
])
def test_appending(test_data, expected):
    assert appending(test_data) == expected


def test_sorting(list_items):
    assert sorting(list_items) == ["1", "2", "привет"]


def test_deleting(list_items):
    assert deleting(list_items) == ["2", "1"]


def test_counting(list_items, list_second_arg):
    assert counting(list_items, list_second_arg) == 1


def test_indexing(list_items, list_second_arg):
    assert counting(list_items, list_second_arg) == 1
