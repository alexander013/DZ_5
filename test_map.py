from functions import squ, sum, subtraction, multiplication, float_nummbers, sortirovka


# тест 1 для функции map() - возведение в степень каждого элемента списка с помрощью функции squ()
numbers_1 = [2, 4]
squared = map(squ, numbers_1)
print(list(squared))

# тест 2 для функции map() - сложение каждого элемента списка с любым числом
numbers_2 = [5, 7]
summa = map(sum, numbers_2)
print(list(summa))

# тест 3 для функции map() - вычитание из каждого элемента списка любого числа
numbers_3 = [10, 5]
subtract_numbers_3 = map(subtraction, numbers_3)
print(list(subtract_numbers_3))

# тест 4 для функции map() - умножение каждого элемента списка на любое число
numbers_4 = [10, 7]
multiplicat = map(multiplication, numbers_4)
print(list(multiplicat))

# тест 5 для функции map() - прелбразование каждого элемента списка в тип float
numbers_5 = [2, 18, 189]
float_nummbers(numbers_5)

# тест 5 для функции map() - прелбразование каждого элемента списка в тип float
numbers_5 = [2, 18, 189]
float_nummbers(numbers_5)