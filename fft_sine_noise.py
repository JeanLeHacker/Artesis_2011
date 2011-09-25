import pylab
from math import pi, sin
from random import random

def noise(factor=1.0):      # generate noise with given multiplication factor
    return factor * 2.0 * (random() - 0.5)


N = 1280                     # number of taps
f = 100.0                    # frequency of sinewave

x = [sin (2.0*pi*f*i/N)+noise(5.0) for i in range (N)]
F = abs(pylab.fft(x))

pylab.close (1)
pylab.figure(1)
pylab.plot(F[:N/2])
pylab.title ("FFT of noisy sine")
