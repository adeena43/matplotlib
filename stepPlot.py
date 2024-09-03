import matplotlib.pyplot as plt

x = [100,200,300,400,500,600]

y= [3,2,1,6,5,4]

plt.step(x, y, color="r", marker = "o", ms=10, mfc="g", label = "Python")

plt.title("Python")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend(loc=2)
plt.grid()
plt.show()
