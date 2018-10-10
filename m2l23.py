import random
lst=[]
nun=10
coun=0

for z in range(nun):
    lst.append(random.randrange(nun*10))
print(lst)
exchanges = True
for i in range(nun):
    exchanges = False
    for j in range(nun-1):
        if not lst[j] <= lst[j+1]:
            exchanges = True
            lst[j], lst[j+1] = lst[j+1], lst[j]
            coun+=1
print(lst)
print(coun)
