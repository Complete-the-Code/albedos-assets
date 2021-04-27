#  Copyright (c) 2021. tooboredtocode
#  All Rights Reserved

import json

from functools import reduce


def gen_possible(input_dict: dict, input_int: int) -> dict:
    """
    Iterates over the possible factorised words and if a factor matches (it divides without any remainder) adds it to
    the returned list.
    """
    possible_ints = {}
    possible_list = []
    for key, val in input_dict["words"].items():
        if int(val["len"]) == 1:
            continue

        if input_int % int(key):
            continue

        possible_ints[key] = val

        for i in val["words"]:
            possible_list.append(i)

    if __name__ == '__main__':
        return {
            "key": input_dict["key"],
            "list": sorted(possible_list),
            "words": possible_ints
        }
    else:
        return {
            "words": possible_ints
        }


if __name__ == "__main__":
    with open("../files/words.json", "r") as read_file:
        data = json.load(read_file)

    letters = "ACDDEEEHOORSTTW"
    fact_letters = int(reduce(lambda x, y: y * x, (sorted(list(data["key"][i.upper()] for i in letters)))))

    output = gen_possible(data, fact_letters)

    disable_this_if_sure = 0
    file = "possible-alt.json" if disable_this_if_sure else "possible.json"

    with open(file, "w") as write_file:
        json.dump(output, write_file)
