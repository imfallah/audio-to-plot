<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<h1 align="center">AUDIO TO PLOT💟</h1>

### 🌏 Readme in [فارسی](https://github.com/jokernets/audiotoplot/blob/main/Fa.md)

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<p align="center">
<img src="https://img.shields.io/badge/language-python-blue?style"/><img src="https://img.shields.io/github/stars/jokernets/audiotoplot"/><img src="https://img.shields.io/github/forks/imfallah/audio-to-plot"/>
</p>

   



Table of contents✅✔
=================

<!--ts-->
* 🔸[Installation](#installation)

* ⚫[requriment](https://github.com/imfallah/audiotoplot/blob/main/requriments.md)

* 🔸[Anilayes Code📈](#analiys-code-)
   * 💫[Importing✔](#importing)
   * 💫[Set Variable✔](#set-variable)
   * 💫[Audio Input✔](#audio-input)
   * 💫[Define✔](#define)
   * 💫[Set Plot✔](#set-plot)
  
* 🔸[Mor Example💯](#more-examples-and-showcase-)
   * 🥇[Project Video📺](#video-image-of-the-app-)
    
* 🎁[`CONNECT ME🎃`](#connect-me)
<!--te-->













# Installation

## Install the Library with pip:

```python
pip install matplotlib
pip install queuelib
pip install os-sys
pip install sounddevice
```

Update existing installation:`pip3 install (YOUR LIBRARY) --upgrade`
(update as often as possible because this library is under active development)


> [!IMPORTANT]
> # read completely:)



# Analiys Code🎃:



## `importing`♻🔰:

```python
import queue
import sys
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

```
## `ُSet Variable`:
- This part of the code defines a variable named ``device'' whose initial value is equal to 0.
- Then parameters related to audio visualization such as `window', `downsample', `channels', and `interval' are defined.
- Finally, a queue named `q' is created, which is used to store sound data.
```python
# Set the audio input device (change the device number if needed)
device = 0
# Parameters for audio visualization
window = 1000  # Window size in milliseconds
downsample = 1
channels = [1]
interval = 30
# Initialize a queue for audio data
q = queue.Queue()
```
## `Audio Input` :
- In this part of the code, first, the information of the input device with ``device'' number is extracted.
    - Then the sampling rate is calculated for the desired device.
    - The length of the data required for sound visualization is also calculated according to the ``window'', ``downsample'' and ``samplerate'' parameters.
    - Finally, a graph with specified dimensions (8 x 4) is created and graph lines are drawn with green color (0, 1, 0.29).
```python
# Query device information
device_info = sd.query_devices(device, 'input')
samplerate = device_info["default_samplerate"]
# Calculate the length of the data buffer
length = int(window * samplerate / (1000 * downsample))
# Initialize the plot data
plotdata = np.zeros((length, len(channels)))
# Create the plot
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_title("Audio To Plot \nGITHUB : Jokernets")
lines = ax.plot(plotdata, color=(0, 1, 0.29))
```
## `Define` :  
1. **Audio callback function ('audio_callback'):**
      - This function is probably used to manage audio data.
      - takes "indata", "frames", "time" and "status" as parameters.
      - Inside the function, it looks like it will pull down the audio data and store it in a queue (`q`).
      - The downsample factor is defined as 'downsample'.
      - The processed audio data is then used for visualization.

2. **update plot function ('update_plot'):**
      - This function updates a graph (probably a real-time audio visualization).
      - retrieves the audio data from the queue (q) and modifies it.
      - The moved data is then assigned to "plotdata".
      - Finally, it updates the y data of each line in the graph.

3. **Global variables:**
      - `plotdata`: a numpy array (with leading zeros) to store audio data.
      - `q`: a queue to store the sampled audio data.
      - `lines': a list of Line2D objects (possibly to draw).

Please note that some placeholders (such as 'lines', 'dataprot' and actual rendering code) should be replaced with actual data and objects. This piece is meant to be integrated into a larger program that handles audio imaging.

```python
# Audio callback function
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
```

## `Set Plot`:
ax.set_facecolor((0, 0, 0)): This line of code sets the background color of an object (axis) of the set in the map. Here, the color specified by RGB (0, 0, 0) is black. In other words, this line of code will make the background black.
ani = FuncAnimation(fig, update_plot, interval=interval, blit=True): This line of code is used to create an animation in the plot. This line of code contains the FuncAnimation function and some statements of the fig object (the object containing the graph), the update_plot function (which is responsible for changing the graph), the distance between each animation frame (distance) and blit=True (ie). only from changes that have changed) as input.
```python
# Set the plot background color
ax.set_facecolor((0, 0, 0))
# Create the audio stream
stream = sd.InputStream(device=device, channels=max(channels), samplerate=samplerate, callback=audio_callback)
# Start the animation
ani = FuncAnimation(fig, update_plot, interval=interval, blit=True)
# Show the plot
with stream:
    plt.show()
```
<img src=""><br><br><img src="https://github.com/jokernets/audiotoplot/blob/main/Figure12024-04-2320_33_05.png" width="500" height="300"><img src=""><br><br>

## More Examples and Showcase 👑

### Video image of the APP 📺
<img src="" width="400" height="300">


# `𝐂𝐨𝐧𝐧𝐞𝐜𝐭 𝐌𝐞`🎈🎃

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammadfallahnejad/" height="40" width="60" /></a>
































































   


