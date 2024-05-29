import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(loc=0, scale=1, size=1000)  # Generating random data with a normal distribution
sns.histplot(data, kde=True)
plt.title('Histogram of Normal Data Distribution')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
