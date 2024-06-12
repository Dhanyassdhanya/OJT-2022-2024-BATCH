import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2,3,6,7,10]

# create a plot with marker
plt.plot(x, y,marker='X',linestyle='-.',color='b',
         markersize=6,markerfacecolor='r')

# Add the label as well as title
plt.title("Line plot with markers")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()