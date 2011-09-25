import pylab
from math import pi, sin
from random import random
from conv import conv, noise, plot

N = 100
x = [sin (2.0*pi*i/N) for i in range (N)]
y = [i + noise(2.0) for i in x]
z = conv (y, y)
plot (y, z)
