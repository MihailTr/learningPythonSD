"""
Створити програму, яка генерує посортований список чисел, де парні елементи
списку діляться на 3, а непарні елементи діляться на 5. Вхідним параметром є N -
число, до якого генерувати список.
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
            if left[i] < right[j]:
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


x = []
y = []
a = []
nun = int(input("Введите число: "))

for aa in range(nun):
    a.append(random.randrange(nun * 10))
print("List a: ", a)


for i in a:
    if i % 3 == 0 and i % 2 == 0:
        x.append(i)
    elif i % 5 == 0 and i % 2 == 1:
        y.append(i)

print("парні елементи списку діляться на 3: ", x)
print("непарні елементи діляться на 5: ", y)
merge_sort(x)
merge_sort(y)
print("List: ",x + y)
