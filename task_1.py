# Задание 1
# Дан файл с произвольным текстом,
# необходимо найти все числа в файле и записать в список numbers


with open("Text_task1.txt") as f:
    data = f.read()
number_list = [int(i) for i in data if i.isdigit()]
print(number_list)
f.close()





