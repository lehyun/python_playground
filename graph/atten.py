import matplotlib.pyplot as plt
import numpy as np
import math

# Beer's Law
def atten1(i, a, d):
	return i * math.exp(-math.log(a)*d)

# 거리 제곱의 반비례
def atten2(i, a, d):
	return i / (1 + math.pow(d, 2))

x = np.arange(0, 10, 0.1)

y1 = [atten1(10, 1.8, xd) for xd in x]
y2 = [atten2(10, 0, xd) for xd in x]
plt.plot(x, y1, label="Beer's Law")
plt.plot(x, y2, label="1 / (1 + distance^2)")
# Place a legend above this subplot, expanding itself to
# fully use the given bounding box.
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=1, mode="expand", borderaxespad=0.)
plt.xlabel('Distance')
plt.ylabel('Intensity')
plt.text(2, 8, r'$A=1.8,\ I=10$')
plt.show()
