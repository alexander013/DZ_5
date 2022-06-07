def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False



def even_numbers_filter(even_number):
    if (even_number % 2) == 1:
        return True
    else:
        return False


# Список строк с похожими элементами
list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]

# функция, которая проверяет строки на вхождение
def filter_duplicate(string_to_check):
    if string_to_check in ll:
        return False
    else:
        return True

# Применение filter() для удаления повторяющихся строк
ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))








#
# def squ(squared):
#     numbers = [1, 2, 3, 4, 5]
#     squared = []
#     for num in numbers:
#         squared.append(num ** 2)
#     return(squared)
#
# squ()
# print(squared)