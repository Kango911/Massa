# Ввод чисел через Memo (список)
numbers_input = input("Введите целые числа через пробел: ")

# Преобразование введенных данных в список целых чисел
numbers = list(map(int, numbers_input.split()))#Kango911

# Фильтрация чисел, которые не делятся на 5
filtered_numbers = [num for num in numbers if num % 5 != 0]

# Определение минимального элемента массива
if filtered_numbers:
    min_element = min(filtered_numbers)
    print("Массив, не содержащий числа, делящиеся на 5:", filtered_numbers)
    print("Минимальный элемент массива:", min_element)
else:
    print("Все введенные числа делятся на 5 или массив пуст.")
#Kango911