import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function to create pie charts
def create_pie_chart(ax, labels, sizes, title):
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    ax.set_title(title)

# Create the main window
root = tk.Tk()
root.title("Dashboard")
root.geometry("1000x600")

# Create a frame for the dashboard
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create a title
title = ttk.Label(main_frame, text="Dashboard", font=("Helvetica", 16))
title.grid(row=0, column=0, columnspan=3, pady=(0, 20))

# Create left frame for buttons
left_frame = ttk.Frame(main_frame, padding="10")
left_frame.grid(row=1, column=0, padx=(0, 20), sticky=(tk.N, tk.S))

# Buttons
buttons = [
    "pedestrian crossing a to b",
    "pedestrian crossing count a to b",
    "speed detection",
    "sleep detection",
    "blind spot detection",
    "traffic sign detection"
]

for i, btn_text in enumerate(buttons):
    button = ttk.Button(left_frame, text=btn_text)
    button.grid(row=i, column=0, pady=5)

# Create right frame for pie charts
right_frame = ttk.Frame(main_frame, padding="10")
right_frame.grid(row=1, column=1, padx=(20, 0), sticky=(tk.N, tk.S, tk.E, tk.W))

# Dummy data for pie charts
labels = ['Bicycle', 'Motorbike', 'Passenger Car', 'Transporter', 'Truck/Bus', 'Long truck']
sizes_a_to_b = [15, 30, 45, 5, 3, 2]
sizes_b_to_a = [5, 25, 50, 10, 8, 2]

# Create matplotlib figure
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 8))

# Create pie charts
create_pie_chart(ax1, labels, sizes_a_to_b, 'Radar classification A -> B')
create_pie_chart(ax2, labels, sizes_b_to_a, 'Radar classification B -> A')

# Embed the matplotlib figure in Tkinter canvas
canvas = FigureCanvasTkAgg(fig, master=right_frame)
canvas.draw()
canvas.get_tk_widget().pack()

# Run the Tkinter event loop
root.mainloop()
