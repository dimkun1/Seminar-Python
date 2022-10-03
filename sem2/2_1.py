# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = (float(input()))
summa = 0
b = a * 10 ** len(str(a))

while b > 0:
    summa = summa + b % 10
    b = b // 10

print(int(summa))
