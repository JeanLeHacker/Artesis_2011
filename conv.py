import pylab
from math import pi, sin
from random import random

def conv(x, y):             # return convolution of x and y
    P, Q, N = len(x), len(y), len(x)+len(y)-1
    z = []
    for k in range (N):
        t = 0.0
        lower = max(0,   k-(Q-1))
        upper = min(P-1, k      )

        for i in range(lower, upper+1):
            t = t + x[i] * y[k-i]
        
        z.append(t)

    return z

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
y = x
z = conv (x, y)
plot (x,z)


