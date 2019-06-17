import scipy.interpolate as interp
import numpy as np, matplotlib.pyplot as plt
from scipy.interpolate import interp1d
x= np.array([0, 1, 2, 3, 4, 5, 6, 7])
y= np.array([3, 4, 3.5, 2, 1, 1.5, 1.25, 0.9])
xx = np.linspace(x.min(), x.max(), 100)
fig, ax = plt.subplots(figsize=(8, 4))
ax.scatter(x, y)
for n in ['linear','zero', 'slinear', 'quadratic', 'cubic']:
    f = interp.interp1d(x, y, kind = n)
    ax.plot(xx, f(xx), label= n)
ax.legend()
ax.set_ylabel(r"$y$", fontsize=18)
ax.set_xlabel(r"$x$", fontsize=18)
plt.show()