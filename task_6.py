# Задание 6
# Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

f = open("task_6.txt", "r")
text = f.read()
text = text.split()
sum = 0
for i in range(len(text)):
    sum += int(text[i])
print(sum)
f.close()
