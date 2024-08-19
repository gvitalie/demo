import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 201)
y = 3 * np.sin(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b')
plt.ylabel('Amplitude')
plt.ylabel('x')
plt.grid()
plt.show()
