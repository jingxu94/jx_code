#__author:  "Jing Xu"
#date:  2018/2/1

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as pl

x = np.linspace(0, 10, 11)
y = np.sin(x)
xnew = np.linspace(0, 10, 101)
pl.plot(x, y, 'ro')
for kind in ['nearest', 'zero', 'slinear', 'quadratic']:
	f = interpolate.interp1d(x, y, kind=kind)
	ynew = f(xnew)
	pl.plot(xnew, ynew, label=str(kind))
pl.legend(loc='lower right')
pl.show()