import matplotlib.pyplot as plt
day = [1,2,3,4,5,6,7]
no = [2,3,4,5,6,7,8]
no2 = [12,3,4,5,6,7,8]
colors = [10,49,30,29,56,20,30]
sizes = [400,200,400,300,200,100,600]
plt.scatter(day, no, c=colors, s=sizes, cmap = "viridis", alpha=0.5)
plt.scatter(day, no2, color = "r", s=sizes, cmap = "viridis", alpha=0.5)
t= plt.colorbar()
t.set_label("ColorBar", fontsize=15)
plt.title("Scatter Plot", fontsize = 15)
plt.xlabel("Day", fontsize = 15)
plt.ylabel("Number", fontsize=15)
plt.show()
