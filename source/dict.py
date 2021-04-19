def deleting(item: dict, x):
    item.pop(x)
    return item


def getting(item: dict, x):
    return item.get(x)


def get_keys(item: dict):
    return item.keys()
    # dict_keys([1, 2])


def get_values(item: dict):
    return item.values()
    # dict_values(['b', 'c'])


def clearing(item: dict):
    return item.clear()
    # None
