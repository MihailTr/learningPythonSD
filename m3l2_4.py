import random

lst = []
nun = 14

for z in range(nun):
    lst.append(random.randrange(nun * 10))
print(lst)

for i in range(len(lst)):
    j = i - 1
    while (j > -1) and lst[j + 1] < lst[j]:
        lst[j + 1], lst[j] = lst[j], lst[j + 1]
        j -= 1

print(lst)
