def get_uniq_numbers(src: list):
    unique_set = set()
    tmp = set()
    for i in src:
        if i not in tmp:
            unique_set.add(i)
        else:
            unique_set.discard(i)
        tmp.add(i)

    return [el for el in src if el in unique_set]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

print(*get_uniq_numbers(src))
