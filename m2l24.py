import random
lst=[]
nun=10
coun=0
for z in range(nun):
    lst.append(random.randrange(nun*10))
print(lst)
for i in range(nun):
    for j in range(nun-1):
        if  lst[j]%2==0 >= lst[j+1]%2==1:
            lst[j], lst[j+1] = lst[j+1], lst[j]
        elif  lst[j]%2!=0 <= lst[j+1]%2!=1:
           lst[j], lst[j+1] = lst[j+1], lst[j]
        #elif  lst[j] >= lst[j+1]:
        #       lst[j], lst[j+1] = lst[j+1], lst[j]
        #elif lst[j] <= lst[j+1]:
        #       lst[j], lst[j+1] = lst[j+1], lst[j]
        coun+=1
print(lst)
print(coun)
