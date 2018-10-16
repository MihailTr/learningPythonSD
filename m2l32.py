import random
lst=[]
nun=14
coun=0

for z in range(nun):
    lst.append(random.randrange(nun*10))
print(lst)

#lst=[78,10,3,5,9,12,7]
#print(lst)
for i in range(len(lst)):
    j=i-1
    while (j > -1) and lst[j+1] < lst[j]:
        lst[j+1], lst[j] = lst[j], lst[j+1]
        j-=1
        print(lst)
        coun+=1
print(lst)
print(coun)