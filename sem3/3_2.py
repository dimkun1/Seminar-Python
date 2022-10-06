#2. Напишите программу, которая найдёт произведение пар чисел списка.
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#in
#4

#out
#[2, 5, 8, 10]
#[20, 40]

#in
#5

#out
#[2, 2, 4, 8, 8]
#[16, 16, 4]


from random import randint


print("введите количество чисел")
a = (int(input()))


def chisla(a):
    list = [randint(1, 10) for i in range(a)]
    return list

list = chisla(a)
print(list)


def proizvpara(a, list):
    list1 = []
    for i in range(a - 1):
        a -= 1
        if i < a:
            list1.append(list[i] * list[a])
        if i == a:
            list1.append(list[i])
    return list1

list1 = proizvpara(a, list)
print(list1)