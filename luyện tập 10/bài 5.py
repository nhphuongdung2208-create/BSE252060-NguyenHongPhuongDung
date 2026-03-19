import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,5))

ax1.plot(x, x**2)
ax1.set_title("y = x^2")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

ax2.plot(x, np.sqrt(x))
ax2.set_title("y = sqrt(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

plt.tight_layout()
plt.show()