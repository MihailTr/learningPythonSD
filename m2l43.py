a = []
nun = int(input("Введите число:"))
coun = 0

for i in range(nun):
    if i == 0:
        i += 3
    if i % 2 == 0 and i % 3 == 0:
        a.append(i)
    elif i % 2 == 1 and i % 7 == 0:
        a.append(i)
print(a)
