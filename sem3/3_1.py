#1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

#in
#5

#out
#[10, 2, 3, 8, 9]
#22

#in
#4

#out
#[4, 2, 4, 9]
#8

from random import randint

print("введите количество чисел")
a = (int(input()))


def chisla(a):
    list = [randint(1, 10) for i in range(a)]
    return list

list1 = chisla(a)
print(list1)

def sumnechet(a, list1):
    summ = 0
    for i in range(0, a, 2):
        summ += list1[i]
    return summ

b = sumnechet(a, list1)
print(b)