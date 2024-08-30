import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
x1 = [40, 30, 20, 10]
y = ["Pakistan", "Kenya", "India", "Bangladesh"]

ex = [0.1, 0.1, 0.1, 0.1]
c = ["g","b","o","y"]

plt.pie(x, labels = y, radius = 1.5)
plt.pie([1], colors = "w")

plt.title("Languages popularity")
plt.legend(loc = 1)
plt.show()
