import random
lst = []
i = 0
j = 0
nun = 10

for z in range(nun):
    lst.append(random.randrange(nun * 10))
print(lst)

flegstop = False
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i] == lst[j]:
            if not i == j:
                print(lst[i])
                flegstop = True
            break
if flegstop == False:
    print('not sumbol')
