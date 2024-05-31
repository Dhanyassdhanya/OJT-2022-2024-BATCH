import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 3.5, 2.8, 4.6, 5.0])

# Initialize and fit the model
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)
    
# Plotting the data and the regression line
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.show()











