#  Copyright (c) 2021. tooboredtocode
#  All Rights Reserved

import json

from functools import reduce
from textwrap import wrap

from genPossible import gen_possible

with open("../files/possible.json", "r") as read_file:
    data = json.load(read_file)

letters = "ACDDEEEHOORSTTTW"
fact_letters = int(reduce(lambda x, y: y * x, (sorted(list(data["key"][i.upper()] for i in letters)))))

loop = 1
letters = list(i for i in letters)

possible_with_remainder = dict(data)
combination = []
while 1:
    print(f"Unused Letters: {', '.join(letters)}")
    inp = input(f"Enter letter no. {loop}: ")

    if not inp:
        break

    for i in inp:
        if i.upper() in "JKQXZ":
            print("The letters JKQXZ are not supported")
            continue

    if inp == "!help":
        rem = '\n'.join(wrap(text=', '.join(possible_with_remainder['list']), width=120))
        print(f"Possible words:\n{rem}")
        continue

    if fact_letters % int(reduce(lambda x, y: y * x, (sorted(list(data["key"][i.upper()] for i in inp))))):
        print("Word not found, you can find the full list in the file possible.json")

        letters_in_word_plus_key = []
        for argh in inp:
            letters_in_word_plus_key.append(
                (data["key"][argh.upper()], argh)
            )

        fact_letters_copy = fact_letters
        missing = []
        for facts_char, char in letters_in_word_plus_key:
            if fact_letters_copy % facts_char:
                missing.append(char)
            else:
                fact_letters_copy = fact_letters_copy // facts_char

        print(f"Missing chars: {', '.join(missing)}")

        if input("Continue [yYcC]") not in "yYcC":
            break
        continue

    fact_letters = fact_letters // int(reduce(lambda x, y: y * x, (sorted(list(data["key"][i.upper()] for i in inp)))))

    for i in str(inp):
        letters.remove(i.upper())

    combination.append(inp)
    loop += 1

    possible_with_remainder = gen_possible(possible_with_remainder, fact_letters)

print()
print(f"Combination found: {', '.join(combination)}")
print(f"Unused letters: {', '.join(letters)}")
