import sounddevice as sd


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata


try:
    with sd.Stream(channels=1, callback=callback, samplerate=8000):
        input('Press Enter to stop ... ')
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("\nDisconnected")
