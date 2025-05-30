import numpy as np
import matplotlib.pyplot as plt

matrix = np.random.randint(1, 11, (5, 5))
plt.figure()
plt.imshow(matrix, cmap='hot', interpolation='nearest')
plt.colorbar()
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        plt.text(j, i, str(matrix[i, j]), ha='center', va='center', color='white')
plt.title("Тепловая карта матрицы")
plt.savefig("heatmap.png")
plt.close()