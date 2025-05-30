import numpy as np

matrix = np.random.randint(1, 11, (5, 5))
mean_val = np.mean(matrix)
min_val = np.min(matrix)
max_val = np.max(matrix)
sum_columns = np.sum(matrix, axis=0)

print("Матрица 5x5:")
print(matrix)
print("Среднее значение:", mean_val)
print("Минимум:", min_val)
print("Максимум:", max_val)
print("Сумма по столбцам:", sum_columns)