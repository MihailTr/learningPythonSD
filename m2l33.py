import random
lst=[]
nun=13
coun=0

for z in range(nun):
    lst.append(random.randrange(nun*10))
print(lst)

#lst=[78,10,3,5,9,12,7]
#print(lst)
for i in range(len(lst)):
    j=i-1
    key =lst[i]
    while lst[j] > key and j>=0:
        lst[j+1] = lst[j]
        j-=1
        #print(lst)
        coun+=1
    lst[j+1]=key
print(lst)
print(coun)