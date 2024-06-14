# Staring point
# learning rate alpha
# number of iterations

# example of gradient descent
x=10
leaning_rate = 0.1
num_iteration = 100

# create a loop for gradiant descent

for i in range(num_iteration):
    # compute the gradient
    gradient = 2*x
    # update the x with new parameters that is new x
    x = x - leaning_rate * gradient
    print(f"Iteration {i+1}, x = {x:.4f}, gradient")

print("minimum  value of the x: ", x)
