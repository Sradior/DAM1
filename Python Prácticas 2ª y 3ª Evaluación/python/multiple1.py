import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axs = plt.subplots(3, 4)

axs[0, 0].plot(x, y)
axs[0, 1].plot(x, y)
axs[0, 2].plot(x, -y)
axs[0, 3].plot(x, -y)

axs[1, 0].plot(x, -y)
axs[1, 1].plot(x, y)
axs[1, 2].plot(x, y)
axs[1, 3].plot(x, y)

axs[2, 0].plot(x, -y)
axs[2, 1].plot(x, -y)
axs[2, 2].plot(x, -y)
axs[2, 3].plot(x, -y)

for ax in axs.flat:
    ax.set(xlabel='x-label', ylabel='y-label')
for ax in axs.flat:
    ax.label_outer()

plt.show()
