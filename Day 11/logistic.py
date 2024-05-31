import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Sample data: Feature (independent variable) and Target (dependent variable)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([0, 0, 0, 0, 0, 2, 2, 2, 2, 2])

# Create and train the logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)
y_prob = model.predict_proba(X)[:, 1]

# Plotting the data and the logistic regression curve
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X, y_prob, color='red', label='Logistic Regression')
plt.xlabel('Feature')
plt.ylabel('Probability')
plt.title('Logistic Regression')
plt.legend()
plt.show()

