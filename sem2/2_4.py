#4. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).


a = int(input("Position one: "))
b = int(input("Position two: "))
c = int(input("Number of elements: "))

spisok = []

for i in range(-c, c + 1):
    spisok.append(i)

print(spisok[a - 1] * spisok[b - 1])



