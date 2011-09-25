import pylab
from math import pi, sin
from conv import conv, noise, plot

N  = 128                    # number of taps
ff = 20                     # frequency of filter
f1 = 10                     # frequency of first  sine
f2 = 50                     # frequency of second sine
t  = 8                      # number of taps in filter

# create FIR mask
mask = [1.0]*ff + [0.0]*(N-ff)

# create FIR template
temp = abs(pylab.ifft(mask))

# truncate, mirror template
filt  = [temp[i] for i in range (8,0,-1)]
filt += [temp[i] for i in range (0,9,+1)]

# use it
x = [(sin (2.0*pi*f1*i/N) + sin (2.0*pi*f2*i/N)) for i in range (N)]
y = conv (x, filt)[:N]

# plot FFT before & after
F = abs(pylab.fft(x))
G = abs(pylab.fft(y))

# plot all
pylab.close (5)
pylab.figure (5)
pylab.plot (F[:N/2])
pylab.plot (G[:N/2], 'r')
pylab.title ("FFT of two-tone and filtered two-tone")

pylab.close (4)
pylab.figure (4)
pylab.plot (x)
pylab.plot (y)
pylab.title ("two-tone and filtered two-tone")

pylab.close (3)
pylab.figure (3)
pylab.plot (filt)
pylab.title ("FIR filter")

pylab.close (2)
pylab.figure (2)
pylab.plot (temp)
pylab.title ("FIR template")

pylab.close (1)
pylab.figure (1)
pylab.plot (mask)
pylab.title ("FIR mask")
