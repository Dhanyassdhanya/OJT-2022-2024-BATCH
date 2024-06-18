# Gradient Descent Algorithm

# Define the cost function (mean squared error)
def cost_function(m, b, X, Y):
    return sum([(m*x + b - y) ** 2 for x, y in zip(X, Y)]) / len(X)

# Define the gradient descent function
def gradient_descent(X, Y, learning_rate, num_iterations):
    m = 0
    b = 0
    for _ in range(num_iterations):
        m_gradient = sum([-2 * x * (y - (m * x + b)) for x, y in zip(X, Y)]) / len(X)
        b_gradient = sum([-2 * (y - (m * x + b)) for x, y in zip(X, Y)]) / len(X)
        m -= learning_rate * m_gradient
        b -= learning_rate * b_gradient
    return m, b

# Example usage
X = [1, 2, 3, 4, 5]  # independent variable
Y = [2, 4, 5, 4, 5]  # dependent variable

learning_rate = 0.01  # learning rate
num_iterations = 1000  # number of iterations

m, b = gradient_descent(X, Y, learning_rate, num_iterations)

print("Final slope (m):", m)
print("Final intercept (b):", b)