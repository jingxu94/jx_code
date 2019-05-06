# @Time : 2019/1/15 10:46 
# @Author : Jing Xu

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


# Initial setting
filename = r"obs_b01.txt"

mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'

families=[ 'fantasy','Tahoma', 'monospace', 'Times New Roman']
styles = ['normal', 'italic', 'oblique']
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']

plt.rcParams['font.family'] = families[3]
plt.rcParams['font.style'] = styles[0]
plt.rcParams['font.weight'] = weights[4]


def tickline():
	ax = plt.gca()
	ax.spines['right'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['bottom'].set_linewidth(2)
	ax.spines['left'].set_linewidth(2)
	ax.tick_params(which="major",width=2,length=5)
	ax.tick_params(which="minor",width=2,length=4)
	ax.set_xlim(1e-6, 1e-1)
	ax.set_ylim(1e-8, 1e-2)
	return ax

# Import data
origin_data = np.loadtxt(filename)
x = origin_data[:,0]; y = origin_data[:,1]

# Decay curve
plt.figure(figsize=(12,12), dpi=80, facecolor='w', edgecolor='k')
plt.plot(x, y, color="k")
plt.xscale('log')
plt.yscale('log')
ax = tickline()
plt.xticks(fontsize=36)
plt.yticks(fontsize=36)
# ax.set_xlabel.labelpad = 100
ax.set_xlabel('t/s', fontsize=36)
ax.set_ylabel(r'$\partial$B$_z$(t)/$\partial$t(V$\cdot$m$^{-1}$)', fontsize=36)
plt.savefig('DecayCurve.png')
plt.show()



