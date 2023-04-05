
import numpy as np
import matplotlib.pyplot as plt


t = np.linspace(0., 10., 10000)
dt = t[1]-t[0]
nsamples = len(t)

# A smooth periodic function with many fourier modes:
signal = np.exp(np.cos(2.*np.pi*t))
# A "sawtooth" oscillation, still periodic, but discontinuous, which requires
# high-order fourier components to represent:
# signal = t%1.

plt.plot(t, signal)
plt.show()

signal_f = np.fft.fft(signal)
f = np.fft.fftfreq(nsamples, dt)

plt.plot(f, signal_f.real)
plt.plot(f, signal_f.imag)
plt.show()

plt.plot(f, np.log(np.abs(signal_f.real)))
plt.plot(f, np.log(np.abs(signal_f.imag)))
plt.show()
