#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
n=int(input('Введите число N: '))
res=[1]#список в котором есть один эллемнт
for i in range(2,n+1):
    res.append(i*res[-1])
print(res)