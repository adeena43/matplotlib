import matplotlib.pyplot as plt

# Data to plot
x = [1, 2, 3, 4, 5, 6]
y = [3, 4, 5, 2, 1, 2]

# Create the stem plot
plt.stem(
    x, y,                      # Data points
    linefmt=":",               # Line format (dotted lines)
    markerfmt="r+",            # Marker format (red plus signs)
    basefmt="g",              # Base line format (green)
    bottom=0,                  # Baseline for the stems
    label="python",            # Label for the legend
    
    orientation="horizontal"  # Orientation of the stems
)

# Add a legend to the plot
plt.legend()

# Display the plot
plt.show()
