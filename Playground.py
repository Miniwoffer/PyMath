import matplotlib.pyplot as pp
import matplotlib.patches as patches
import numpy as np


def hoyre_rigmans(func, x1, x2, interval=10,fig1 = pp.plot()):
    summation = 0.0
    dx = float(x2-x1)/interval
    interval += 1
    for i in range(1, interval):
        summation += func(x1+i*dx)
        ax1 = fig1.add_subplot(111, aspect='equal')
        ax1.add_patch(
            patches.Rectangle(
                (x1+ i*dx -dx,0),  # (x,y)
                dx,  # width
            func(x1 + i * dx),  # height
                facecolor="#ff0000",
                hatch='\ ',
                edgecolor="#000000",
                alpha=0.5
            )
        )

    summation *= dx
    return summation
    pass


def venstre_rigmans(func, x1, x2, interval=10,fig1= pp.plot()):
    summation = 0.0
    dx = float(x2-x1)/interval
    for i in range(0, interval):
        summation += func(x1+i*dx)
        ax1 = fig1.add_subplot(111, aspect='equal')
        ax1.add_patch(
            patches.Rectangle(
                (x1+i*dx,0),  # (x,y)
                dx,  # width
            func(x1 + i * dx),  # height
                facecolor="#0000ff",
                hatch='/',
                edgecolor="#000000",
                alpha=0.5,
            )
        )
    summation *= dx
    return summation
    pass


def trapes_metoden(func, a, b, interval=10):
    return (venstre_rigmans(func,a,b,interval) + hoyre_rigmans(func,a,b,interval))/2.0
    pass

def fu(x):
    return x**2

def fuint(x):
    return (x**3)/3.0

start = 1
end = 0
intervals = 10
fig1 = pp.figure()
print fuint(start)-fuint(end)
hoyre_rigmans(fu,end,start,intervals,fig1)
venstre_rigmans(fu,end,start,intervals,fig1)

x = np.linspace(0,4,1000)
y = fu(x)
iy = fuint(x)
pp.plot(x,y)
pp.axis([0,1,0,1])
#pp.grid()
pp.xlabel("x")
pp.ylabel("y")
pp.title("Numeric integration")

pp.show()


def f(x_in):
    return x_in
    pass


def eulers_metode(y_start, x_start, x_end, f, intervals = 10):
    delta_x = float(x_end-x_start)/intervals
    y = y_start;
    for i in range(0, intervals):
        y += delta_x*f(x_start+i*delta_x)
    return y
    pass

print eulers_metode(1, 0, 2, f(x), 4)
