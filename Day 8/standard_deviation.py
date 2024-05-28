# Practice the programs with Machine Learning - Standard Deviation using python Jupiter Notebook

# Importing necessary libraries
import numpy as np
import pandas as pd

# Data
data = [10, 12, 23, 23, 16, 23, 21, 16]

# Using NumPy to calculate standard deviation
std_dev_numpy = np.std(data)
print("Standard Deviation using NumPy: ", std_dev_numpy)

# Using Pandas to calculate standard deviation
df = pd.DataFrame({'values': data})
std_dev_pandas = df['values'].std()
print("Standard Deviation using Pandas: ", std_dev_pandas)
