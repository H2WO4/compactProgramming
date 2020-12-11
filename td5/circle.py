import matplotlib as mpl
import matplotlib.pyplot as mplpp
from math import sin, cos, pi
from random import choice



def circle(origin, radius, precision = 100):
    colorList = ["xkcd:tan", "xkcd:aqua", "xkcd:lime", "xkcd:gold", "xkcd:light red",
                "xkcd:steel blue", "xkcd:grass", "xkcd:orchid", "xkcd:emerald", "xkcd:pastel pink",
                "xkcd:lemon", "xkcd:light indigo", "xkcd:vermillion", "xkcd:muddy brown", "xkcd:electric pink",
                "xkcd:heliotrope", "xkcd:wisteria", "xkcd:sunflower", "xkcd:royal", "xkcd:ruby",
                "xkcd:vivid blue", "xkcd:ice", "xkcd:greenblue", "xkcd:wintergreen", "xkcd:charcoal grey"]
    pointList = [i * (2 * pi / precision) for i in range(precision)]
    xList = [origin[0] + sin(i) * radius for i in pointList]
    yList = [origin[1] + cos(i) * radius for i in pointList]
    mplpp.fill(xList, yList, choice(colorList))



def target(origin, radius, n):
    radiuses = [radius - (radius / n) * i for i in range(n)]
    for i in radiuses:
        circle(origin, i)



def innerTangent(origin, radius, n):
    radiuses = [radius / (2 ** i) for i in range(n)]
    originsX = [origin[0] - radius / (2 ** i) for i in range(n)]
    for i in range(n):
        circle((originsX[i], origin[1]), radiuses[i])



def outerTangent(origin, radius, n):
    radiuses = [radius / (2 ** i) for i in range(n)]
    originsX = [origin[0] -  3 * radius / (2 ** i) for i in range(n)]
    for i in range(n):
        circle((originsX[i], origin[1]), radiuses[i])



outerTangent((0, 0), 10, 5)

mplpp.axis("equal")
mplpp.show()