
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as siw


samplerate = 44100 # Standard rate of digital sampling.
signallength = 5.  # generating five seconds of audio

nsamples = int(signallength*samplerate)

t = np.linspace(0., signallength, nsamples)

# First, generate a string of independent gaussian random numbers.
# Such a sequence is called "white noise" for reasons we'll see in a moment:
whitenoise = np.random.normal(0.,1.,nsamples)

plt.plot(t, whitenoise)
plt.show()

# Fourier transform this to see its frequency content:
whitenoise_f = np.fft.fft(whitenoise)
f = np.fft.fftfreq(nsamples, 1./samplerate)

plt.plot(f, whitenoise_f.real)
plt.plot(f, whitenoise_f.imag)
plt.title("Fourier transform of noise signal. (blue=real, orange=imag)")
plt.show()

siw.write('WhiteNoise.wav', samplerate, whitenoise/(1.2*np.max(np.abs(whitenoise))))


# Let's filter that noise. Divide by f to construct pink noise:
pinknoise_f = whitenoise_f/np.sqrt((.0001+abs(f)))
plt.plot(f, pinknoise_f.real)
plt.plot(f, pinknoise_f.imag)
plt.show()

# Transform back to the time domain ("inverse" fourier transform ifft):
pinknoise = np.fft.ifft(pinknoise_f)

plt.plot(t, pinknoise.real)
#plt.plot(t, pinknoise.imag)
plt.show()

pinknoise = pinknoise.real
pinknoise -= np.mean(pinknoise)

siw.write('PinkNoise.wav', samplerate, pinknoise/(1.2*np.max(np.abs(pinknoise))))



# Generate "Brown noise", scaling as 1.f**2:
brownnoise_f = whitenoise_f/(.0001+abs(f))
plt.plot(f, brownnoise_f.real)
plt.plot(f, brownnoise_f.imag)
plt.show()

# Transform back to the time domain ("inverse" fourier transform ifft):
brownnoise = np.fft.ifft(brownnoise_f)

plt.plot(t, brownnoise.real)
#plt.plot(t, brownnoise.imag)
plt.show()

brownnoise = brownnoise.real
brownnoise -= np.mean(brownnoise)

siw.write('BrownNoise.wav', samplerate, brownnoise/(1.2*np.max(np.abs(brownnoise))))
