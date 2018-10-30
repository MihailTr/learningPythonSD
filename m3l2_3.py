x = 10
y = 15
n = []
m = []
z = []
for i in range(x):
    n.append(i)
print(n)
for j in range(y):
    m.append(j)
print(m)

if len(n) > len(m):
    for f in n:
        if f in m:
            z.append(f)
    print("n", z)
else:
    for g in m:
        if g in n:
            z.append(g)
    print("m", z)
