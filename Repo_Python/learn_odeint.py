# @Time : 2018/12/3 17:05 
# @Author : Jing Xu

import numpy as np
import scipy
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import brentq
from scipy.optimize import fsolve
import pylab
import matplotlib.pyplot as plt

miu = 0.25
x1 = 0
x2 = 0
r1 = 6000
r2 = 8000

x0 = 0
y0 = 0
vx = 6
vy = 8

u0 = [x0, y0, 0, vx, vy, 0]

def deriv(u, dt):
    return [u[3], u[4], u[5],
            ((2 * u[4] + u[0] - (1 - miu) * (u[0] - x1)/r1**3) - miu * (u[0] - x1)/r2**3),
            (-2 * u[4] + u[1] - (1 - miu) * u[1] / r1 ** 3 - miu * u[1] / r2 ** 3),
            0]

dt = np.linspace(0.0, 500.0, 500.0)  #  secs to run the simulation
u = odeint(deriv, u0, dt)

x, y, z, x2, y2, z2 = u.T

# new a figure and set it into 3d
fig = plt.figure()
ax = fig.gca(projection='3d')

# set figure information
ax.set_title("3D_Track")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# draw the figure, the color is r = read
figure = ax.plot(x, y, z, c='r')

plt.show()