import os
import math
#  1 filter()
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False


# 2 filter()
def even_numbers_filter(even_number):
    if (even_number % 2) == 1:
        return True
    else:
        return False

#  3 filter()
# Список строк с похожими элементами
list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]
# функция, которая проверяет строки на вхождение
def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True
ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))


#  4 map()
def squ(i):
    return i ** 2


#  5 map()

def sum(k):
    return (k + 10)

#  6 map()
def subtraction(m):
    return (m - 10)

#  7 map()
def  multiplication(n):
    return (n * 4)

#  8 map()
def float_nummbers(number_5):
    return print(list(map(float, number_5)))

# 9 sorted()
def sortirovka(stroka):
    return print(sorted(stroka))

# 10 sorted()
def sortirovka_2(stroka_2):
    return print(sorted(stroka_2, reverse=True))

# 11 sorted()
def sortirovka_3(stroka_3):
    return print(sorted(stroka_3))

# 12 sorted()
def kortej_sorted(kortej):
    return print(sorted(kortej))

# 13 sorted()
def kortej_sorted_2(kortej_2):
    return print(sorted(kortej_2))

# 14 sorted()
def kortej_sorted_3(kortej_3):
    return print(sorted(kortej_3))

# 14 sorted()
def kortej_sorted_4(kortej_4):
    return print(sorted(kortej_4))


# 15 math.pi
def number_pi():
    return math.pi

# 16 math.sqrt
def number_sqrt(k):
    """

    :param k: число из которого вычисляется корень квадратный
    :return: вывод значения фугкции math.sqrt
    """
    return print(math.sqrt(k))

# 17 math.pow
def number_pow(x, y):
    return print(math.pow(x, y))




