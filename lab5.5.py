import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 3, figsize=(15, 4))

x_vals = np.linspace(-10, 10, 100)
axs[0].plot(x_vals, x_vals**2, color='green')
axs[0].set_title("y = x^2")
axs[0].grid(True)

x_rand = np.random.rand(50)
y_rand = np.random.rand(50)
axs[1].scatter(x_rand, y_rand, color='purple')
axs[1].set_title("Случайные точки")
axs[1].grid(True)

categories = ['A', 'B', 'C']
values = [3, 7, 2]
axs[2].bar(categories, values, color='orange')
axs[2].set_title("Категориальные данные")
axs[2].grid(True)

plt.tight_layout()
plt.savefig("subplots.png")
plt.close()