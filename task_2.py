# Задание 2
# Запросить у пользователя текст и записать его в файл data.txt
text = input("text: ")
with open('data.txt', 'w') as f:
    f.write(text)
f.close()

