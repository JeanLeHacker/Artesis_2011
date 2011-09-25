import pylab
from math import pi, sin

N = 128                     # number of taps
f = 10.0                    # frequency of sinewave

x = [sin (2.0*pi*f*i/N) for i in range (N)]
F = abs(pylab.fft(x))

pylab.close (1)
pylab.figure(1)
pylab.plot(F[:N/2])
pylab.title ("FFT of pure sine")
