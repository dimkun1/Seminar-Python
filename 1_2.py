#2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


#left = not (x or y or z)
#right = not x and not y and not z
#a = left == right

print("x, y, z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) == (not x and not y and not z):
                print(x, y, z)




