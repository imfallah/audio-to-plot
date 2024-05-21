
#####################################################################
#                             Real-Time voice Plot
#                             github : imfallah
###################################################################

# importing===================================================================================
import queue
import sys
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
#=============================================================================================================================================
# Set the audio input device (change the device number if needed)
device = 0

# Parameters for audio visualization============================================================================================================
window = 1000  # Window size in milliseconds
downsample = 1
channels = [1]
interval = 30

# Initialize a queue for audio data===============================================================================================
q = queue.Queue()

# Query device information=============================================================================================================
device_info = sd.query_devices(device, 'input')
samplerate = device_info["default_samplerate"]

# Calculate the length of the data buffer==========================================================================================
length = int(window * samplerate / (1000 * downsample))

# Initialize the plot data=============================================================================================================================
plotdata = np.zeros((length, len(channels)))

# Create the plot=============================================================================================================================
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_title("Audio To Plot \nGITHUB : imfallah")
lines = ax.plot(plotdata, color=(0, 1, 0.29))

# Audio callback function=============================================================================================================================
def audio_callback(indata, frames, time, status):
    q.put(indata[::downsample, [0]])

# Update plot function
def update_plot(frame):
    global plotdata
    while True:
        try:
            data = q.get_nowait()
        except queue.Empty:
            break
        shift = len(data)
        plotdata = np.roll(plotdata, -shift, axis=0)
        plotdata[-shift:, :] = data
    for column, line in enumerate(lines):
        line.set_ydata(plotdata[:, column])
    return lines

# Set the plot background color
ax.set_facecolor((0, 0, 0))

# Create the audio stream
stream = sd.InputStream(device=device, channels=max(channels), samplerate=samplerate, callback=audio_callback)

# Start the animation
ani = FuncAnimation(fig, update_plot, interval=interval, blit=True)

# Show the plot
with stream:
    plt.show()


