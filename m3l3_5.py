"""
Створити програму для генерування послідовності Фібоначчі для числа N
рекурсивно
"""

def fib(n):
    if n < 0:
        return
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    return n


n=int(input("Введите число: "))
print(fib(n))

