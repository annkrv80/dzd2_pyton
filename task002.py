#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
import os
def clear(): return os.system('cls')


clear()
n = int(input('Введите чило N '))
res = 1
for i in range(1, n+1):
    res = res*i
    print(res, end=' ')
