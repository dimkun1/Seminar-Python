# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input("Введите число: "))

mult = 1
spisok = []

for i in range(1, n+1):
    spisok.append (i)


spisok1 = []
for i in range(1, n+1):
    mult *= i
    spisok1.append(mult)
print(spisok1)
