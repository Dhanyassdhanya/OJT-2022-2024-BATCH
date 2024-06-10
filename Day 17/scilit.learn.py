# Fit a linear regression model using scikit-learn for the data points x = [1, 2, 3, 4, 5] and y = [2, 3, 5, 7, 11]. Predict the value of y when x = 6.

import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Create the data points
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Reshape for sklearn
y = np.array([2, 3, 5, 7, 11])

# Step 2: Fit the linear regression model
model = LinearRegression()
model.fit(x, y)

# Step 3: Predict the value of y when x = 6
x_new = np.array([[6]])
y_pred = model.predict(x_new)

print(f"Predicted value of y when x = 6: {y_pred[0]}")
