
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as siw


samplerate, tptsignal = siw.read("TrumpetA440.wav")
print(samplerate)

nsamples = len(tptsignal)
finaltime = nsamples/samplerate
print(finaltime)

t = np.linspace(0., finaltime, nsamples)

plt.plot(t, tptsignal)
plt.show()

# Fourier transform the signal:
tpt_f = np.fft.fft(tptsignal)
f = np.fft.fftfreq(nsamples, 1./samplerate)
plt.plot(f, tpt_f.real)
plt.plot(f, tpt_f.imag)
plt.show()

# Define a "window function" that smoothly interpolates between 0 and 1 in a
# window of given center and width:

def windowfunction(f, f0, deltaf, transitionwidth):
    return (1./(1.+np.exp(-(f-(f0-.5*deltaf))/transitionwidth)))*(1./(1.+np.exp((f-(f0+.5*deltaf))/transitionwidth)))

#ff = np.linspace(-300,300, 1000)
#plt.plot(ff, windowfunction(ff, 150, 50, 3))
#plt.show()

def symmfilter(f, f0, deltaf, transitionwidth):
    return 1.-windowfunction(f, f0, deltaf, transitionwidth) - windowfunction(f, -f0, deltaf, transitionwidth)

#ff = np.linspace(-300,300, 1000)
#plt.plot(ff, symmfilter(ff, 150, 50, 3))
#plt.show()


#Filter the 440-hz information from the audio:
tpt_fundremoved_f = tpt_f*symmfilter(f, 440, 50, 3)
plt.plot(f, np.log(tpt_fundremoved_f.real**2 + tpt_fundremoved_f.imag**2))
plt.show()

# Inverse-FFT this so we can hear it:
tpt_fundremoved = np.fft.ifft(tpt_fundremoved_f).real

plt.plot(t, tpt_fundremoved)
plt.show()

siw.write("Trumpet_fundremoved.wav", samplerate, tpt_fundremoved/(1.2*np.max(np.abs(tpt_fundremoved))))


# Remove all odd-numbered multiples of 440 Hz:
tpt_evenharms_f = np.copy(tpt_f)
for i in range(1, 45, 2):
    tpt_evenharms_f *= symmfilter(f, 440*i, 50, 3)

plt.plot(f, np.log(tpt_evenharms_f.real**2 + tpt_evenharms_f.imag**2))
plt.show()

tpt_evenharms = np.fft.ifft(tpt_evenharms_f).real

siw.write("Trumpet_evenharmonics.wav", samplerate, tpt_evenharms/(1.2*np.max(np.abs(tpt_evenharms))))
