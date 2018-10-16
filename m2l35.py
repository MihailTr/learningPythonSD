n=26
lst=[]
i=2
for i in range(n):
    if i==0:
        i+=1
    #print(i)
    y=i%3
    x=i%5
    if y==0 or x==0:
        lst.append(i)
        
print(lst)