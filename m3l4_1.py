"""
Написати програму яка рекурсивно перевірить чи заданий список чисел є
посортовано.
"""


def is_sorted(lst):
    if len(lst) == 1:
        return True
    return lst[0] <= lst[1] and is_sorted(lst[1:])


any_list = [1, 2, 3, 4]
print(is_sorted(any_list))
