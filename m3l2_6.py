import random

lst = []
chet=[]
notchet=[]
j=0
nun = 10
coun = 0

for z in range(nun):
    lst.append(random.randrange(nun * 10))
print(lst)
for i in range(nun):
    if lst[i]%2==0:
        chet.append(lst[i])
    else:
        notchet.append(lst[i])

nun1=len(chet)
for i in range(nun1):
    for j in range(nun1-1):
        if not chet[j] <= chet[j+1]:
            chet[j], chet[j+1] = chet[j+1], chet[j]

nun2=len(notchet)
for i in range(nun2):
    for j in range(nun2-1):
        if not notchet[j] <= notchet[j+1]:
            notchet[j], notchet[j+1] = notchet[j+1], notchet[j]

print(chet)
print(notchet)

print(chet+notchet)