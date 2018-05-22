import matplotlib.pyplot as plt
import numpy as np
import math

flg, ax = plt.subplots()

text = "0 12 12 12 1 19 46 19 2 37 10 10 3 49 89 22 4 57 40 17 5 96 42 19 6 132 15 15 7 169 20 20 8 60 10 10 9 168 61 19 10 92 82 19 11 130 55 13 12 130 86 16 13 83 10 10 14 168 102 20 15 87 118 14 16 120 120 16 17 122 156 18 18 10 186 10 19 18 153 18 20 164 160 22 21 59 155 20"

numbers = map(int, text.split())
grouped = list(zip(*[iter(numbers)] * 4))
for g in grouped:
	circle = plt.Circle((g[1],g[2]), g[3])
	ax.add_artist(circle)
	plt.text(g[1]-4,g[2]-4, g[0])
	
axes = plt.gca()
axes.set_xlim([0,200])
axes.set_ylim([0,200])
plt.grid(True)
plt.show()
