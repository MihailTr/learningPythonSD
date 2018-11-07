"""
Написати програму яка отримує від користувача стрічку, рахує скільки разів
зустрічається те чи інше слово та виводить результат у постортованому порядку.
Наприклад, користувач задав стрічку: Hello, my name is Taras. yes, yes, Taras.
Taras has 5 letters! Результат - це список: [5:1, Hello:1, Taras:3, has:1, is:1, letters:1,
my:1, name:1, yes:2]
"""


n_lst = []
n_lst_c = []
n_lst_d = []
n_lst_cc = []
z = []
n_Str = "Hello, my name is Taras. yes, yes, Taras. Taras has 5 letters!"
print(n_Str)
n_Str = n_Str.replace('.', '')
n_Str = n_Str.replace(',', '')
n_Str = n_Str.replace('!', '')
n_lst = n_Str.split()
n_lst = sorted(n_lst)
n_lst_cc = n_lst[:]


for i in n_lst:
    n_lst_c = n_lst_cc.count(i)
    n_lst_d.append((str(i) + ':' + str(n_lst_c)))

for j in n_lst_d:
    if j not in z:
        z.append(j)


print(n_Str)
print("z", z)
print("контроль [5:1, Hello:1, Taras:3, has:1, is:1, letters:1, my:1, name:1, yes:2]")
