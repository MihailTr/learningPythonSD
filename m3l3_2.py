"""
Створити програму сортування списку чисел методом злиття (рекурсивно) в
порядку спадання
"""


import random


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1
        if i < len(left):
            l[k: k + len(left[i:])] = left[i:]
        if i < len(right):
            l[k: k + len(right[j:])] = right[j:]


n = int(input("Введите число: "))
lst = random.sample(range(1, 100), n)
print('inp list: ', lst)

merge_sort(lst)
print('out list: ', lst)
