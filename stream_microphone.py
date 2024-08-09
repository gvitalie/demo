# Usage — python-sounddevice, version 0.4.7
# https://python-sounddevice.readthedocs.io/en/0.4.7/usage.html#callback-streams

import sounddevice as sd
duration = 5.5  # seconds


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata


samplerate = 44100
blocksize = 10
latency = 'high'
channels = 2

print('Listening microphone')
with sd.Stream(channels=channels,
               callback=callback,
               samplerate=samplerate,
               blocksize=blocksize,
               never_drop_input=False):
    # sd.sleep(int(duration * 1000))
    input("Press any key to stop ...")

