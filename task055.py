from random import randint, random


list = [randint(-100, 100) for i in range(11)]
print(list)
for i in range(len(list)):
    k = randint(0,len(list)-1)
    list[i], list[k] = list[k],list[i]
print(list)
