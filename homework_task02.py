from random import randint

def merge_sort(arr):
	if len(arr) > 1: # Проверка, что длина массива больше 1 (иначе сортировка не нужна).
		mid = len(arr) // 2 # Вычисление середины массива.
		left_half = arr[:mid] # Создание левой половины массива.
		right_half = arr[mid:] # Создание правой половины массива.

		# Рекурсивный вызов merge_sort для левой и правой половин массива.
		merge_sort(left_half)
		merge_sort(right_half)

		i = j = k = 0  # Инициализация индексов для объединения двух половин.
	
		# Объединение левой и правой половин в один отсортированный массив.
		while i < len(left_half) and j < len(right_half):
			if left_half[i] < right_half[j]:  # Сравнение элементов левой и правой половин.
				arr[k] = left_half[i]  # Если элемент из левой меньше, помещаем его в исходный массив.
				i += 1
			else:
				arr[k] = right_half[j]  # Если элемент из правой меньше, помещаем его в исходный массив.
				j += 1
			k += 1
		
		k = add_side_elements(i, k, arr, left_half)
		add_side_elements(j, k, arr, right_half)
		return k
	
# Добавление оставшихся элементов из левой и правой половин (если такие есть).
def add_side_elements(i, k, arr, some_half):
	while i < len(some_half):
		arr[k] = some_half[i]
		i += 1
		k += 1
	return k

# Генерация массива случайных чисел (размер: size, диапазон 1–99)
def random_list(lst_size):
    lst = []
    for i in range(lst_size):
        lst.append(randint(1, 99))
    return lst
    
lst_size = 15
initial_list = random_list(lst_size)
print(f'Initial_list: \t{initial_list}')
merge_sort(initial_list)
print(f'Merge sort: \t{initial_list}')
        
my_array = [64, 34, 25, 12, 22, 11, 90] # Создание неотсортированного массива.
merge_sort(my_array) # Вызов функции сортировки слиянием.
print("Отсортированный массив (Merge Sort):", my_array) # Вывод отсортированного массива.