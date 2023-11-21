# Importing required library
import numpy as np
import matplotlib.pyplot as plt

# Creating x axis with range and y axis 
# Function for Plotting Sine and Cosine Graph
x = np.arange(0, 5 * np.pi, 0.1)
y1 = np.sin(2*x)

# Plotting Sine Graph
plt.plot(x, y1, color='green')
plt.savefig("sine_test.png")

# Source Provided By
# https://www.geeksforgeeks.org/plotting-sine-and-cosine-graph-using-matloplib-in-python/
