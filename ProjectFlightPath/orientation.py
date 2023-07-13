import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import atan2, asin, degrees
from matplotlib.widgets import Slider

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
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the initial orientation
initial_orientation = euler_from_quaternion(
    orientation.iloc[0]['x'],
    orientation.iloc[0]['y'],
    orientation.iloc[0]['z'],
    orientation.iloc[0]['w']
)
quiver = ax.quiver(0, 0, 0, initial_orientation[0], initial_orientation[1], initial_orientation[2],
                   length=0.1, normalize=True, color='r', label='Drone Orientation')
ax.set_xlabel('Roll')
ax.set_ylabel('Pitch')
ax.set_zlabel('Yaw')
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
    global quiver
    index = int(slider.val)
    orientation_values = euler_from_quaternion(
        orientation.iloc[index]['x'],
        orientation.iloc[index]['y'],
        orientation.iloc[index]['z'],
        orientation.iloc[index]['w']
    )
    quiver.remove()  # Remove the previous quiver plot
    quiver = ax.quiver(0, 0, 0, orientation_values[0], orientation_values[1], orientation_values[2],
                       length=0.1, normalize=True, color='r', label='Drone Orientation')
    title_text.set_text(f'Drone Orientation at Time: {time.iloc[index]}')  # Update the title text

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

    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
