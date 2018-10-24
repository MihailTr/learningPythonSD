y=5
z=False
while True:
    x = int(input("Введите число от 1 до 10: "))
    if x==y:
        print("Угадали")
        break
    elif x>y:
        print("Меньше")
        z=False
    else:
        print("Больше")
        z=False