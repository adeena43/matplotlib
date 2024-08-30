import matplotlib.pyplot as plt
import numpy as np

# Provided number list
number = [25, 18, 14, 41, 10, 20, 53, 27, 34, 37, 33, 46, 59, 12, 15, 54, 23, 27, 45, 49, 37, 
          14, 40, 51, 55, 20, 35, 54, 14, 27, 24, 32, 21, 15, 14, 55, 49, 11, 46, 16, 42, 58, 
          38, 29, 53, 10, 11, 23, 16, 16]

# Bin edges
bins = [10, 20, 30, 40, 50, 60]

# Plotting the histogram
plt.figure(figsize=(10, 6))  # Set the figure size
plt.hist(number, color="blue", bins=bins, edgecolor="black", bottom=10, cumulative=-1, histtype="stepfilled", label="Python")
plt.axvline(45, color="red", linestyle="--", label="Threshold 45")  # Adding a vertical line with a label
plt.title("Python Histogram")
plt.xlabel("Value")
plt.ylabel("Cumulative Frequency")
plt.legend()  # Add legend to the plot
plt.grid(True)  # Add grid for better readability
plt.show()  # Display the plot
