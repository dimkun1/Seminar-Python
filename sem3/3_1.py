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


print(chisla(a))

def sumnechet(chisla()):
    summ = 0
    for i in range(0, len(list), 2):
        summ += list[i]
    return summ

print(sumnechet(a))