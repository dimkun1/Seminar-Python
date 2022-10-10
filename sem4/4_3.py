# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

# in
# 7

# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

# in
# -1

# out
# Negative value of the number of numbers!
# []

# in
# 10

# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]



from random import randint

print("введите количество чисел")
a = (int(input()))


def chisla(a):
    list = [randint(1, 10) for i in range(a)]
    return list

list1 = chisla(a)
print(list1)



def chislanuniqu(list1):
    list2 = []
    for list1 in list1:
        if list1 not in list2:
            list2.append(list1)
    return list2


print(chislanuniqu(list1))



