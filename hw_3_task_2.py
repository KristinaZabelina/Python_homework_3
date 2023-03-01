# Задача 18: Требуется найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих строках 
# записаны N целых чисел Ai. Последняя строка содержит число X

import random
N = int(input('Введите размерность массива: '))
X = int(input('Введите число: '))
list=[]
delta = []
for i in range(N):
    i = random.randint(1,N)
    list.append(i+1)
print('Массив  :',list)
for j in range(len(list)):
    d = abs(list[j]-X)
    delta.append(d)
print(delta)
min = delta[0]
for k in range(len(delta)):
    if delta[k] < min:
         min = delta[k]
         a = list[k]

print('Самый близкий по величине к заданному числу X= ',a)