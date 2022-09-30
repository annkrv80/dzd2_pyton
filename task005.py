#Реализуйте алгоритм перемешивания списка.
from random import randint
import numbers
import os
from random import randrange
def clear(): return os.system('cls')


clear()
list = [randint(-100, 100) for i in range(11)]
print(list)
for i in range(len(list) // 2):
    box = list[i]
    list[i] = list[-i-1]
    list[-i-1] = box
print(list)
