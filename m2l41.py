import random

a = []
nun = 13
coun = 0

for aa in range(nun):
    a.append(random.randrange(nun * 10))
print(a)


# a=[1]
# a=[1,3,5,10,4,2,8]
def MergerGroup(a, left, m, right):
    if left >= right: return None
    if m < left or right < m: return None
    t = left
    for j in range(m + 1, right + 1):
        for i in range(t, j):
            #	print(a[j],a[i])
            if a[j] < a[i]:
                r = a[j]
                for k in range(j, i, -1):
                    a[k] = a[k - 1]
                a[i] = r
                t = 1
                break


if len(a) < 2:
    print('None')
    exit(0)
# print(a)
k = 1
while k < len(a):
    g = 0
    while g < len(a):
        z = g + k + k - 1
        r = z if z < len(a) else len(a) - 1
        MergerGroup(a, g, g + k - 1, r)
        g += 2 * k
    k *= 2
print(a)
