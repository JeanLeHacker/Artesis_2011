import pylab
from math import pi, sin

N  = 128                    # number of taps
f1 = 10.0                   # frequency of first  sinewave
f2 = 30.0                   # frequency of second sinewave

x = [(sin (2.0*pi*f1*i/N) + sin (2.0*pi*f2*i/N)) for i in range (N)]
F = abs(pylab.fft(x))

pylab.close (1)
pylab.figure(1)
pylab.plot(x)
pylab.title ("two-tone")

pylab.close (2)
pylab.figure(2)
pylab.plot(F[:N/2])
pylab.title ("FFT of two-tone")
