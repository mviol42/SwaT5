import matplotlib.pyplot as plt
import numpy as np

x_axis = [1000, 10000, 100000, 1000000]
no_repeats_same_roots = [0.007, 0.59, 0.859, 0.888]
new_roots = [0.015, 0.392, 0.382, 0.394]
repeats_same_roots = [0.018, 0.649, 0.876, 0.9]

plt.plot(x_axis, new_roots, label='new roots')
plt.plot(x_axis, no_repeats_same_roots, label='new words, seen roots')
plt.plot(x_axis, repeats_same_roots, label='seen words, seen roots')
plt.xlabel("number of data points")
plt.ylabel("accuracy")
plt.title(f"number of data points vs accuracy")
plt.xscale('log')
plt.ylim(0, 1)
plt.savefig("plot all.png")
plt.legend()
plt.show()
