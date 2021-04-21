import json
import os
import pprint
import csv
import datetime

with open(os.path.join("in_files", "users.json"), "r") as file:
    person_lst = json.loads(file.read())

with open(os.path.join("in_files", "books.csv"), newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    books_lst = []
    for row in reader:
        books_lst.append(dict(zip(header, row)))


def time_count(func):
    def wrapper():
        start = datetime.datetime.now()
        result = func()
        print(datetime.datetime.now() - start)
        return result

    return wrapper


@time_count
def main():
    book_result = []
    for book in books_lst:
        one_book_dict = {
            "title": book["Title"],
            "author": book["Author"],
            "height": book["Height"],

        }
        book_result.append(one_book_dict)

    person_result = []
    for person in person_lst:
        one_person_dct = {
            "name": person["name"],
            "gender": person["gender"],
            "address": person["address"],
            "books": []
        }
        person_result.append(one_person_dct)

    TOTAl_LST = []
    for i, j in zip(person_result, book_result):
        i["books"].append(j)
        TOTAl_LST.append(i)

    with open(os.path.join("out_files", "result.json"), "w", encoding="utf-8") as file:
        result = json.dumps(TOTAl_LST, indent=4)
        file.write(result)


if __name__ == '__main__':
    main()
