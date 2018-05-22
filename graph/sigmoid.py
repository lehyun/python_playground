import matplotlib.pyplot as plt
import numpy as np
import math
def sigmoid(x):
	return 1 / (1 + math.exp(-x))

x = np.arange(-10, 10, 0.1)
y = [sigmoid(xd) for xd in x]
plt.plot(x, y)
plt.show()
