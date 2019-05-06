import numpy as np 
import matplotlib.pyplot as plt 

fname = 'halfspace.dat'
data  = np.loadtxt(fname)

t = data[:,0]
b = data[:,1]
d = data[:,1]

# Initial setting
# mpl.rcParams['xtick.direction'] = 'in'
# mpl.rcParams['ytick.direction'] = 'in'

families=[ 'fantasy','Tahoma', 'monospace', 'Times New Roman']
styles = ['normal', 'italic', 'oblique']
weights = ['light', 'normal', 'medium', 'semibold', 'bold', 'heavy', 'black']

# plt.rcParams['font.family'] = families[1]
# plt.rcParams['font.style'] = styles[0]
plt.rcParams['font.weight'] = weights[3]

def tickline():
	ax = plt.gca()
	ax.spines['right'].set_linewidth(1.5)
	ax.spines['top'].set_linewidth(1.5)
	ax.spines['bottom'].set_linewidth(1.5)
	ax.spines['left'].set_linewidth(1.5)
	# ax.tick_params(which="major",width=2,length=5)
	# ax.tick_params(which="minor",width=2,length=4)
	# ax.set_xlim(min(x), 1e-2)
	# ax.set_ylim(1e-10, 1e-2)
	return ax


plt.figure(figsize = (8,8), dpi = 100, edgecolor = 'k')
plt.loglog(t, b, color = 'b', label='analytic solution')
plt.scatter(t, d, s = 30, c = '#FF00FF')
# plt.loglog(t, d, 'o--', MarkerSize = 4, color = '#FF00FF', label='numerical solution')

# plt.scatter(t, d, alpha=0.5, color = '#FF00FF', label='numerical solution')
# plt.scatter(t, d)
# plt.xscale('log')
# plt.yscale('log')
ax = tickline()
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
ax.set_xlabel('T/s', fontsize=18)
ax.set_ylabel(r'$\partial$B$_z$(t)/$\partial$t(V$\cdot$m$^{-1}$)', fontsize=18)

plt.legend(loc = 'upper right', frameon = False)
plt.grid(True)
plt.show()