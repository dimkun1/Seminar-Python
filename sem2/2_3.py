#3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
import math

n = int(input("Введите число: "))


spisok = []

for i in range(1, n+1):
    spisok.append(math.ceil((1 + 1 / n) ** n))
print(spisok)

summa = 0
for i in range(len(spisok)):
    summa += spisok[i]
print(summa)