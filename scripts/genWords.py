#  Copyright (c) 2021. tooboredtocode
#  All Rights Reserved

import json

from collections import OrderedDict
from functools import reduce

with open('../files/words_alpha.txt') as word_file:
    words = set(word_file.read().split())

data = {
    "key": {
        "A": 3,
        "B": 5,
        "C": 7,
        "D": 11,
        "E": 13,
        "F": 17,
        "G": 19,
        "H": 23,
        "I": 29,
        "L": 31,
        "M": 37,
        "N": 41,
        "O": 43,
        "P": 47,
        "R": 53,
        "S": 59,
        "T": 61,
        "U": 67,
        "V": 71,
        "W": 73,
        "Y": 79
    },
    "words": {}
}

key = data["key"]

for word in words:
    try:
        val = int(reduce(lambda x, y: y * x, (used_primes := sorted(list(key[i.upper()] for i in word)))))
    except KeyError:
        continue

    if val in (base := data["words"]):
        base[val]["words"].append(word)
    else:
        base[val] = {
            "len": len(word),
            "used_characters": list(i.upper() for i in word),
            "words": [word]
        }

data["words"] = OrderedDict(sorted(data["words"].items()))

with open("../files/words.json", "w") as write_file:
    json.dump(data, write_file)
