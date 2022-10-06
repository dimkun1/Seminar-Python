# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

a = (int(input()))


def decidouble(a):
    list = []
    while a > 0:
        list.append(a % 2)
        a = a // 2

    list1 = []
    j = len(list)
    for i in range(j):
        j -= 1
        list1.append(list[j])
    s = ''.join(str(x) for x in list1)
    return s

b = decidouble(a)
print(b)
