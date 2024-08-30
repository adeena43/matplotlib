import matplotlib.pyplot as plt
x = ["python", "C", "C++", "Java"]
y= [85, 67, 70, 80]
z = [95, 80, 89, 55]
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Year 2024", fontsize = 20)

colors = ["yellow","green","blue","magenta"]
plt.bar(x, y, width = 0.4, color=colors, align = "center", edgecolor="black", linewidth = 5, linestyle = ":", alpha = 0.8, label = "2024 update")
plt.bar(x, z, width = 0.4, color=colors, align = "center", edgecolor="black", linewidth = 5, linestyle = ":", alpha = 0.8, label = "2023 update")
plt.legend()
plt.show()
