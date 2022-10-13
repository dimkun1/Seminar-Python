# def check(line):
#     arr = line.split()
#     for i in arr:
#         if not i.strip("-").isdigit():
#             return[]
#     return arr

# def min_max(array):
#     if array:
#         return min(array, key=int), max(array, key=int)
#     return []

# f = check("2 3 56 12")
# print(min_max(f))





from math import sqrt


def abc(a, b, c):
    D = b ** 2 - 4 * a * c
    with open("result.txt", 'a', encoding='utf-8') as my_f:
        my_f.write(f"{a}x**2 + {b}x + {c} = 0\n")
        if D > 0:
            my_f.write(str((-b + sqrt(D)) / (2 * a)) + "\n")
            my_f.write(str((-b - sqrt(D)) / (2 * a)) + "\n")
        elif D == 0 and b:
            my_f.write(str(-b / (2 * a)) + "\n")
        else:
            my_f.write(str("корней нет" + "\n"))


for i in range(1):
    abc(int(input("введите число = ")), int(
        input("введите число = ")), int(input("введите число = ")))

