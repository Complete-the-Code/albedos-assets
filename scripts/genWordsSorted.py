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
    "words": {
        "u16": {},
        "u32": {},
        "u64": {},
        "u128": {},
        "bigint": {}
    }
}

key = data["key"]

for word in words:
    try:
        val = int(reduce(lambda x, y: y * x, (used_primes := sorted(list(key[i.upper()] for i in word)))))
    except KeyError:
        continue

    if val < 2 ** 16:
        sort = "u16"
    elif val < 2 ** 32:
        sort = "u32"
    elif val < 2 ** 64:
        sort = "u64"
    elif val < 2 ** 128:
        sort = "u128"
    else:
        sort = "bigint"

    if val in (base := data["words"][sort]):
        base[val]["words"].append(word)
    else:
        base[val] = {
            "used_primes": used_primes,
            "words": [word]
        }

for i in ["u16", "u32", "u64", "u128", "bigint"]:
    data["words"][i] = OrderedDict(sorted(data["words"][i].items()))

with open("../files/words-sorted.json", "w") as write_file:
    json.dump(data, write_file)
