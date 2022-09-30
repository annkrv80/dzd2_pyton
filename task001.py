#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

import os
def clear(): return os.system('cls')


clear()

a = input('Введите вещественное число: ')
sum = 0
for i in a:
    if i != '.':
        sum += int(i)

print(sum)
