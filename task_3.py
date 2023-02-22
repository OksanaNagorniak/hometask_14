# Задание 3
# Запросить у пользователя число N и запросить
# N чисел у пользователя, потом записать их в файл numbers.txt через пробел
from random import random

number_list = []
N = int(input('Введите размер списка: '))
for i in range(N):
    print("Введите елемент списка")
    item = int(input())
    number_list.append(item)
with open("numbers.txt", "w") as f:
    for item in number_list:
        s = str(item)
        f.write(s + " ")
