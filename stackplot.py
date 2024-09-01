import matplotlib.pyplot as plt

x = [1,2,3,4,5,6]

area1 =[5,4,2,3,6,3]
area2 = [3,4,5,6,3,2]
area3 = [1,5,3,2,4,6]

l = ["area1", "area2", "area3"]

plt.stackplot(x, area1, area2, area3, labels = l, colors = ["pink", "yellow", "blue"])

plt.title("Python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc = 2)
plt.grid()
plt.show()
