"""
Створити програму сортування списку чисел методом швидкого сортування в
порядку зростання
"""


import random


def QuickSort(a):
    w = [x for x in range(int(4 + (len(a) // 2)))]
    k = 0
    w[0] = 0
    w[1] = len(a) - 1
    while (k >= 0):
        i = QuickSortPos(a, w[k], w[k + 1])
        if (i != w[k + 1]):
            RL = i + 1
        else:
            RL = w[k + 1]
        RR = w[k + 1]
        LL = w[k]
        if (i != w[k]):
            LR = i - 1
        else:
            LR = w[k]
        k -= 2
        if (RL != RR):
            k += 2
            w[k] = RL
            w[k + 1] = RR
        if (LL != LR):
            k += 2
            w[k] = LL
            w[k + 1] = LR
    return (a)


def QuickSortPos(a, left, right):
    i = left
    j = right - 1
    while (True):
        while (a[i] < a[right]):
            i += 1
        while (a[j] > a[right] and j > left):
            j -= 1
        if (i >= j):
            break
        a[i], a[j] = a[j], a[i]
    a[right], a[i] = a[i], a[right]
    return (i)


a = []
nun = int(input("Введите число:"))


for z in range(nun):
    a.append(random.randrange(nun * 10))

print(a)
print(QuickSort(a))
