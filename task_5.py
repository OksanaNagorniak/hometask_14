# Задание 5
# Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю

f = open("Words_text.txt", 'r')
data = f.read()
words = data.split()
print("Words in text file:", len(words))
f.close()
