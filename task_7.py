# Задание 7
# Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз
# 'привет' - 10 раз
# 'как' - 9 раз
# 'у' - 7
# 'world' - 4
words = []
with open('words_text.txt', 'r') as f:
    for line in f:
        words.extend(line.split())
from collections import Counter

counts = Counter(words)
popular_5 = counts.most_common(5)
print("\n".join(str(e) for e in popular_5))
f.close()
