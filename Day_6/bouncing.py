import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
g = 9.81  # gravity acceleration (m/s^2)
bounce_coefficient = 0.7  # energy loss at each bounce
initial_height = 10  # initial height of the ball (meters)
dt = 0.05  # time step (seconds)

# Ball properties
ball_radius = 0.5
ball_y = initial_height  # initial position
ball_vy = 0.0  # initial vertical velocity

# Create figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, initial_height + 1)
ball, = ax.plot([], [], 'o', markersize=20)

# Initialization function
def init():
    ball.set_data(5, ball_y)
    return ball,

# Update function
def update(frame):
    global ball_y, ball_vy
    
    # Update ball position and velocity
    ball_vy -= g * dt
    ball_y += ball_vy * dt
    
    # Check for bounce
    if ball_y - ball_radius <= 0:
        ball_y = ball_radius
        ball_vy = -ball_vy * bounce_coefficient
    
    ball.set_data(5, ball_y)
    return ball,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=200, init_func=init, blit=True, interval=dt*1000)

plt.show()
