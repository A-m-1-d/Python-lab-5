import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.title("Гистограмма нормального распределения")
plt.xlabel("Значение")
plt.ylabel("Частота")
plt.grid(True)
plt.savefig("histogram.png")
plt.close()