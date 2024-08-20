import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import rfft, rfftfreq, irfft

signFreq1 = 27
signFreq2 = 35
step = 0.001

npTime = np.arange(start=0, stop=1, step=step)
npSin1 = np.sin(2 * np.pi * signFreq1 * npTime)
npSin2 = np.sin(2 * np.pi * signFreq2 * npTime)
cleanSignal = npSin1 + npSin2

plt.subplot(421)
plt.plot(npTime, npSin1, linewidth=1, label=str(signFreq1) + "Hz")
plt.margins(x=0, y=1)
plt.legend()

plt.subplot(422)
plt.plot(npTime, npSin2, linewidth=1, label=str(signFreq2) + "Hz")
plt.margins(x=0, y=1)
plt.legend()

plt.subplot(423)
plt.plot(npTime, cleanSignal, linewidth=1,
         label="Signal " + str(signFreq1) + "Hz and " + str(signFreq2) + "Hz combined")
plt.margins(x=0, y=1)
plt.legend()
# plt.show()

noise = 2.5 * np.random.randn(len(npTime))
noiseSignal = cleanSignal + noise

plt.subplot(424)
plt.plot(noise, linewidth=1, label="Noise")
plt.margins(x=0, y=1)
plt.legend()

plt.subplot(425)
plt.plot(npTime,noiseSignal, linewidth=1, label="Signal with noise")
plt.margins(x=0, y=1)
plt.legend()
# plt.show()

plt.subplot(426)
n = len(npTime)
yf = rfft(noiseSignal)
xf = rfftfreq(n,step)
plt.plot(np.abs(yf), linewidth=1,label="DFT")
plt.margins(x=0, y=0.5)
plt.legend()

plt.subplot(427)
yf_abs = np.abs(yf)
indices = yf_abs>300   # filter out those value under 300
yfClean = indices * yf # noise frequency will be set to 0
plt.plot(np.abs(yfClean), linewidth=1, label="DFT Removed Noise Frequencies")
plt.margins(x=0, y=0.5)
plt.legend()

plt.subplot(428)
newFClean = irfft(yfClean)
plt.plot(npTime, newFClean, linewidth=1, label="DFT inversed back to Time signal")
plt.margins(x=0, y=1)
plt.legend()
plt.show()
