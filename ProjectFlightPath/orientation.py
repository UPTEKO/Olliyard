import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import atan2, asin, degrees
import math
from matplotlib.widgets import Slider
import numpy as np

# Read the CSV file
data = pd.read_csv('data_orig/drone_local_position_unformated.csv')

# Extract time, orientation, and convert time to only include time part
time = pd.to_datetime(data['time']).dt.time
orientation = data['pose'].apply(lambda x: eval(x)['orientation'])

def euler_from_quaternion(x, y, z, w):
    """
    Convert a quaternion into euler angles (roll, pitch, yaw)
    roll is rotation around x in radians (counterclockwise)
    pitch is rotation around y in radians (counterclockwise)
    yaw is rotation around z in radians (counterclockwise)
    """
    t0 = +2.0 * (w * x + y * z)
    t1 = +1.0 - 2.0 * (x * x + y * y)
    roll_x = atan2(t0, t1)
    t2 = +2.0 * (w * y - z * x)
    t2 = +1.0 if t2 > +1.0 else t2
    t2 = -1.0 if t2 < -1.0 else t2
    pitch_y = asin(t2)
    t3 = +2.0 * (w * z + x * y)
    t4 = +1.0 - 2.0 * (y * y + z * z)
    yaw_z = atan2(t3, t4)
    return roll_x, pitch_y, yaw_z  # in radians

# Initialize the plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the initial orientation
initial_orientation = euler_from_quaternion(
    orientation.iloc[0]['x'],
    orientation.iloc[0]['y'],
    orientation.iloc[0]['z'],
    orientation.iloc[0]['w']
)

# Create three arrows for roll, pitch, and yaw
roll_arrow = ax.quiver(0, 0, 0, 1, 0, 0, length=0.1, normalize=True, color='r', label='Roll')
pitch_arrow = ax.quiver(0, 0, 0, 0, 1, 0, length=0.1, normalize=True, color='g', label='Pitch')
yaw_arrow = ax.quiver(0, 0, 0, 0, 0, 1, length=0.1, normalize=True, color='b', label='Yaw')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
title_text = ax.set_title('')  # Create an empty title text
ax.legend()

# Create a slider for selecting the time
slider_ax = plt.axes([0.2, 0.1, 0.6, 0.03])
slider = Slider(slider_ax, 'Index', 0, len(data) - 1, valinit=0, valstep=1)

# Add a text annotation for direction
direction_text = ax.text2D(0.05, 0.95, '', transform=ax.transAxes)

# Add a text annotation for up and down
vertical_text = ax.text2D(0.05, 0.9, '', transform=ax.transAxes)

# Update the plot based on the selected time
def update(val):
    global roll_arrow, pitch_arrow, yaw_arrow  # Add global keyword here
    index = int(slider.val)
    orientation_values = euler_from_quaternion(
        orientation.iloc[index]['x'],
        orientation.iloc[index]['y'],
        orientation.iloc[index]['z'],
        orientation.iloc[index]['w']
    )
    print("                 { roll_x | pitch_y | yaw_z }")
    print(math.degrees(orientation_values[0]), math.degrees(orientation_values[1]), math.degrees(orientation_values[2]))
    print(orientation_values)
    print("                       { x | y | z | w }")
    print(orientation.iloc[index]['x'], orientation.iloc[index]['y'], orientation.iloc[index]['z'], orientation.iloc[index]['w'])
    print("----------------------------------------------------------------")

    # Update the roll arrow
    roll_arrow.set_segments([[[0, 0, 0], [np.cos(orientation_values[0]), np.sin(orientation_values[0]), 0]]])

    # Update the pitch arrow
    pitch_arrow.set_segments([[[0, 0, 0], [0, np.cos(orientation_values[1]), np.sin(orientation_values[1])]]])

    # Update the yaw arrow
    yaw_arrow.set_segments([[[0, 0, 0], [np.sin(orientation_values[2]), 0, np.cos(orientation_values[2])]]])

    # Calculate the direction based on the yaw angle
    yaw_degrees = degrees(orientation_values[2])
    if -45 <= yaw_degrees < 45:
        direction = 'Forward'
    elif 45 <= yaw_degrees < 135:
        direction = 'Right'
    elif -135 <= yaw_degrees < -45:
        direction = 'Left'
    else:
        direction = 'Backwards'

    direction_text.set_text(f'Direction: {direction}')  # Update the direction text

    # Calculate the vertical direction based on the pitch angle
    pitch_degrees = degrees(orientation_values[1])
    if pitch_degrees > 0:
        vertical = 'Up'
    else:
        vertical = 'Down'

    vertical_text.set_text(f'Vertical: {vertical}')  # Update the vertical text

    title_text.set_text(f'Drone Orientation at Time: {time.iloc[index]}')  # Update the title text
    fig.canvas.draw_idle()

slider.on_changed(update)

# Add a red circle in the middle
ax.scatter(0, 0, 0, c='red', s=100)

plt.show()
