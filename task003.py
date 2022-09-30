#Задайте список из n чисел последовательности (1+1/n)^n выведите на экран их сумму.
import os
def clear(): return os.system('cls')


clear()

n = int(input('Введите число n: '))
sum = 0
for i in range(1, n+1):
    a = round((1+1/i)**i, 2)
    sum += a
    print(a)
print('Сумма', round(sum,2))
