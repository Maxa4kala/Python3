#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#Пример:

#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

#my_list = [2, 3, 5, 9, 3]
#print(sum(my_list[1::2]))

#some_list = [int(input()) for _ in range(int(input()))]
#summ = 0
#for i in range(1, len(some_list), 2):
#    summ += some_list[i]
#print(summ)

#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#Пример:

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

#my_list = [2, 3, 4, 5, 6]
#result_list = []
#for i in range((len(my_list)+1)//2):
#     result_list.append(my_list[i]*my_list[len(my_list)-1-i])
#print(result_list)

#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов.

#a = [float(input()) for i in range(int(input()))]
#my_list = [float('0.' + str(i).split('.')[1]) for i in a if '.' in str(i)]
#print(max(my_list) - min(my_list))

#Напишите программу, которая будет преобразовывать десятичное число в 
# двоичное.

#Пример:

#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

#n = int(input())
#my_str = ''
#while n > 0:
#    my_str = str(n % 2) + my_str
#    n //= 2
#print(my_str)    

#Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

#Пример:

#- для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

a = int(input("Insert a:"))

fibo_list = [0]*(a*2*1)
print(fibo_list)
fibo_list[a] = 0
fibo_list[a+1] = 1

for i in range(a+2, len(fibo_list)):
    fibo_list[i] = fibo_list[i-2]+fibo_list[i-1]

for i in range(a, -1, -1):
    fibo_list[i] = fibo_list[i+2]-fibo_list[i+1]

print(fibo_list)    