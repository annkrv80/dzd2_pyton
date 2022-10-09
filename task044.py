#Чтение файла
#f=open('file.txt','r',encoding='utf8')
#data=f.readlines()#['1\n', '-2']
#data = [int(i) for i in data] #замена строковых i на int i
#data=f.read().split() #['1', '-2']
#print(data)

n = int(input('Введети число N '))
sp = [i for i in range(-n, n+1)]
print(sp)
with open('file.txt', 'r', encoding='utf') as f:
    index = [int(i) for i in f.readlines()]
print (index)
mult = 1
for ind in index:
    mult*= sp[ind]
print(mult)
