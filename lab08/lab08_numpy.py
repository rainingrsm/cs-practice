import numpy as np

#=============================================================================
print('=============================================================================')
print('Задание 1\n')

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3, dtype=int)

print(f'hours: {hours}')
print(f'shape: {hours.shape}')
print(f'ndim: {hours.ndim}')
print(f'size: {hours.size}')
print(f'dtype: {hours.dtype}')
print(f'line: {line}')
print(f'zeros: {zeros}')
print(f'unknown_table:\n{unknown_table}')
print(f'identity:\n{identity}')


#=============================================================================
print('=============================================================================')
print('Задание 2\n')

print('Третий элемент:', hours[2])
print('Последний элемент:', hours[-1])
print('Индексы 2–5:', hours[2:6])
print('Каждый второй:', hours[::2])
print('Обратный порядок:', hours[::-1])

#=============================================================================
print('=============================================================================')
print('Задание 3')

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print(f'shape: {temperatures.shape}')
print(f'ndim: {temperatures.ndim}')
print(f'size: {temperatures.size}')
print(f'Вторая строка, третий столбец: {temperatures[1, 2]}')
print(f'Первая строка: {temperatures[0]}')
print(f'Последний столбец: {temperatures[:, -1]}')
print(f'Первые две строки без первого столбца:\n{temperatures[:2, 1:]}')

center = temperatures[:2, 1:3]
print(f'Центральный фрагмент:\n{center}')

#=============================================================================
print('=============================================================================')
print('Задание 4')

matrix = np.arange(1, 26).reshape(5, 5)

first_rows = matrix[:3, :]
print(f'Первые три строки:\n{first_rows}')
print(f'shape: {first_rows.shape}')

last_rows = matrix[-2:, :]
print(f'Последние две строки:\n{last_rows}')
print(f'shape: {last_rows.shape}')

first_columns = matrix[:, :2]
print(f'Первые два столбца:\n{first_columns}')
print(f'shape: {first_columns.shape}')

block = matrix[1:4, 2:5]
print(f'Строки 1–3, столбцы 2–4:\n{block}')
print(f'shape: {block.shape}')

corner = matrix[-2:, -2:]
print(f'Правый нижний блок 2 x 2:\n{corner}')
print(f'shape: {corner.shape}')

#=============================================================================
print('=============================================================================')
print('Задание 5')

# copy() создаёт отдельный массив. При changed_hours = hours менялся бы и hours.
changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[::2] = -1 
print(f'Изменённый hours: {changed_hours}')
print(f'Исходный hours: {hours}')

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print(f'Изменённая matrix:\n{changed_matrix}')
print(f'Исходная matrix:\n{matrix}')

#=============================================================================
print('=============================================================================')
print('Задание 6')

numbers = np.arange(12)
# Всего 12 элементов: 3 * 4 = 12, поэтому reshape(3, 4) работает.
# Для reshape(5, 3) нужно 15 элементов, поэтому он вызовет ошибку.
table = numbers.reshape(3, 4)
transposed = table.T

print(f'shape numbers: {numbers.shape}')
print(f'shape table: {table.shape}')
print(f'shape transposed: {transposed.shape}')
