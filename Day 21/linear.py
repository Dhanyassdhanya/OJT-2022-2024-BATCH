import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# dataset
height = np.array([150,160,164,165,173]).reshape(-1,1)
weight = np.array([50,65,63,68,72])

# create a linear regression model for the above dataset
model = LinearRegression()

# lets fit the model with approprote data
model.fit(height,weight)

predicted_weight = model.predict(height)

print("Intercepts :",model.intercept_)
print("Coefficients :",model.coef_[0])

# create a scatterplot for the above
plt.scatter(height,weight,color='lightblue')
plt.plot(height,predicted_weight,color='pink')
plt.xlabel('Height')
plt.ylabel('Weight')
plt.title('Linear Regression')
plt.show()