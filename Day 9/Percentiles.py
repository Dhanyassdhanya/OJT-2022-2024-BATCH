import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a box plot
sns.boxplot(data=data)

# Add percentiles to the plot
plt.axhline(y=np.percentile(data, 25), color='r', linestyle='--', label='25th Percentile')
plt.axhline(y=np.percentile(data, 50), color='g', linestyle='--', label='50th Percentile')
plt.axhline(y=np.percentile(data, 75), color='b', linestyle='--', label='75th Percentile')

plt.legend()
plt.show()