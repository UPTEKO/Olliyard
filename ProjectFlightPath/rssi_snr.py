import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Read the CSV files
df = pd.read_csv('data_orig/rssi_air.csv')
df_snr = pd.read_csv('data_orig/snr_air.csv')

# Merge the data based on 'time' column
# df_merged = pd.merge(df, df_snr, on='time', how='inner')

# Convert columns to NumPy arrays
rssi_time = df['time'].str[17:19].to_numpy()
rssi_data = df['data'].to_numpy()
snr_time = df_snr['time'].str[17:19].to_numpy()
snr_data = df_snr['data'].to_numpy()

# Set up the figure and subplots
# fig, ax_snr = plt.subplots(1, 1, figsize=(10, 8), sharex=True)
# fig, ax_rssi = plt.subplots(1, 1, figsize=(10, 8), sharex=True)
fig, (ax_rssi, ax_snr) = plt.subplots(2, 1, figsize=(10, 8))#, sharex=True)
plt.subplots_adjust(top=0.9, bottom=0.3, left=0.1, right=0.9, hspace=0.4)

# Set the initial index value
initial_index = 0

# Create the slider
ax_index = plt.axes([0.2, 0.2, 0.6, 0.03], facecolor='lightgoldenrodyellow')
slider_index = Slider(ax=ax_index, label='Index', valmin=0, valmax=len(rssi_time)-1,
                      valinit=initial_index, valstep=1)

# Function to update the graphs when the slider is changed
def update(val):
    index = int(slider_index.val)
    selected_rssi_time = rssi_time[:index + 1]
    selected_rssi = rssi_data[:index + 1]
    selected_snr_time = snr_time[:index + 1]
    selected_snr = snr_data[:index + 1]

    ax_rssi.clear()
    ax_snr.clear()
    ax_rssi.plot(selected_rssi_time, selected_rssi, color='blue')
    ax_rssi.set_xlabel('Time (sec)')
    ax_rssi.set_ylabel('RSSI')
    ax_rssi.set_title('RSSI')

    ax_snr.plot(selected_snr_time, selected_snr, color='green')
    ax_snr.set_xlabel('Time (sec)')
    ax_snr.set_ylabel('SNR')
    ax_snr.set_title('SNR')

    ax_snr.text(0.5, -0.2, f'Time: {snr_time[index]}', transform=ax_snr.transAxes, ha='center', fontsize=10)

    fig.canvas.draw_idle()

slider_index.on_changed(update)

# Initialize the graphs
update(initial_index)

# Set the figure size
fig.set_size_inches(10, 8)

# Display the plot
plt.show()
