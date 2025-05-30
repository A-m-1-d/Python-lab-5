import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)
z = np.cos(x)

plt.figure()
plt.plot(x, y, label='sin(x)')
plt.plot(x, z, label='cos(x)')
plt.xlabel("x")
plt.ylabel("Значение")
plt.title("Графики sin(x) и cos(x)")
plt.legend()
plt.grid(True)
plt.savefig("plot_sin_cos.png")
plt.close()