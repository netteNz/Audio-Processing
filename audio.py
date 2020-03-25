%matplotlib inline
import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq

samplerate, data = wavfile.read('mirrored.wav')

plt.style.use('classic')

print(samplerate)
print(data.shape)
data.shape[0]
samples = data.shape[0]
print(samples)

plt.plot(data[:300])

datafft = fft(data)
#Get the absolute value of real and complex component:
fftabs = abs(datafft)
freqs = fftfreq(samples, 1/samplerate)

plt.plot(freqs, fftabs)

plt.xlim( [10, samplerate/2] )
plt.xscale( 'log' )
plt.grid( True )
plt.xlabel( 'Frequency (Hz)' )
plt.plot(freqs[:int(freqs.size/2)],fftabs[:int(freqs.size/2)])