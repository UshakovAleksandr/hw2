from source.dict import *
import pytest


def test_deleting(dict_items, dict_second_arg):
    assert deleting(dict_items, dict_second_arg) == {"2": 'c'}


def test_getting(dict_items, dict_second_arg):
    assert getting(dict_items, dict_second_arg) == "b"


def test_get_keys(dict_items):
    isinstance(get_keys(dict_items), dict)


def test_get_values(dict_items):
    isinstance(get_values(dict_items), dict)


def test_clearing(dict_items):
    assert clearing(dict_items) == None
