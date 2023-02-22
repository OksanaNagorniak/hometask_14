# Задание 4
# # Сгенерировать 100 рандомных чисел и записать их в файл
# random_numbers.txt, где одна строка = одно число

import random
with open("random_numbers.txt", 'w') as f:
    for i in range(100):
        numbers = random.randint(0, 100)
        f.write(str(numbers) + "\n")
f.close()
