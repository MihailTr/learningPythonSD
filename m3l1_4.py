x = input("Введите слово: ")
y = list(reversed(x))
z = ''.join(y)
if x == z:
    print(x, " - Слово полиндром")
else:
    print(x, " - Слово не полиндром")