#Задайте числами список из N элементов, заполненных из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#Позиции хранятся в файле file.txt в одной строке одно число.

import os
def clear(): return os.system('cls')


clear()
n = int(input('Введите число N '))
with open('file.txt') as file:
    i1 = int(file.readline())
    i2 = int(file.readline())
numbers = list(range(-n, n+1))
print(numbers)
print('Позиции',i1,i2)
print(numbers[i1]*numbers[i2])
