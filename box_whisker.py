import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50, 60, 70]
x1 = [10, 20, 30, 40, 50, 60, 90]

y = [x, x1]
plt.boxplot(y, labels = ["Python", "C++"], showmeans=True,
            sym="g+", boxprops=dict(color="r"),
            whiskerprops=dict(color="pink"))

plt.show()
