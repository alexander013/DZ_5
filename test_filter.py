from functions import filter_odd_num, even_numbers_filter, filter_duplicate

# первый тест для функции filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(filter_odd_num, numbers)))

# второй тест для функции filter()
number_list_2 = [1, 2, 5, 8, 9, 13, 10, 100, 50]
print(list(filter(even_numbers_filter, number_list_2)))




# третий тест для функции filter()
list1 = ["Python", "CSharp", "Java", "Go"]
list2 = ["Python", "Scala", "JavaScript", "Go", "PHP", "CSharp"]

ll = list2
out_filter = list(filter(filter_duplicate, list1))
ll = list1
out_filter += list(filter(filter_duplicate, list2))

print("Отфильтрованный список:", out_filter)



