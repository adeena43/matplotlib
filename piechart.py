import matplotlib.pyplot as plt

x = [10, 20, 30, 40]
y = ["Pakistan", "Kenya", "India", "Bangladesh"]

ex = [0.1, 0.1, 0.1, 0.1]
c = ["g","b","o","y"]

plt.pie(x, labels = y, explode=ex, autopct="%0.1f%%",
     shadow = True, radius = 1, labeldistance=1.1, startangle=90,
       textprops={"fontsize":15}, counterclock="True", wedgeprops={"linewidth":4})

plt.title("Languages popularity")
plt.legend(loc = 1)
plt.show()
