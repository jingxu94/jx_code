# @Time : 2018/4/4 9:16 
# @Author : Jing Xu

x_grid = [-500,-300,-200,-140,-100,-80,-60,-42,-34,-30,-28,-27,-26,-25.5,-25,-24.5,-24,-23,-22,-21,-20.5,-20,-19.5,-19,
          -18,-17,-16,-15.5,-15,-14.5,-14,-13,-12,-11,-10.5,-10,-9.5,-9,-8,-7,-6.5,-6,-5.6,-5.4,-5.2,-5,-4.8,-4.5,-4,-3,
          -2,-1,0,1,2,3,4,4.5,4.8,5,5.2,5.4,5.6,6,6.5,7,8,9,9.5,10,10.5,11,12,13,14,14.5,15,15.5,16,17,18,19,19.5,20,
          20.5,21,22,23,24,24.5,25,25.5,26,27,28,30,34,42,60,80,100,140,200,300,500]

for i in range(len(x_grid)-1):
	x_grid[i] = round(x_grid[i]*1.0,1)

def set_source(x_point):
	source_list = []
	for i in range(13):
		source_list.append(round(x_point-1.2+0.2*i,1))

	for i in range(13):
		for j in range(len(x_grid)-1):
			if x_grid[j] <= source_list[i] and x_grid[j+1] > source_list[i]:
				x_grid.insert(j+1,source_list[i])
				break

	new_xgrid = []
	for id in x_grid:
		if id not in new_xgrid:
			new_xgrid.append(id)
	# print(new_xgrid)
	return new_xgrid

xgrid = set_source(1.0)

with open("xgrid.txt","w") as f:
	f.write(str(len(xgrid)))
	f.write("\n")
	for i in x_grid:
		f.write(str(i))
		f.write("\n")
