
# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt





# Create the independent variable x to plot all these functions
# Generate input values
x = np.linspace(-10, 10, 100)





# Define Step function
def stepFunction(z):
    return np.where(z >= 0, 1, 0)
# Compute outputs
y_step = stepFunction(x)

# Plot the graph
plt.plot(x, y_step, label='Step Function', color='pink')
plt.title('Step Function')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.show()





# Define Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))
# Compute outputs
y_sigmoid = sigmoid(x)

# Plot the graph
plt.plot(x, y_sigmoid, label='Sigmoid', color='y')
plt.title('Sigmoid')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.show()





# Define Hyperbolic Tangent (tanh) Function
def tanh(z):
    return np.tanh(z)
# Compute outputs
y_tanh = tanh(x)
# Plot the graph
plt.plot(x, y_tanh, label='Tanh', color='g')
plt.title('Tanh')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()





# Define Relu function
def relu(z):
    return np.maximum(0, z)
# Compute outputs
y_relu = relu(x)

# Plot the graph
plt.plot(x, y_relu, label='ReLU', color='r')
plt.title('ReLU')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()





# Define Leaky Relu Function
def leaky_relu(z, alpha=0.01):
    return np.where(z > 0, z, alpha * z)
# Compute outputs
y_leaky_relu = leaky_relu(x)

# Plot the graph
plt.plot(x, y_leaky_relu, label='Leaky ReLU', color='b')
plt.title('Leaky ReLU')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()





# Define Softmax Function
def softmax(z):
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z, axis=0)
# Compute outputs
y_softmax = softmax(x)

# Plot the graph
plt.plot(x, y_softmax, label='Softmax', color='m')
plt.title('Softmax')
plt.xlabel('Input')
plt.ylabel('Output')
plt.grid(True)
plt.legend()
plt.show()





