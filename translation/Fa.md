<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<h1 align="center">تبدیل صوت به نمودار✨</h1>

### 🌏 مطالعه مفاله به [English](https://github.com/jokernets/audiotoplot/blob/main/README.md)

<img src="https://github.com/jokernets/audiotoplot/blob/main/pic.png">
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>
<p align="center">
<img src="https://img.shields.io/badge/language-python-blue?style"/><img src="https://img.shields.io/github/stars/jokernets/audiotoplot"/><img src="https://img.shields.io/github/forks/jokernets/audiotoplot"/>
</p>

   



فهفهرست مطالب✅✔


<!--ts-->
* 🔸[نصب کن!]()
* 
* ⚫[الزامات ورژن ها](https://github.com/imfallah/audiotoplot/blob/main/requriments.md)

* 🔸آنالیز کد📈](-)
  * 💫[ورودی کد]()
  * 💫[چک کردن متغیر ها ✔]()
  * 💫[ورودی های صدا✔]()
  * 💫[تابع✔]()
  * 💫[ساختن نمودار✔]()
  
* 🔸[ویترین💯]()
  * 🥇[ویدوی از پروژه📺]()
    
* 🎁[`ارتباط با من 🎃`]()
<!--te-->













# نصب کن !

## ماژول ها رو با استفاده از pip نصب کن:

```python
pip install matplotlib
pip install queuelib
pip install os-sys
pip install sounddevice
```

نصب موجود را به روز کنید: pip3 install (کتابخانه شما) -- ارتقاء دهید (تا حد امکان به روز رسانی کنید زیرا این کتابخانه در حال توسعه فعال است)

> [!IMPORTANT]
> # تا آخرشو بخون :)



# آنالیز کدد ها 🎃:



## `ایمپورت`♻🔰:

```python
import queue
import sys
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd

```
## «تنظیم متغیر»:
- این قسمت از کد متغیری به نام "دستگاه" را تعریف می کند که مقدار اولیه آن برابر با 0 است.
- سپس پارامترهای مربوط به تصویرسازی صوتی مانند 'window'، 'downsample'، 'channels' و 'interval' تعریف می شوند.
- در نهایت یک صف با نام 'q' ایجاد می شود که برای ذخیره داده های صدا استفاده می شود.
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
## 'ورودی صوتی':
- در این قسمت از کد ابتدا اطلاعات دستگاه ورودی با شماره ``دستگاه` استخراج می شود.
     - سپس میزان نمونه برداری برای دستگاه مورد نظر محاسبه می شود.
     - طول داده های مورد نیاز برای تجسم صدا نیز با توجه به پارامترهای "window"، "downsample" و "samplerate" محاسبه می شود.
     - در نهایت نموداری با ابعاد مشخص شده (4*8) ایجاد شده و خطوط نمودار با رنگ سبز (0، 1، 0.29) ترسیم می شود.
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
## "تعریف":
1. **عملکرد پاسخ به تماس صوتی ('audio_callback'):**
       - این تابع احتمالا برای مدیریت داده های صوتی استفاده می شود.
       - "indata"، "frames"، "time" و "status" را به عنوان پارامتر در نظر می گیرد.
       - در داخل تابع، به نظر می رسد که داده های صوتی را پایین می کشد و در یک صف (`q`) ذخیره می کند.
       - فاکتور downsample به عنوان 'downsample' تعریف می شود.
       - سپس داده های صوتی پردازش شده برای تجسم استفاده می شود.

2. **به روز رسانی تابع نمودار ('update_plot'):**
       - این تابع یک نمودار را به روز می کند (احتمالاً تصویرسازی صوتی در زمان واقعی).
       - داده های صوتی را از صف (q) بازیابی می کند و آن را اصلاح می کند.
       - سپس داده های منتقل شده به "plotdata" اختصاص داده می شود.
       - در نهایت، داده های y هر خط در نمودار را به روز می کند.

3. **متغیرهای جهانی:**
       - `plotdata`: یک آرایه ناچیز (با صفرهای ابتدایی) برای ذخیره داده های صوتی.
       - `q`: یک صف برای ذخیره داده های صوتی نمونه برداری شده.
       - `خطوط`: لیستی از اشیاء Line2D (احتمالاً برای ترسیم).

لطفاً توجه داشته باشید که برخی از متغیرها (مانند 'خطوط'، 'dataprot' و کد رندر واقعی) باید با داده ها و اشیاء واقعی جایگزین شوند. این قطعه قرار است در یک برنامه بزرگتر که تصویربرداری صوتی را مدیریت می کند ادغام شود.
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
## «تنظیم طرح»:
ax.set_facecolor((0, 0, 0)): این خط کد رنگ پس زمینه یک شی (محور) مجموعه را در نقشه تعیین می کند. در اینجا، رنگ مشخص شده توسط RGB (0، 0، 0) سیاه است. به عبارت دیگر، این خط کد، پس زمینه را سیاه می کند.
ani = FuncAnimation(fig, update_plot, interval=interval, blit=True): این خط کد برای ایجاد یک انیمیشن در طرح استفاده می شود. این خط کد شامل تابع FuncAnimation و برخی از دستورات شیء fig (شیء حاوی نمودار)، تابع update_plot (که وظیفه تغییر نمودار را بر عهده دارد)، فاصله بین هر فریم انیمیشن (فاصله) و blit=True ( یعنی). فقط از تغییراتی که تغییر کرده اند) به عنوان ورودی.
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
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br><img src="https://github.com/jokernets/audiotoplot/blob/main/Figure%201%202024-04-23%2020_33_05.png" width="500" height="300"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"><br><br>



## نمونه های بیشتر و ویترین 👑

### ویدیو از پروژه 📺


# `اتباط با من `🎈🎃

<a herf="https://www.buymeacoffee.com/jokernets"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="180px">
<a href="mailto:joker.until33@gmail.com"><img align="center" width="60px" src="https://github.com/edent/SuperTinyIcons/raw/master/images/svg/gmail.svg" style="max-width: 100%;"></a><a href="https://www.linkedin.com/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/mohammadfallahnejad/" height="40" width="60" /></a>
































































   

