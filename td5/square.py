import matplotlib as mpl
import matplotlib.pyplot as mplpp
from random import choice



def square(origin, radius):
    colorList = ["xkcd:tan", "xkcd:aqua", "xkcd:lime", "xkcd:gold", "xkcd:light red",
                "xkcd:steel blue", "xkcd:grass", "xkcd:orchid", "xkcd:emerald", "xkcd:pastel pink",
                "xkcd:lemon", "xkcd:light indigo", "xkcd:vermillion", "xkcd:muddy brown", "xkcd:electric pink",
                "xkcd:heliotrope", "xkcd:wisteria", "xkcd:sunflower", "xkcd:royal", "xkcd:ruby",
                "xkcd:vivid blue", "xkcd:ice", "xkcd:greenblue", "xkcd:wintergreen", "xkcd:charcoal grey"]
    xList = 2 * [origin[0] + radius] + 2 * [origin[0] - radius]
    yList = [origin[1] + radius] + 2 * [origin[1] - radius] + [origin[1] + radius]
    mplpp.fill(xList, yList, choice(colorList))



def target(origin, radius, n):
    radiuses = [radius - (radius / n) * i for i in range(n)]
    for i in radiuses:
        square(origin, i)



def innerTangent(origin, radius, n):
    radiuses = [radius / (2 ** i) for i in range(n)]
    originsY = [origin[0] + radius / (2 ** i) for i in range(n)]
    for i in range(n):
        square((origin[0], originsY[i]), radiuses[i])



def tower(origin, radius, n):
    radiuses = [radius / (2 ** i) for i in range(n)]
    originsY = [origin[0] -  3 * radius / (2 ** i) for i in range(n)]
    for i in range(n):
        square((origin[0], originsY[i]), radiuses[i])



def stairs(origin, radius, n):
    originsX = [origin[0] * 2 * (i+1) for i in range(n)]
    originsY = [origin[1] * 2 * (i+1) for i in range(n)]
    for i in range(n):
        square((originsX[i], originsY[i]), radius)


def squareSquared(origin, radius, n):
    for _ in range(n-1):
        square(origin, radius)
        origin = (origin[0], origin[1] + 2 * radius)
    for _ in range(n-1):
        square(origin, radius)
        origin = (origin[0] + 2 * radius, origin[1])
    for _ in range(n-1):
        square(origin, radius)
        origin = (origin[0], origin[1] - 2 * radius)
    for _ in range(n-1):
        square(origin, radius)
        origin = (origin[0] - 2 * radius, origin[1])



def pyramid(origin, radius, n):
    originalOrigin = origin
    for i in range(n):
        origin = originalOrigin
        for _ in range(i):
            square(origin, radius)
            origin = (origin[0] + 2 * radius, origin[1])
        originalOrigin = (originalOrigin[0] - radius, originalOrigin[1] - 2 * radius)



def spiral(origin, radius, n):
    for i in range(n):
        if (i % 4 == 0):
            for _ in range(i):
                square(origin, radius)
                origin = (origin[0], origin[1] + 2 * radius)
        if (i % 4 == 1):
            for _ in range(i):
                square(origin, radius)
                origin = (origin[0] + 2 * radius, origin[1])
        if (i % 4 == 2):
            for _ in range(i):
                square(origin, radius)
                origin = (origin[0], origin[1] - 2 * radius)
        if (i % 4 == 3):
            for _ in range(i):
                square(origin, radius)
                origin = (origin[0] - 2 * radius, origin[1])



pyramid((10, 10), 10, 20)

mplpp.axis("equal")
mplpp.show()