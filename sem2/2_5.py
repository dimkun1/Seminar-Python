#5. ** Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
from random import randint

c = int(input("Number of elements: "))

spisok = []
spisok1 = []
for i in range(1, c + 1):
    spisok.append(i)

for i in range(1, c + 1):
    k = randint(0, c + 1)
    spisok1.append(spisok[k])
print(spisok1)
