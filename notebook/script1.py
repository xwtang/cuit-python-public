import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0., 2*np.pi, 361)
y = np.sin(x)

plt.plot(x, y, color='r')
plt.show()
