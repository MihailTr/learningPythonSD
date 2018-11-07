"""
Створити програму сортування списку чисел методом швидкого сортування
(рекурсивно) в порядку спадання
"""


import random


def QuickSort(a, start, end):
    if start < end:
        s = split(a, start, end)
        QuickSort(a, start, s - 1)
        QuickSort(a, s + 1, end)


def split(a, start, end):
    i = start - 1
    splitter = a[end]
    for j in range(start, end):
        if a[j] <= splitter:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[end] = a[end], a[i + 1]
    return (i + 1)


a = []
nun = int(input("Введите число:"))

for z in range(nun):
    a.append(random.randrange(nun * 10))
print(a)
QuickSort(a, 0, len(a) - 1)
print(a)
