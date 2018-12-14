import sys
from copy import deepcopy

from common import load_input


def preprocess(raw):
    return raw


def create_recipe(recipes, elf_1, elf_2):
    s = recipes[elf_1] + recipes[elf_2]
    if s < 10:
        recipes.append(s)
    else:
        recipes.append(s // 10)
        recipes.append(s % 10)
    elf_1 = (elf_1 + recipes[elf_1] + 1) % len(recipes)
    elf_2 = (elf_2 + recipes[elf_2] + 1) % len(recipes)
    return recipes, elf_1, elf_2


def fn_p1(data):
    data = int(data)
    recipes, elf_1, elf_2 = [3, 7], 0, 1
    while len(recipes) < data + 10:
        recipes, elf_1, elf_2 = create_recipe(recipes, elf_1, elf_2)
    return "".join(map(str, recipes[data : data + 10]))


def fn_p2(data):
    recipes, elf_1, elf_2 = [3, 7], 0, 1
    ending = list(map(int, data))
    while True:
        if ending == recipes[-len(ending) :]:
            return len(recipes) - len(data)
        if ending == recipes[-len(ending) - 1 : -1]:
            return len(recipes) - len(data) - 1
        recipes, elf_1, elf_2 = create_recipe(recipes, elf_1, elf_2)


if __name__ == "__main__":
    raw_data = "5"
    data = preprocess(raw_data)
    print("Part 1 Example:", fn_p1(deepcopy(data)))
    raw_data = "59414"
    data = preprocess(raw_data)
    print("Part 2 Example:", fn_p2(deepcopy(data)))

    raw_data = "509671"
    data = preprocess(raw_data)
    # print("Part 1:", fn_p1(deepcopy(data)))  # answer: 2810862211
    print("Part 2:", fn_p2(deepcopy(data)))  # answer: 20227889
