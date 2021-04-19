import json
import os
import pprint
import csv

with open(os.path.join("in_files", "users.json"), "r") as file:
    person_lst = json.loads(file.read())


with open(os.path.join("in_files", "books.csv"), newline='') as f:
    reader = csv.reader(f)
    header = next(reader)
    books_lst = []
    for row in reader:
        books_lst.append(dict(zip(header, row)))


def union():
    TOTAL_LST = []

    for person in person_lst:
        for book in books_lst:
            one_book_dict = {
                "title": book["Title"],
                "author": book["Author"],
                "height": book["Height"]
            }

            one_person_dct = {
                "name": person["name"],
                "gender": person["gender"],
                "address": person["address"],
                "books": [one_book_dict]
            }

            TOTAL_LST.append(one_person_dct)
    return TOTAL_LST

result = union()
#print(len(result))
#pprint.pprint(result)

with open(os.path.join("out_files", "result.json"), "w", encoding="utf-8") as file:
    s = json.dumps(result, indent=4)
    file.write(s)
