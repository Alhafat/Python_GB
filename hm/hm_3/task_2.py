"""
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.

Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф)
считать двумя словами.
Цифры за слова не считаем.

Отсортируйте по убыванию значения количества повторяющихся слов.

Пример

На входе:


text = 'Hello world. Hello Python. Hello again.'
На выходе:


[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
"""
import decimal

text = 'Hello world. Hello Python. Hello again.'
chars_to_remove = [".", ",", "!", "?", "-"]
text = text.replace("'", " ")
text = "".join([c.lower() for c in text if c not in chars_to_remove])
print(text)
temp = text.split(" ")
print(temp)
result = [(i, temp.count(i)) for i in temp if i.isalpha()]
result = list(set(result))
print(result)
result.sort()
result.sort(key=lambda a: a[1], reverse=True)
print(result[:10])
