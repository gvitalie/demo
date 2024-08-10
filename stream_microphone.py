import sounddevice as sd


def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    outdata[:] = indata


try:
    with sd.Stream(channels=2, callback=callback):
        input('Press Enter to stop ... ')
except Exception as e:
    print(e)
except KeyboardInterrupt:
    print("\nDisconnected")
