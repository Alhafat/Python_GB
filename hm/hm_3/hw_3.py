
#                                      * * *  DZ_3_1  * * *


backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight

#                                      * * *  DZ_3_2  * * *

import re
from collections import Counter

# Удаляем знаки препинания и приводим текст к нижнему регистру
cleaned_text = ''.join(char.lower() if char.isalpha() or char.isspace() else ' ' for char in text)

# Разбиваем текст на слова и считаем их количество
words = cleaned_text.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# Получаем 10 самых часто встречающихся слов
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)

#                                      * * *  DZ_3_3  * * *

backpacks = []
sorted_result = []
for i in range(2**len(items)):
    backpack = {}
    weight = 0
    for j, item in enumerate(items):
        if i & (1 << j):
            if weight + items[item] <= max_weight:
                backpack[item] = items[item]
                weight += items[item]
            else:
                break
    backpacks.append(backpack)

full_result = [backpack for backpack in backpacks if backpack]
result = []
for item in full_result:
    if item not in result:
        result.append(item)
pprint(result)


#                                      * * *  DZ_3_4  * * *


duplicates = set()
for item in lst:
    if lst.count(item) >= 2:
        duplicates.add(item)
result = list(duplicates)
print(result)
