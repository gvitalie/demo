import matplotlib.pyplot as plt
import numpy as np

signFreq1 = 27
signFreq2 = 35
step = 0.001

npTime = np.arange(start=0, stop=1, step=step)
npSin1 = np.sin(2 * np.pi * signFreq1 * npTime)
npSin2 = np.sin(2 * np.pi * signFreq2 * npTime)
cleanSignal = npSin1 + npSin2

plt.subplot(411)
plt.plot(npTime, npSin1, linewidth=1, label=str(signFreq1) + "Hz")
plt.margins(x=0, y=1)
plt.legend()

plt.subplot(412)
plt.plot(npTime, npSin2, linewidth=1, label=str(signFreq2) + "Hz")
plt.margins(x=0, y=1)
plt.legend()

plt.subplot(413)
plt.plot(npTime, cleanSignal, linewidth=1,
         label="Signal " + str(signFreq1) + "Hz and " + str(signFreq2) + "Hz combined")
plt.margins(x=0, y=1)
plt.legend()
# plt.show()

noise = 2.5 * np.random.randn(len(npTime))
noiseSignal = cleanSignal + noise

plt.subplot(414)
plt.plot(npTime,noiseSignal, linewidth=1, label="Signal with noise")
plt.margins(x=0, y=1)
plt.legend()
plt.show()

