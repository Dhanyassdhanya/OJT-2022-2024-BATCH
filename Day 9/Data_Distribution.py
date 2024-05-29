import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1, size=1000)  # Generating random data with a normal distribution
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram of Normal Data Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
