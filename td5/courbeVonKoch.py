from math import sqrt
from matplotlib.pyplot import plot, show, xlim, axis, xkcd
x, y = [float(input("x de A : ")), float(input("x de E : "))], [float(input("y de A : ")), float(input("y de E : "))]
x, y = [x[0]] + [(2*x[0] + x[1])/3, (x[0] + x[1])/2 + (y[0] - y[1])/(2 * sqrt(3)), (2*x[1] + x[0])/3] + [x[1]], [y[0]] + [(2*y[0] + y[1])/3, (y[0] + y[1])/2 + (x[1] - x[0])/(2 * sqrt(3)), (2*y[1] + y[0])/3] + [y[1]]
[xkcd(), plot(x, y, ".-"), xlim(x[0] - 1, x[1] + 1), axis("equal"), show()]