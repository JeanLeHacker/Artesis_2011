import pylab
from cconv import conv, float_arr
from math import pi, sin
from random import random

def noise(factor=1.0):      # generate noise with given multiplication factor
    return factor * 2.0 * (random() - 0.5)

def plot(x, z):             # plot input x versus convolution z
    pylab.close(1)
    pylab.figure(1)
    pylab.plot (x, 'b', label="sine")
    pylab.plot ([abs(i/max(z)) for i in z], 'r', label="convolution")
    pylab.title ("convolution of pure sine")
    pylab.legend()


N = 100
x = [sin (2.0*pi*i/N) for i in range (N)]

xx = float_arr(N)
zz = float_arr(2*N-1)

for i in range (N):
    xx[i] = sin (2.0*pi*i/N) 
conv (xx, N, xx, N, zz, 2*N-1)

z = []
for i in range (2*N-1):
    z.append(zz[i])

plot (x,z)


