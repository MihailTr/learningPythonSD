import random

nun = 15
x = []
for a in range(nun):
    x.append(random.randrange(nun * 13 / 5))
print(x)
n = []
for i in x:
    if i not in n:
        n.append(i)
print(n)
