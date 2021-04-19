def appending(item: list):
    lst = [el for el in item]
    return lst


def sorting(item: list):
    return sorted(item)


def deleting(item: list):
    item.pop()
    return item


def counting(item: list, x):
    return item.count(x)


def indexing(item: list, x):
    return item.index(x)
