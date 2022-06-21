from functions import sortirovka, sortirovka_2, sortirovka_3, kortej_sorted, kortej_sorted_2, kortej_sorted_3, kortej_sorted_4

# тест 1 для функции sortid() - сортировка слов строки по возрастанию
stroka = 'hello'
print(sortirovka(stroka))

# # тест 2 для функции sortid() - сортировка слов строки по убыванию
stroka_2 = 'hello'
print(sortirovka_2(stroka_2))

# # тест 3 для функции sortid() - сортировка чисел
stroka_3 = [1, 4, 6, 9, 2]
print(sortirovka_3(stroka_3))

# тест 4 для функции sortid() - сортирвка списка кортежей
kortej = [(1, 2), (6, 8), (10, 45), (0, 1)]
print(kortej_sorted(kortej))

# тест 5 для функции sortid() - сортирвка словаря (вывод списка ключей)
kortej_2 = {2: 'red', 3: 'Pyton', 1: 'java'}
print(kortej_sorted_2(kortej_2))

# тест 6 для функции sortid() - сортирвка словаря (вывод списка значений)
kortej_3 = {2: 'red', 3: 'Pyton', 1: 'java'}
print(kortej_sorted_3(kortej_3.values()))

# тест 7 для функции sortid() - сортирвка словаря (вывод списка списка кортежей)
kortej_4 = {2: 'red', 3: 'Pyton', 1: 'java'}
print(kortej_sorted_4(kortej_4.items()))