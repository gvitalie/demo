# Usage — python-sounddevice, version 0.4.7
# https://python-sounddevice.readthedocs.io/en/0.4.7/usage.html#callback-streams

import sounddevice as sd
duration = 5.5  # seconds


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata


print('Listening microphone')
with sd.Stream(channels=2, callback=callback):
    sd.sleep(int(duration * 1000))

