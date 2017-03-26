from matplotlib.pyplot import *
from math import *
from numpy import *

def f(x, y):
    return x*y

def ifunc(x):
    return e**((x**2)/2)

def eulers_metode(y_start, x_start, x_end, integrated_function, intervals = 10):
    delta_x = float(x_end-x_start)/intervals
    y = y_start
    for i in range(0, intervals):
        plot(x_start + i * delta_x, y,"*")
        y += delta_x*integrated_function(x_start+i*delta_x, y)
    plot(x_end, y, "*")
    return y

x = linspace(0, 2, 400)
y = ifunc(x)

xlabel("x")
ylabel("y")
title("Numeric differential equation")
plot(x, y)
eulers_metode(1, 0, 2, f, 10)

show()
