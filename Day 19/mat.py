import matplotlib.pyplot as plt


# dataset
x = [1,2,3,4,5]
y = [2,3,5,7,11]

# Create a plot for our data
plt.plot(x,y)
# customization for the plot

# Add a titile
plt.title("Line Plot")

# Add the lables
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Output the plot
plt.show()
