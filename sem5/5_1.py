# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.

# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

from random import sample


def list_rand_world(count: int, alp: str = "абв"):
    words_list = []
    for i in range(count):
        letters = sample(alp, 3)
        words_list.append("".join(letters))
    return " ".join(words_list)


def simple(words: str) -> str:
    return " ".join(words.replace("абв", "").split())

all_list = list_rand_world(int(input("Number of words: ")))
print(all_list)
print(simple(all_list))







